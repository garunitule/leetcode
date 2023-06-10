class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_map = {v: v for v in nums2}
        ans_map = {}
        for num1 in nums1:
            if num1 in nums2_map and num1 not in ans_map:
                ans_map[num1] = num1
        return ans_map.values()