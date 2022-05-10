class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        aggregate = set()
        
        for element in nums:
            if element in aggregate:
                return True
            aggregate.add(element)
        return False
    