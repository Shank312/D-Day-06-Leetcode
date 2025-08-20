
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []                  # an empty list used as a stack
        for ch in s:                # process input left to right
            if ch == '*':           # if current char is a star
                stack.pop()         # remove the top element of the stack
            else:
                stack.append(ch)    # otherwise push char onto the stack
        return ''.join(stack)       # return the characters left in the stack as a string