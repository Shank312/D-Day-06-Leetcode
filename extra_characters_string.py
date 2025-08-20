

class Solution:

 def minExtraChar(self, s: str, dictionary: list[str]) -> int:
    n = len(s)
    wordset = set(dictionary)           # convert dictionary to set for fast lookup
    dp = [0]*(n + 1)                    # dp[i] = min extra chars for prefix s[:i]

    for i in range(1, n + 1):
        # Case 1: assume s[i-1] is extra char
        dp[i] = dp[i-1] + 1

        # Case 2: check if some substring s[j:i] is a word in dictionary
        for j in range(i):
            if s[j:i] in wordset:
                # if s[j:i] is a word, we don't add extra chars for it
                dp[i] = min(dp[i], dp[j])

    return dp[n] 
