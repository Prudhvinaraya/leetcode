class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()  # Remove the last character from the stack
            else:
                stack.append(char)  # Add the current character to the stack
        
        return ''.join(stack)