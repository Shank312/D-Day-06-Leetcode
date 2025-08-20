
class Solution:
    def maxArrayValue(self, nums):
        # Start from the last element
        cur = ans = nums[-1]

        # Traverse the array from right to left
        for i in range(len(nums) -2, -1, -1):

            # If current number is <= cur, merge it with cur
            if nums[i] <= cur:
                cur += nums[i]
            else:
                cur = nums[i]

            # Keep track of the maximum value so far
            ans = max(ans, cur)

        return ans

