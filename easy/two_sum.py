# LeetCode Practice
# Problem - TwoSum
# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    i = 1
    holding_list = []
    index_list = []
    for num in nums:
        for step in range(1, len(nums)):
            sum = num + nums[step]
            holding_list.append(sum)
            if sum == target:
                index_list.append(i-1)
                index_list.append(step)
                return index_list
        i += 1        

