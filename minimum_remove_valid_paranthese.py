
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack =[]                                 # stack will store the indices of '(' encountered and not yet matched
        to_remove = set()                         # indices of characters to remove (unmatched')' or leftover '(')

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)                   # record index of '('
            elif ch == ')':
                if stack:
                    stack.pop()                   # match this ')' with the last unmatched '('
                else:
                    to_remove.add(i)              # no '(' available to match -> this ')' must be removed 

        to_remove.update(stack)                   # any '(' indices left in the stack are unmatched -> remove then

        # Rebuild the string skipping characters at indices in to_remove
        return ''.join(ch for i, ch in enumerate(s) if i not in to_remove)
 