"""3. Longest Substring Without Repeating Characters

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring."""

# Brute Force Logic 
#s = "abcabcbb"
#s = "dvdf"
#s = "abcaef"
#s="aaaaab"
s = "abcbde"
r=0
l=[]
maxi=0
for i in range(len(s)):
    if s[i] in l:
        while s[i] in l:
            l.pop(0)
            r-=1
    l.append(s[i])
    r=r+1
    if maxi<r:
        maxi=r
print(maxi)
    