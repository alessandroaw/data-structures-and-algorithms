# array and hashing
# TC: O(n)
# SC: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        # get the count of all number in nums O(n)
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # sort based on the most frequent
        # create an array of frequency O(n)
        freq = [[] for x in range(len(nums) + 1)]

        for (key, v) in count.items():
            freq[v].append(key)

        res = []
        # combine the result array O(k)
        for i in range(len(freq) - 1, 0, -1):
            if len(freq[i]) > 0:
                res += freq[i]

        # Time complexity O(n) + O(n) + O(k) = O(n)
        # Space complexity O(n) + O(n) = O(n)

        return res[:k]
