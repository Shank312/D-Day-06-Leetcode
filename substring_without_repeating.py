
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}             # stores last index of each character
        left = 0              # left pointer of the window
        best = 0              # result = max length found

        for i, ch in enumerate(s):
            # if char already seen inside current window -> move left pointer
            if ch in last and last[ch] >= left:
                left = last[ch] + 1

            # update last seen index of char
            last[ch] = i

            # update best length
            best = max(best, i - left + 1)

        return best
    
# Printable test runs 
sol = Solution()

# Test cases
a = sol.lengthOfLongestSubstring
print(a("abcabcbb"))                   # output = abc
print(a("bbbbb"))                      # output = b 
print(a("pwwkew"))                     # output = wke
print(a(""))                           # output = 
print(a("dvdf"))                       # output = vdf
