class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        alphabet_count = Counter(s)
        current_reading = set()
        current_length = 0
        partitions = []
        for ch in s:
            current_reading.add(ch)
            alphabet_count[ch] -= 1
            current_length += 1

            if alphabet_count[ch] ==0:
                current_reading.remove(ch)
            if len(current_reading) ==0:
                partitions.append(current_length)
                current_length =0
        
        return partitions 
            
