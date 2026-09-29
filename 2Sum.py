#You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

 

#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#Example 2:

#Input: nums = [3,2,4], target = 6
#Output: [1,2]
#Example 3:

#Input: nums = [3,3], target = 6
#Output: [0,1]

#nums=[2,7,11,15]

#this solution when nums is sorted O(n)
"""nums=[3,3]
target=6
l=0
r=len(nums)-1
flag=True
while l<r:
    total=nums[l]+nums[r]
    if total==target:
        print(l,r)
        flag=False
        break
    elif total<target:
        l=l+1
    else:
        r=r-1
if flag:
    print(-1)"""

#Brute Force Solution O(n^2)
def Sum2(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

nums=[2,3,7,11,15]
target=9
print(Sum2(nums,target))


# nums is unsorted hashing O(n)
"""def Sum2(nums,t):
    dic={}
    for i in range(len(nums)):
        res=t-nums[i]
        if res in dic:
            return [i,dic[res]]
        dic[nums[i]]=i

nums=[2,7,11,5]
print(Sum2(nums,9))"""
