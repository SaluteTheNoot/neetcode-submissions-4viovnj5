from collections import defaultdict

class TimeMap:
    
    def __init__(self):
        self.values = defaultdict(list)
        # Using defaultdict to automatically handle missing keys with empty lists

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Perform binary search to find the correct insertion index
        self.values[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""
        
        l, r = 0, len(self.values[key])-1
        while l <= r:
            m = (l + r) // 2
            if timestamp > self.values[key][m][1]:
                l = m + 1
            elif timestamp < self.values[key][m][1]:
                r = m - 1  # Changed from m - 1 to m
            else:
                return self.values[key][m][0]
        
        # After the loop, l is the insertion point
        # The desired value is at index l - 1 if l > 0
        if l == 0:
            return ""
        else:
            return self.values[key][l - 1][0]
    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key, value, timestamp)
# param_2 = obj.get(key, timestamp)