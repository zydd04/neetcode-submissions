class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            anagrams[key].append(i)
        
        return [[strs[idx] for idx in group] for group in anagrams.values()]