class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tab = {}
        for i in range(len(names)):
            tab[heights[i]] = names[i]
        heights.sort(reverse = True)
        ans = []
        for h in heights:
            ans.append(tab[h])
        return ans