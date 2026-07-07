class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a default dictionary
        groups = defaultdict(list)

        # loop through the list of strings
        for str in strs:
            count = [0] * 26

            # loop through characters of string
            for char in str:
                count[ord(char) - ord('a')] += 1\
            
            # add the count list to the dictionary
            groups[tuple(count)].append(str)
        
        return list(groups.values())