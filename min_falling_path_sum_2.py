class Solution:
  def minFallingPathSum(self, grid):
    n = len(grid)

    # dp[j] = the minimum path sum reaching row 0..i-1, ending at column j
    dp = grid[0][:]                  # Start with the first row ( base case )

    # Process each row one by one (starting from 2nd row)
    for i in range(1, n):

        # Find the smallest and second smallest values in dp, along with their columns
        # min1 = (value, col) of the smallest
        # min2 = (value, col) of the second smallest
        min1, min2 = sorted([(v, j) for j, v in enumerate(dp)])[:2]

        new_dp = [0]*n

        # Prepare a new dp array for the current row
        for j in range(n):
            if j == min1[1]:
                new_dp[j] = grid[i][j] + min2[0]
            else:
                new_dp[j] = grid[i][j] + min1[0]
            
        # Update dp to be the new row results
        dp = new_dp

    return min(dp)
