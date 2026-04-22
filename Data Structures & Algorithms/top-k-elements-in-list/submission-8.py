from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return k most requent element within nums array
            #answer is unique, meaning there wont be issues with
                #same freq for more then k items 
        #first, we count freq of numbers and sotre in dict
        #after, we sort dicts by freq as key and values as the number
        #then add to ouput array until k items and return

        freqDict = defaultdict(int)

        for num in nums:
            freqDict[num] = freqDict.get(num,0) + 1
        
        elementDict = defaultdict(list)

        #iterate throughout the freqDict
        for number, freq in freqDict.items():
            elementDict[freq].append(number)
        
        #now go through in sorted order of key largest to smallest
        key_order = sorted(elementDict.keys(), reverse = True)

        output = []
        index = 0

        while len(output) < k:
            output.extend(elementDict[key_order[index]])
            index += 1
        return output
        
        