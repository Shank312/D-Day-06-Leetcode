
class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Initialize two pointers: left (l) at start, right (r) at end
        l, r = 0, len(height) - 1

        # Variable to store maximum area found so far
        best = 0

        # Step count for printing progress
        step = 1

        # Loop until the two pointers meet
        while l<r:
            # Calculate the current area:
            # Width = distance between two pointers (r-l)
            # Height = min(height[l], height[r]) because water can't go higher than the shorter line
            area = min(height[l], height[r])*(r-l)

            # Update the maximum area if the current one is bigger
            best = max(best, area)

            # Print current state for debugging or tracing
            print(
                f"Step {step}: "
                f"l={l}, r={r}"
                f"height[l]={height[l]}, height[r]={height[r]}, "
                f"area={area}, best={best}"
            )

            step += 1               # Increment step counter

            # Move the pointer that points to the sorter line:
            # This is the greedy trick: moving the taller height won't help,
            # since width decreases and height can't increase beyond the shorter one

            if height[l]<height[r]:
                l += 1                # Move left pointer rightward
            else:
                r -= 1                # Move right pointer leftward

        # After the loop, return the maximum area found 
        return best
    
# Example Run
sol = Solution()
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Max Area: ", sol.maxArea(heights))



# Uploaded code

class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        l, r = 0, len(height) - 1

       
        best = 0

       
        step = 1

        
        while l<r:
            
            area = min(height[l], height[r])*(r-l)

           
            best = max(best, area)

           
           

            step += 1               

            if height[l]<height[r]:
                l += 1                
            else:
                r -= 1               

        
        return best