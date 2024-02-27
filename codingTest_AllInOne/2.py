""" 128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/
"""

longest = 0
num_dict = {}

nums = map(int, input().split())

for num in nums:
    num_dict[num] = True

for num in num_dict:
    if num-1 not in num_dict:
        cnt = 1
        target = num+1

        while target in num_dict:
            target += 1
            cnt += 1
        longest = max(longest, cnt)
print(longest)