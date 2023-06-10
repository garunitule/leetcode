class Solution:
    def firstUniqChar(self, s: str) -> int:
        # key: 文字, value: 登場回数
        countMap = collections.defaultdict(int)
        for c in s:
            countMap[c] += 1
        
        for i, c in enumerate(s):
            if countMap[c] == 1:
                return i
        return -1
