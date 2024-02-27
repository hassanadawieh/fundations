'''
Given a string s, find the length of the longest
substring without repeating characters.

Example 1:

Input: s =    "abcabcbb"   
Output : 3     ^

Explanation : the answer is "abc", with the length of 3.

Example 2:

Input : s = "bbbbb"
Output : 1

Explanation : the answer is "b", with the length of 1.

Example 3:

'''

def solution(s:str):
    max_length = 0
    char_set = set()
    left = 0
    # sliding window
    for right in range(len(s)):

        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length , right-left+1)

    return max_length

print(solution("abcdabcbb"))    

