class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
			return nums
		left, right = nums[0], nums[0]
        ans = []
        for i in range(len(nums)-1):
            if nums[i+1] != right+1:
                if left!=right:
                    ans.append(f"{left}->{right}")
                    left = nums[i+1]
                    right = nums[i+1]-1

                else:
                    ans.append(f"{left}")
                    left = nums[i+1]
                    right = nums[i+1]-1
            right+=1
        if left!=right:
            ans.append(f"{left}->{right}")
        else:
            ans.append(f"{left}")
        return ans
