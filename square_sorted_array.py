
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)              # length of the array
        res = [0]*n                # result array (same size as nums)
        l, r = 0, n-1              # two pointers: left at start, right at end
        i = n-1                    # position to fill in result (start from end)

        # loop until the right pointer crosses the right
        while l <= r:
            # Compare absolute  values at both ends
            if abs(nums[l])>abs(nums[r]):
                res[i] = nums[l]*nums[l]             # square left value
                l += 1                               # move left pointer
            else:
                res[i] = nums[r]*nums[r]             # square right value
                r -= 1                               # move right pointer
            i -= 1                               # move result index to left

        return res                                   # return the sorted squares array
