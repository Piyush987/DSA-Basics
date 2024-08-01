class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")" : "(", "}" : "{", "]" : "["} # Creating a hashmap with only closing brackets mapped to starting brackets
        stack = []
        for i in s:
            if i not in Map:   # Appending only starting brackets to stack
                stack.append(i)
                continue
            if not stack or stack[-1] != Map[i]:   # Check top of stack is in order with closing bracket
                return False
            stack.pop()        # We need empty stack if all brackets are closed
        return not stack     # Return not of stack -  empty or not
