class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums, i, res):
        appeared = set()
        j = i + 1
        while j < len(nums):
            comp = -nums[i] - nums[j]
            if comp in appeared:
                res.append([nums[i], nums[j], comp])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            appeared.add(nums[j])
            j += 1
