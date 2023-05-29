class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapify(self.nums)
        # 値の昇順に並べた時、k番目以上の要素のみ残す
        while len(self.nums) > self.k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        # 与えられたnumsの長さよりもkの方が大きい場合、ヒープに追加
        if len(self.nums) < self.k:
            heappush(self.nums, val) # O(log(len(self.nums)))
        # 長さkがある(つまりk番目が定義できる)、かつ、最小値よりもvalが大きい場合
        # このヒープはk番目より大きい値を保持しなくて良いので、最小値をpopして、valをヒープに入れる
        elif val > self.nums[0]:
            heapreplace(self.nums, val) # O(log(len(self.nums)))
        
        # 長さkがあって、最小値よりもvalが小さいか等しい場合は、init時に捨てた部分にvalが入る(k-1番目以前の要素)ので、何もしなくてok

        return self.nums[0] # O(1)
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)