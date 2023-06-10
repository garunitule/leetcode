class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        # まず昇順に並んだ部分文字列に分割する
        while r - l > 1 and nums[l] > nums[r]:
            mid = (l + r) // 2 + (l + r) % 2
            if nums[l] < nums[mid]:
                l = mid
            else:
                r = mid
    
        
        # どちらかの部分配列にtargetが入るか確かめれば、探索は1回で終了する
        # 定数倍の改善なので今回はやってない
        # leftについて探索
        i = bisect.bisect_left(nums, target, lo=0, hi=r)
        if 0 <= i and i < len(nums) and target == nums[i]:
            return i
        
        # rightについて探索
        i = bisect.bisect_left(nums, target, lo=r)
        if 0 <= i and i < len(nums) and target == nums[i]:
            return i
        
        return -1