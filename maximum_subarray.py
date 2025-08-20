
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize two variables:
        # 'cur' will track the maximum subarray sum ending at the current index
        # 'best' will track the global maximum subarray sum found so far
        cur = best = nums[0]

        # Loop through the array starting from the 2nd element (nums[1:])
        for x in nums[1:]:
              # Decide whether to start a new subarray at 'x'
              # OR extend the previous subarray by adding 'x'
              # (whichever gives a larger sum)
              cur = max(x, cur + x)

              # Update the global maximum if the current subarray sum is larger
              best = max(best, cur)

        return best
    
