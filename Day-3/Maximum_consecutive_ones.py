from typing import List

class Solution:
    def findconsecutiveone(self,nums: List[int]) -> int:
        count = 0
        maxi = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
            else:
                count = 0
            maxi = max(maxi,count)
        return maxi
    
if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1,1]
    obj = Solution()
    ans = obj.findconsecutiveone(nums)
    print("The maximum  consecutive 1's are", ans)