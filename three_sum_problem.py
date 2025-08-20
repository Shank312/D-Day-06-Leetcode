
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()             # Step 1: Sort array
        n = len(nums)
        res = []

        for i in range(n-2):    # Step 2: Fix nums[i]
            if i>0 and nums[i] == nums[i-1]:
                continue        # Skip: dublicate i

            a = nums[i]
            l, r = i+1, n-1     # Step 3: Two-pointer search

            while l < r:
                s = a + nums[l] + nums[r]

                if s==0:        # Found a triplet
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip dublicate nums[l]
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    # Skip dublicate nums[r]
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s<0:                          # Need larger sum
                    l += 1
                else:                              # Need smaller sum
                    r -= 1
        return res
    
# ---------------------------
# Driver code for printing
# ---------------------------
nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
output = solution.threeSum(nums)

print("Input: ", nums)
print("3 Sum triplets: ")
for triplet in output:
    print(triplet)




