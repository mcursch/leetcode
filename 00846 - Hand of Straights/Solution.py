class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        # Counter will produce a hashmap of the array, where each value is mapped to its count
        count = Counter(hand)
        # Go through the array once, sort it first
        hand.sort()
        for card in hand:
            if count[card]:
                # go through the next groupSize number cards ( to form a group)
                for i in range(card,card + groupSize):
                    # if the card at i doesnt exist (or its count is 0), then we cant form a group with current card, so return false
                    if not count[i]:
                        return False
                    # include this card (decremement count)
                    count[i] -= 1
        return True

