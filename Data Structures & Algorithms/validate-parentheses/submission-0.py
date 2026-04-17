class Solution:
    def isValid(self, s: str) -> bool:
        
        # Create an empty stack to store opening brackets
        stack = []
        
        # Dictionary to map closing bracket to its matching opening bracket
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # Loop through each character in the string
        for c in s:
            
            # If the character is a closing bracket
            if c in closeToOpen:
                
                # Check if stack is not empty AND
                # top of stack matches the expected opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    
                    # If match, remove the opening bracket from stack
                    stack.pop()
                
                else:
                    # If stack is empty OR brackets do not match
                    return False
            
            else:
                # If it is an opening bracket, push into stack
                stack.append(c)

        # After processing all characters:
        # If stack is empty → all brackets matched correctly
        # If not empty → some opening brackets were not closed
        return True if not stack else False
