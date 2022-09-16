def next_permutation(nums):
    n=len(nums)
    tmp2=0
    tmp=-1
    for i in range(n-1,-1,-1):
        if nums[i-1]<nums[i]:
            tmp=i-1
         
            break
    if tmp<0:
        nums.reverse()
    else:
        for j in range(n-1,-1,-1):
            if nums[j]>nums[tmp]:
                tmp2=j
        
                break
        nums[j],nums[tmp]=nums[tmp],nums[j]
        nums[tmp+1:]=reversed(nums[tmp+1:])
    return nums
