class Solution:
 def numberOfSubstrings(self, s: str) -> int:
    n = len(s)
    # Dictionary to track frequency of 'a', 'b', 'c' in the current sliding window
    count = {'a': 0, 'b': 0, 'c': 0}

    left = 0           # Left pointer of the sliding window
    ans = 0            # Final count of the substrings containing all three characters 

    # Expand the window by moving 'right' pointer one step at a time
    for right in range(n):
        count[s[right]] += 1          # Include the new character in the window

        # Check if the window currently contains at least one of each 'a', 'b', 'c'
        while all(count[c] > 0 for c in 'abc'):
              ans += n - right
              count[s[left]] -= 1
              left += 1

    return ans  