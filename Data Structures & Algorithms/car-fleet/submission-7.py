class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [0] * len(position)
        hashPos = {}
        if len(position) == 1:
            return 1
        for x in range(len(position)):
            hashPos[position[x]] = speed[x]
        position = sorted(position)
        for x in range(len(position)):
            speed[x] = hashPos[position[x]]
        #how to find time?
        for x in range(len(position)):
            time[x] = (target - position[x])/speed[x]
        groups = 1
        for x in range(len(time)-2,-1,-1):
            if time[x] <= time[x+1]:
                time[x] = time[x+1]
            elif time[x] > time[x+1]:
                groups += 1
        return groups