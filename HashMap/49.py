# メモリエラーが出る解法
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            chars = list(s)
            permutations = list(itertools.permutations(s))
            anagrams[s] = list(map(lambda x: "".join(x), permutations))
        
        # key: 文字列, value: アナグラム判定された文字列
        grouped_anagrams = {}
        for s in strs:
            if s in grouped_anagrams:
                grouped_anagrams[s].append(s)
            else:
                is_belong_to_group = False
                for group in grouped_anagrams:
                    if s in anagrams[group]:
                        grouped_anagrams[group].append(s)
                        is_belong_to_group = True
                        break
                
                # どのグループにも所属しなかった場合
                if not is_belong_to_group:
                    grouped_anagrams[s] = [s]
        
        return grouped_anagrams.values()


# メモリエラーが出ない解き方
# 無駄な順列生成をなくした
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in grouped_anagrams:
                grouped_anagrams[sorted_s].append(s)
            else:
                grouped_anagrams[sorted_s] = [s]
        return grouped_anagrams.values()

