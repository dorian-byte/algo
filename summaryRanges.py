class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
			return nums
	# left is exclusive and right is inclusive and always right gets incremented by 1 .
	# Then we check if nums[i+1] != right+=1, meaning up until now left-right is a range, 
	# so add them into ans updating left & right.
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
        # after the loop exhausts left and right still holds values, so adding them
        if left!=right:
            ans.append(f"{left}->{right}")
        else:
            ans.append(f"{left}")
        return ans
