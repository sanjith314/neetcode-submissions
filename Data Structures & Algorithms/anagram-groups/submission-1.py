class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table ={}
        for word in strs:
            key = "".join(sorted(word))
            if key not in table:
                table[key] = []
            table[key].append(word)
        return list(table.values())
