class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def recur(s):
            if s in memo:
                return memo[s]

            for word in wordDict:
                # 完全一致
                if s == word:
                    memo[s] = True
                    return memo[s]

                # 部分一致
                if s[0:len(word)] == word:
                    # wordを取り除いた文字列について判定
                    # Trueならその時点で終了. 追加の判定は不要
                    if recur(s[len(word):]):
                        memo[s] = True
                        return memo[s]
            memo[s] = False
            return memo[s]
        return recur(s)