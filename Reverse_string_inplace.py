class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse() # in-place 

        # reversed_list = s[::-1]  #creates new list

        # s = [s[i] for i in range(len(s)-1, -1, -1)] #creates new list

#and the question is all about inplace reversing ..that is why it is not working

# Other best in-place way is also below
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    """
