
class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []               # Stack stores the indices of the bars (monotonic decreasing)
        water = 0                # Total trapped water

        # Iterates over each baar 
        for i, h in enumerate(height):
            print(f"\nCurrent index = {i}, height={h}, Stack={stack}")

            # While the current bar is taller than the bar at the stack top
            while stack and h > height[stack[-1]]:
                top = stack.pop()                   # Pop the valley bottom
                print(f" Popped index={top}, height= {height[top]}")

                if not stack:
                    # No left wall exists, so break
                    print("Stack empty -> No left wall, break")
                    break

                # Distance between current bar (right wall) and new stack top (left wall)
                distance = i - stack[-1] -1

                # Bounded height = min(left wall, right wall) - bottom height
                bounded_h = min(h, height[stack[-1]]) - height[top]

                trapped = distance*bounded_h
                water += trapped

                print(f" Left wall index={stack[-1]}, height={height[stack[-1]]}")
                print(f" Right wall index={i}, height={h}")
                print(f" Distance={distance}, Bounded Height={bounded_h}, Water Trapped={trapped}")

            # Push current index into stack
            stack.append(i)
            print(f" Pushed index={i}, -> Stack={stack}")

        print(f"\nTotal Trapped Water = {water}")
        return water
    
sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))