"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 """

#Brute Force logic O(n^3)
"""def Sum3(nums):
    res=set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k]==0:
                    tri=tuple(sorted([nums[i],nums[j],nums[k]]))
                    res.add(tri)
        
    return [list(x) for x in res]

nums = [-1,0,1,2,-1,-4]
print(Sum3(nums))"""

#Optimized Solution O(n^2)
def Sum3(nums):
    nums.sort()
    res=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l=i+1
        r=len(nums)-1
        while l<r:
            if nums[i]+nums[l]+nums[r]==0:
                res.append([nums[i],nums[l],nums[r]])
                l=l+1
                r=r-1
                while l<r and nums[l]==nums[l-1]:
                    l=l+1
                while l<r and nums[r]==nums[r+1]:
                    r-=1
                    
            elif nums[i]+nums[l]+nums[r]<0:
                l=l+1
            else:
                r-=1
    return res


nums = [-1,0,1,2,-1,-4]
print(Sum3(nums))