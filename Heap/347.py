class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_nums = {key: 0 for key in nums}
        for num in nums:
            freq_nums[num] += 1
        
        freq_values = list(freq_nums.values())
        freq_values.sort(reverse=True)

        freq_threshold = freq_values[k-1]

        ans = []
        for num in nums:
            if freq_nums[num] >= freq_threshold:
                ans.append(num)
                # 2回目以降はカウントしたくないので
                freq_nums[num] = -1
        return ans

# ヒープで解いた場合
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_nums = {key: 0 for key in nums}
        for num in nums:
            freq_nums[num] += 1
        
        # freq_threshold求める部分をヒープで求めるようにする
        freq_values = list(freq_nums.values())
        import heapq
        heapq.heapify(freq_values)
        freq_threshold = heapq.nlargest(k, freq_values)
        freq_threshold = freq_threshold[-1]

        ans = []
        for num in nums:
            if freq_nums[num] >= freq_threshold:
                ans.append(num)
                # 2回目以降はカウントしたくないので
                freq_nums[num] = -1
        return ans
    
# 実装が綺麗な解き方
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        # (-頻度, 値)
        c=[(-v, k) for k,v in c.items()]
        # -頻度の最小ヒープ（頻度の最大ヒープ）を作る
        heapq.heapify(c)
        output=[]
        for i in range(k):
            item=heapq.heappop(c)
            output.append(item[1])
        return output