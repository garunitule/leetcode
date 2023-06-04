class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        sums = []
        for num1 in nums1:
            for num2 in nums2:
                sums.append((num1 + num2, num1, num2))
        
        import heapq
        heapq.heapify(sums)
        ans = []
        for i in range(k):
            if len(sums) < 1:
                break
            item = heapq.heappop(sums)
            ans.append((item[1], item[2]))
        return ans

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq
        hq = []
        heapq.heapify(hq)

        # 一旦nums2[0]に対しての和を全部作る
        for i in range(min(len(nums1), k1)):
            heapq.heappush(hq, (nums[i]+nums2[0], nums1[i], nums2[0], 0))
        
        out = []
        while k > 0 and hq:
            _, n1, n2, idx = heapq.heappop(hq)
            out.append((n1, n2))
            # 肝がこの部分
            # n1+nums2[idx+1]を参考にヒープ則が保たれる
            # もし、n1+nums2[idx+1]が最小ならば、次のloopで取り出される
            # →自分がnum1, num2の増分の小さい方のインデックスを増やそうとしてた操作に対応する
            # 
            # 最小ヒープは先頭の要素に最小が入ることを利用した解法
            # 常に和が最小な値の組み合わせが先頭に来る
            # nums1とnums2の全ての組み合わせを追加する必要はない
            # nums1, nums2はどちらも昇順に並べられてるので
            # 現在のi, jに対して、i,j, i+1,j, i,j+1の三つがあれば良いはず
            # 多分遷移則が複雑になるから、numsに関しては全て計算してると思ってる
            # i, jそれぞれ超えないように気をつけるのが面倒だからかな
            if idx + 1 < len(nums2):
                heapq.heappush(hq, n1+nums2[idx+1], n1, nums2[idx+1])
            k -= 1
        return out
