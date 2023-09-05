class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in output_dict.keys():
                # make value List
                output_dict[key] = []
                output_dict[key].append(''.join(word))
            else:
                # append in the list
                output_dict[key].append(''.join(word))

        return (list(output_dict.values()))


# Feedback
'''
# Intuition

Two strings are anagrams if and only if their sorted strings are equal.

'''
