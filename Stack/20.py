class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        open_parentheses = ["(", "{", "["]
        corresponding_open_parentheses = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            # open括弧の場合
            if c in open_parentheses:
                opened.append(c)
            # close括弧の場合
            else:
                # open括弧がないのに閉じ括弧が来たらFalse
                if len(opened) == 0:
                    return False
                item = opened.pop()
                # 対応する括弧で閉じられなかったらFalse
                if item != corresponding_open_parentheses[c]:
                    return False
        
        # 閉じられたなかったらFalse
        return len(opened) == 0