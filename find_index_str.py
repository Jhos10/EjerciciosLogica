# 27.Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        indice = 0
        contador = 0
        for indiceCadenaHay in range(len(haystack)):
            if contador == len(needle):
                return indice
            if haystack[indiceCadenaHay] == needle[contador] and contador == 0:
                print(haystack[indiceCadenaHay])
                contador += 1
                indice = indiceCadenaHay
            elif haystack[indiceCadenaHay] == needle[contador]:
                print(haystack[indiceCadenaHay])
                contador += 1
            else:
                contador = 0
                indice = 0
        if contador == len(needle):
            return indice
        else:
            return -1


# haystack = "a"
# needle = "a"
# solucion = Solution()
# print(solucion.strStr(haystack,needle))

haystack = "mississippi"
needle = "issip"
solucion = Solution()
print(solucion.strStr(haystack,needle))




