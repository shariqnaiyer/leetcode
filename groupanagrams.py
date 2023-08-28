class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anag = {}
        for i in range(len(strs)):
            a = "".join(sorted(strs[i]))
            if a not in anag.keys():
                anag[a] = [strs[i]]
            else:
                anag[a].append(strs[i])
        return anag.values()