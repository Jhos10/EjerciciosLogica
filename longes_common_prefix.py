# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
      palabraConstruccion = ""
      contadorAuxiliar = 0
      cadenaAuxiliar = strs[0]
      if len(strs) == 0 and len(strs[0]) == 0:
        return ""
      for palabra in strs:
        contadorLetrasIguales = 0
        palabraSubConstruccion = ""
        if len(cadenaAuxiliar) >= len(palabra):
          for indice in range(len(palabra)):
            if cadenaAuxiliar[indice] == palabra[indice]:
              palabraSubConstruccion += palabra[indice]
              contadorLetrasIguales += 1
            else:
              break
          if contadorLetrasIguales != 0:
            contadorAuxiliar += 1
            cadenaAuxiliar = palabraSubConstruccion
        elif len(palabra) >= len(cadenaAuxiliar):
          for indice in range(len(cadenaAuxiliar)):
            if cadenaAuxiliar[indice] == palabra[indice]:
              palabraSubConstruccion += palabra[indice]
              contadorLetrasIguales += 1
            else:
              break
          if contadorLetrasIguales != 0:
            contadorAuxiliar += 1
            cadenaAuxiliar = palabraSubConstruccion
        palabraConstruccion = palabraSubConstruccion
      if contadorAuxiliar == len(strs):
        return palabraConstruccion
      else:
        return ""
      
      


solucion = Solution()
listaPalabras = ["flower","flow","flight"]
print(solucion.longestCommonPrefix(listaPalabras))
listaPalabras = ["dog","racecar","car"]
print(solucion.longestCommonPrefix(listaPalabras))
        
