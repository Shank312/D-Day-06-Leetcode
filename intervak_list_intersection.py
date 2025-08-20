
class Solution:
    def intervalIntersection(self, A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
        i = j = 0             # two pointers for A and B
        ans = []              # store intersections

        while i < len(A) and j < len(B):
            # Compute overlap boundaries
            start = max(A[i][0], B[j][0])    # later of the two starts
            end   = min(A[i][1], B[j][1])    # earlier of the two ends

            if start <= end:
                ans.append([start, end])     # valid overlap

            # Move the interval with smaller endpoint forward
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
