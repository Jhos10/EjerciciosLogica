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
      contadorDeSignosConsecutivos = 0
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
      
      valorMitad = len(s)//2
      signosApertura,signosCierr = ['[','{','('],[']',')','}']
      contador = 0
      listaSepararSeguidos = []
      cadenaAuxiliar = ""
      verificar = False
      if len(s) % 2 != 0 or len(s) == 0:
        return False
      elif s[0] in signosCierr or s[len(s)-1] not in signosCierr:
        return False
      
      for signo in s:
        diccionarioContador[signo] += 1

      for clave in diccionarioContador:
        if diccionarioContador[clave] != diccionarioContador[diccionarioSignos[clave]]:
          return False

      loop = True
      cadenaAuxiliar = s
      contador = 0
      contadorVecesWhile = 0
      while loop:
        cadena = ""
        contadorVecesWhile += 1
        verificar = False
        for indice in range(len(cadenaAuxiliar)):
          auxiliar = diccionarioSignos[cadenaAuxiliar[indice]]
          if cadenaAuxiliar[indice] in signosApertura:
            signosCierr.remove(diccionarioSignos[cadenaAuxiliar[indice]])
          if indice == len(cadenaAuxiliar)-1:
            if cadena == "":
              break
            elif len(cadenaAuxiliar) >= 1 and verificar != True:
              cadena += cadenaAuxiliar[indice]
              break
          elif verificar == True:
            verificar = False
            continue
          elif cadenaAuxiliar[indice+1] == diccionarioSignos[cadenaAuxiliar[indice]] and cadenaAuxiliar[indice] in signosApertura:
            contador += 1
            listaSepararSeguidos.append((cadenaAuxiliar[indice],cadenaAuxiliar[indice+1]))
            verificar = True
          elif (cadenaAuxiliar[indice+1] in signosCierr) and (cadenaAuxiliar[indice] not in signosCierr) and (cadenaAuxiliar[indice] != diccionarioSignos[cadenaAuxiliar[indice+1]]):
            return False
          else:
            cadena += cadenaAuxiliar[indice]
            verificar = False
          if auxiliar not in signosApertura:
            signosCierr.append(auxiliar)
        cadenaAuxiliar = cadena

        if cadenaAuxiliar == "":
          loop = False
        
      if contador == len(s)//2:
        return True
      else:
        print("Ultimo else")
        return False
          
            

solucion = Solution()
s = "()"
print(solucion.isValid(s))
s = "()[]{}"
print(solucion.isValid(s))
s = "(]"
# s = "([)]"
print(solucion.isValid(s))
s = "([])"
print(solucion.isValid(s))

s = "[()](())"
print(solucion.isValid(s))