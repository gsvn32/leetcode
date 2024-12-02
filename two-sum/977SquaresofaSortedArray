#using two pointer solution, 1st arry to store squares, second array to store the result, time: O(n) space: O(n)
#Run time: 7ms, beats 80.09%
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        i=0
        j=len(nums)-1
        result = len(nums)*[0]
        resindex=len(nums)-1
        if i==j:
            result[resindex] = nums[i]
            return result
        while i < j:
            #print(result)
            if nums[i] < nums[j]:
                result[resindex] = nums[j]
                j-=1
                resindex-=1
            if nums[i] > nums[j]:
                result[resindex] = nums[i]
                i+=1
                resindex-=1
            if nums[i] == nums[j] and i !=j:
                result[resindex] = nums[i]
                resindex-=1
                result[resindex] = nums[j]
                resindex-=1
                i+=1
                j-=1
            if i==j:
                result[resindex] = nums[i]
                resindex-=1
                i+=1

        return result
        
