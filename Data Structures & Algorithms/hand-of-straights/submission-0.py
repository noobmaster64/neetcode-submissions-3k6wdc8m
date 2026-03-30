class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        card_count = Counter(hand)
        for card in sorted(card_count):
            count = card_count[card]
            if count >0:
                for j in range(groupSize):
                    if card_count[card +j] < count:
                        return False
                    card_count[card +j] -= count
            
        return True 
