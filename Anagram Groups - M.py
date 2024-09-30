class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            ana[key].append(s)

        return list(ana.values())

        ## Above solution has TC = O(n*mlogm) where n is no of strings and m is max length of strings

        ## Below is more optimized solution with TC = O(n*m)

        ana = defaultdict(list)

        for s in strs:
            cnt = [0]*26
            for c in s:
                cnt[ord(c) - ord("a")] += 1  #This is to give count to letters like a is 0 b is 1 and so on
            ana[tuple(cnt)].append(s)

        return ana.values()
