class Solution:
    def minSwaps(self, s: str) -> int:
        #using stack 
        """stack = []
        unbalanced = 0
        for c in s:
            if c is '[':
                stack.append(c)
            else:
                if stack: # if stack is not empty
                    stack.pop()
                else:
                    unbalanced += 1

        return ((unbalanced + 1)//2)
        """
        # Iterative approach
        closing = maxclosing = ans = 0
        for c in s:
            if c is '[':
                closing -= 1
            else:
                closing += 1
            
            maxclosing = max(maxclosing, closing)
        
        return (maxclosing + 1) // 2
