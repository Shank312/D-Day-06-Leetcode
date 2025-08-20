
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)                          # maps prefix-sum -> how many times seen
        count[0] = 1                                      # empty prefix (helps handle subarrays starting at index 0)
        pref = 0                                          # current prefix sum
        ans = 0                                           # number of subarrays summing to k
        for x in nums:
            pref += x
            ans += count[pref-k]                          # add number of previous prefixes that would form sum k
            count[pref] += 1                              # record that we've now seen this prefix sum
        return ans

