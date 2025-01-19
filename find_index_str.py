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
        # print(len(haystack))
        if len(haystack) < len(needle):
            return -1
        indice = 0
        contador = 0
        for indiceCadenaHay in range(len(haystack)):
            if (haystack[indiceCadenaHay] == needle[0]):
                indiceAuxiliarPrincipal = indiceCadenaHay + 1
                indice = indiceCadenaHay
                contador +=1
                # print("Ingreso a un nuevo ciclo secundario------------------")
                for indiceSubCa in range(1,len(needle)):
                    # print(indiceAuxiliarPrincipal,indiceSubCa)
                    if indiceAuxiliarPrincipal >= len(haystack):
                        break
                    if needle[indiceSubCa] == haystack[indiceAuxiliarPrincipal]:
                        contador += 1
                        indiceAuxiliarPrincipal += 1
                if len(needle) == contador:
                    return indice
                else:
                    contador = 0
        
        return -1



haystack = "a"
needle = "a"
solucion = Solution()
print(solucion.strStr(haystack,needle))

haystack = "sadbutsad"
needle = "sad"
solucion = Solution()
print(solucion.strStr(haystack,needle))

haystack = "leetcode"
needle = "leeto"
solucion = Solution()
print(solucion.strStr(haystack,needle))


haystack = "mississippi"
needle = "issipi"
solucion = Solution()
print(solucion.strStr(haystack,needle))
haystack = "mississippi"
needle = "issip"
solucion = Solution()
print(solucion.strStr(haystack,needle))




