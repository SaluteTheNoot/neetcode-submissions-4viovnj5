class Solution:
    def isValid(self, s: str) -> bool:
        hashPar = {')':'(', '}':'{', ']':'['}
        tracker = []
        for x in s:
            if x in hashPar:
                if len(tracker) == 0 or tracker[-1] != hashPar[x]:
                    return False
                else:
                    tracker.pop()
            else:
                tracker.append(x)
        if len(tracker) != 0:
            return False
        else:
            return True

        