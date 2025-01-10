# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution:
    def isValid(self, s: str) -> bool:
      diccionarioSignos = {
         '[': ']',
         '(': ')',
         '{': '}',
         ']': '[',
         ')': '(',
         '}': '{'
      }
      diccionarioContador = {
        '[': 0,
        '(': 0,
        '{': 0,
        ']': 0,
        ')': 0,
        '}': 0
      }
      signosApertura,signosCierr = ['[','{','('],[']',')','}']
      contador = 0
      if len(s) % 2 != 0:
         return False
      elif s[0] not in signosApertura:
         return False
      elif s[len(s)-1] in signosApertura:
        return False
      else:
        for signo in s:
          variableAuxiliar = str()
          contador +=1
          for indiceExpresion in range(contador,len(s)):
            variableAuxiliar = diccionarioSignos[signo]
            signosCierr = list(filter(lambda x: True if x != diccionarioSignos[signo] else False, signosCierr))
            if indiceExpresion == contador and s[indiceExpresion] in signosCierr:
              return False
            elif s[indiceExpresion] == diccionarioSignos[signo]:
              break
            signosCierr.append(variableAuxiliar) 
      return True
            
            

solucion = Solution()
s = "()"
print(solucion.isValid(s))
s = "()[]{}"
print(solucion.isValid(s))
s = "(]"
print(solucion.isValid(s))
s = "([])"
print(solucion.isValid(s))