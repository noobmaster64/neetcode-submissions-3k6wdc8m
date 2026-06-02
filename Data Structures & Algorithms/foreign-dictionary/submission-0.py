class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
    # Initialize adjacency list and in-degree map for ALL unique characters
        graph = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}
    
    # 1. Build the Graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
        
        # Check prefix invariant violation edge case (e.g., ["abc", "ab"])
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            
        # Find the first differing character
            for k in range(min_len):
                if w1[k] != w2[k]:
                    parent, child = w1[k], w2[k]
                # Avoid duplicate edge counting
                    if child not in graph[parent]:
                        graph[parent].add(child)
                        in_degree[child] += 1
                    break # Remaining characters provide no order data
                
    # 2. Kahn's Algorithm (BFS)
    # Collect all nodes with 0 in-degree
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []
    
        while queue:
            current = queue.popleft()
            result.append(current)
        
        # Process neighbors
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                
    # 3. Validation
    # If result length doesn't match total unique characters, a cycle exists
        if len(result) < len(in_degree):
            return ""
        
        return "".join(result)
        