

class Solution:
  def partitionString(self, s: str) -> int:

    if not s:
        return 0
    
    seen = set()
    count = 1

    for ch in s:
        if ch in seen:
            count += 1
            seen.clear()
        seen.add(ch)

    return count