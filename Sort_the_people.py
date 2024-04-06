class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n):
            swapped = False
            for j in range(n-1-i):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]                   
                    names[j], names[j+1] = names[j+1], names[j]
                    swapped = True
            if not swapped:
                break
        return names

#The swapped condition is only used for time complexity minimization  if the elements has already are order correctly  i.e. it is a flag checker simply   

"""
I'm using a bubble sorting method 
rather the way below is also possible
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_names_heights = sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
    
        sorted_names = [name for name, _ in sorted_names_heights]
        
        return sorted_names
 """
