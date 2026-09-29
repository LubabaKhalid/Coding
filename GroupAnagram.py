"""49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]"""

#Brute Force Logic
"""strs = ["eat","tea","tan","ate","nat","bat"]

groups=[]

for i in range(len(strs)):
    flag=False
    for group in groups:
        if sorted(strs[i])==sorted(group[0]):
            group.append(strs[i])
            flag=True
            break

    if not flag:
        groups.append([strs[i]])   
print(groups) """

#HashMap + Sorting Optimized Solution 

def anagram(strs):
    dic={}
    for s in strs:
        key=''.join(sorted(s))
        if key not in dic:
            dic[key]=[]
        dic[key].append(s)
    return list(dic.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(anagram(strs))

