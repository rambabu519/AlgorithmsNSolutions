'''
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dt = {'(':')','{':'}','[':']'}
        
        # Taken another local storage to avoid iterating through keys  for each character in string
        dtk = dt.keys()
        
        for c in s:
            #If it is open paranthesis then PUSH to stack
            if c in dt.keys):
                stack.append(c)
            
            #If it is closed paranthesis then pop from stack and compare with current closed paranthesis
            elif stack:
                if dt[stack.pop()] != c:
                    return False
            # This case is when a single open closed paranthesis is present
            else:
                return False
        
        # if no characters remaining in string and still stack is not empty then given string is not valid 
        if stack:
            return False
        else:
            return True
