class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        n = len(nums)
        
        for i in range(n - 1):
            if max_reachable < i:
                return False
            
            max_reachable = max(max_reachable, i + nums[i])
            
        return max_reachable >= n - 1
