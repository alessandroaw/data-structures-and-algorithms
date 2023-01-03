class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Idea:
        # store the index for each element on hash map
        # for each element x find the pair (target - x)
        # if x and the pair is the same then check if minimum two element exist
        # return the two sum

        nums_set = set(nums)
        count_dict = {}

        for i, v in enumerate(nums):
            if count_dict.has_key(v):
                count_dict[v].append(i)
            else:
                count_dict[v] = [i]

        for n in nums_set:
            remain = target - n

            if remain == n:
                if len(count_dict[n]) > 1:
                    return count_dict[n][0:2]
            else:
                if count_dict.has_key(remain):
                    return [count_dict[n][0], count_dict[remain][0]]
