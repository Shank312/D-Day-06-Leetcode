
class Solution:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        n = len(temps)                          # total number of days 
        res = [0]*n                             # answer array, initially all 0
        stack = []                              # stack to keep indices (not tempratures)

        for i, t in enumerate(temps):           # go through each day with index and temp
            # check if the current temprature is greater than the temprature
            # at the stack stored at the top of the stack
            while stack and temps[stack[-1]] < t:
                j = stack.pop()                 # get the index from stack
                res[j] = i - j                  # differences in the days untill warmer temprature
            stack.append(i)                     # push current index onto stack

        return res
    
# --------- Driver code for printing output ----------------
temps = [73, 74, 75, 71, 69, 72, 76, 73]
sol = Solution()
result = sol.dailyTemperatures(temps)

print("Input Temperatures: ", temps)
print("Days untill warmer temperature: ", result)
