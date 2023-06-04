class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return nums[0]

        while r - l > 1:
            mid = (l + r) // 2 + ((l + r) % 2)
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        return nums[r]