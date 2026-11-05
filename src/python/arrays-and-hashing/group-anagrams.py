# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
import functools
from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        return Solution.counting_implv1(strs)

    @staticmethod
    def best_solution(strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            hashmap["".join(sorted(string))].append(string)
        return list(hashmap.values())

    
    @staticmethod
    def sorting_impl(strs: list[str]) -> list[list[str]]:
        # we are going to sort each string and use a dictionary and then flatten it into a list
        hashmap: dict[str, list[str]] = {}
        for string in strs:
            key = "".join(sorted(string))
            if key not in hashmap:
                hashmap[key] = [string]
            else:
                hashmap[key].append(string)

        return list(hashmap.values())

    @staticmethod
    def counting_implv1(strs: list[str]) -> list[list[str]]:
        # we are going to use Counter() as the key
        hashmap: dict[frozenset, list[str]] = {}
        for string in strs:
            key = frozenset(Counter(string).items())
            if key not in hashmap:
                hashmap[key] = [string]
            else:
                hashmap[key].append(string)

        return list(hashmap.values())

    @staticmethod
    def counting_implv2(strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            key = tuple(sorted(Counter(string).items()))
            hashmap[key].append(string)
        return list(hashmap.values())

if __name__ == "__main__":
    sol = Solution()
    Solution.sorting_impl([])
