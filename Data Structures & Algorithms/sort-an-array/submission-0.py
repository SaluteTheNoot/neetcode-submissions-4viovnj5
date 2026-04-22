class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #merge sort
            #divides the array into two halves, 
            #recursively sorts each half, 
            #and then merges the sorted halves
        
        l,r = 0, len(nums)
        m = (l+r)//2
        if l >= r:
            return

        if r == 1:
            return nums
        
        if r == 2:
            if nums[0] > nums[1]:
                hold = nums[0]
                nums[0] = nums[1]
                nums[1] = hold
                print(nums)
                return nums
        #[3,2,4,1] --> [2,3] [1,4]

        first = self.sortArray(nums[l:m])
        second = self.sortArray(nums[m:r])
        first_index = 0
        second_index = 0
        output = []

        while first_index < len(first) and second_index < len(second):
            if first[first_index] < second[second_index]:
                output.append(first[first_index])
                first_index += 1
            else:
                output.append(second[second_index])
                second_index += 1
        
        if first_index < len(first):
            output.extend(first[first_index:])
        if second_index < len(second):
            output.extend(second[second_index:])
       
        return output


        

        