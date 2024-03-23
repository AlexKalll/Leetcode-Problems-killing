class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos =0
        neg = 1
        ans =[3] * len(nums) 
        for x in nums:
            if x> 0:
                ans[pos] = x
                pos +=2
            else:
                ans[neg]= x
                neg += 2
        return ans
        #The reason why we initialize a list ans as equal lentgh as the given one nums is since it helps us to itrate over the list if we let it an empty list it will not iterate over
        #simply what we are doing is changing the elements of the list ans
