class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        Visited = set()

        def has_cycle(u,parent):
            Visited.add(u)
            for neighbour in adj[u]:
                if neighbour == parent:
                    continue
                if neighbour in Visited:
                    return True 
                if has_cycle(neighbour,u):
                    return True
        if n>0 and has_cycle(0,-1):
            return False
        
        return n == len(Visited)
        