
class Solution:

  def subArrayRanges(self, nums):
    n = len(nums)

    # Helper function to count how many subarrays
    # each element contributes to as min OR max
    def count(is_min):
        res = [0]*n                          # stores contribution count for each index
        stack = []                           # monotonic stack

        # iterate through array + one extra step (i==n for cleanup)
        for i in range(n + 1):

            while stack and (i==n or (nums[stack[-1]] > nums[i] if is_min else nums[stack[-1]] < nums[i])):
                j = stack.pop()
                k = stack[-1] if stack else -1

                res[j] = (j-k)*(i-j)

            stack.append(i)

        return res
    
    # Count contibution for being minimum in subarrays
    min_contrib = count(True)

    # Count contribution for being maximum in subarrays
    max_contrib = count(False)

    return sum((max_contrib[i] - min_contrib[i])*nums[i] for i in range(n))