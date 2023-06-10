# 下記は他の人の解法
# 自分の理解を言語化して残すために示している
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # key-value pair of (0, 1), where 0 is the sum of the empty subarray and 1 is the frequency of the empty subarray
        d = {0: 1}
        count = 0 # initialize count of subarrays whose sum equals k to 0
        sum_so_far = 0 # initialize sum_so_far to 0
        
        for num in nums:
            sum_so_far += num # update the sum_so_far by adding num to it
            diff = sum_so_far - k # compute the difference between the sum_so_far and k
            
            # 和がdiffとなる部分配列が存在するということ
            # 今回の目的は和がkとなる部分配列数を求めること
            # 現在の累積和 - k が過去に存在したということは、
            # 和が現在の累積和となる部分配列と、和が(現在の累積和 - k)となる部分配列の間の部分配列の和はkとなるということ
            # つまり、和がkとなる部分配列が存在することになる
            # でもその場合、d[diff]で良いのか？
            # 多分、sum_so_farは累積和なので、先頭のいくつかの要素をうまく消してるんだろうが理解できてない
            # 
            # 自分は最初のdを作ってから、k += numとなるものが存在するかを調べていたけど、その方法だと毎回dからその時のnumを含むものを消す必要があったが、dictなのでそれができなかった
            # ↑うまく説明できてない
            if diff in d: # if diff is in the dictionary d, increment the count by the value of d[diff]
                count += d[diff]
            
            if sum_so_far in d: # if sum_so_far is in the dictionary d, increment its value by 1, otherwise add a new key-value pair to d
                d[sum_so_far] += 1
            else:
                d[sum_so_far] = 1
        
        return count # return the count of subarrays whose sum equals k