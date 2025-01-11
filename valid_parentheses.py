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
      signosApertura,signosCierr = ['[','{','('],[']',')','}']
      contador = 0
      if len(s) % 2 != 0:
        # print("Ingreso en el primer if")
        return False
      elif s[0] not in signosApertura:
        # print("Ingreso en el primer elif")
        return False
      elif s[len(s)-1] in signosApertura:
        # print("Ingreso en el segundo elif")
        return False
      else:
        for indicePrincipal in range(len(s)):
          diccionarioContador[s[indicePrincipal]] += 1
          variableAuxiliar = str()
          contador +=1
          for indiceExpresion in range(contador,len(s)):
            variableAuxiliar = diccionarioSignos[s[indicePrincipal]]
            signosCierr = list(filter(lambda x: True if x != diccionarioSignos[s[indicePrincipal]] else False, signosCierr))
            # print("-----------------------------------------------------------------------------------------------")
            # print(f'El signo es: {signo} y deja la lista de signos de cierre de la siguiente manera {signosCierr}')
            if indicePrincipal == len(s)-1:
              break
            elif indiceExpresion == contador and s[indiceExpresion] in signosCierr and s[indicePrincipal] not in signosCierr:
              # print(contador,indiceExpresion)
              # print(f"Ingreso en el if con el signo secundario de {s[indiceExpresion]} y el signo del ciclo principal es {signo}")
              return False
            elif s[indiceExpresion] == diccionarioSignos[s[indicePrincipal]]:
              # print("Hola")
              if variableAuxiliar not in signosApertura:
                signosCierr.append(variableAuxiliar)
              # contadorDeSignosConsecutivos += 1
              break
            if variableAuxiliar not in signosApertura:
              signosCierr.append(variableAuxiliar)

      for clave in diccionarioContador:
        if diccionarioContador[clave] != diccionarioContador[diccionarioSignos[clave]]:
          return False


      mitadArregloNum = len(s)//2
      convertirExpresionLista = list(s)
      # print(signosCierr)
      listaParaZipCierre = list(filter(lambda x: True if x in signosCierr else False,convertirExpresionLista))
      listaParaZipApertura = list(filter(lambda x: True if x in signosApertura else False,convertirExpresionLista))
      listaCombinada = list(zip(listaParaZipApertura,listaParaZipCierre))
      # print(listaCombinada)
      for tupla in  listaCombinada:
        if diccionarioSignos[tupla[0]] == tupla[1]:
          contadorDeSignosConsecutivos += 1

      if contadorDeSignosConsecutivos == len(listaCombinada):
        return True
      
      listaComprobanteApertura = []
      listaComprobanteCierre = []
      for indiceExpresion in range(len(s)):
        if indiceExpresion <= mitadArregloNum-1:
          listaComprobanteApertura.append(s[indiceExpresion])
        else:
          listaComprobanteCierre.append(s[indiceExpresion])

      listaComprobanteCierre.reverse()
      for indiceComprobante in range(len(listaComprobanteApertura)):
        if listaComprobanteCierre[indiceComprobante] != diccionarioSignos[listaComprobanteApertura[indiceComprobante]]:
          return False
      return True
          
            

solucion = Solution()
s = "()"
# print(solucion.isValid(s))
s = "()[]{}"
# print(solucion.isValid(s))
s = "(]"
# s = "([)]"
# print(solucion.isValid(s))
s = "([])"
# print(solucion.isValid(s))

# s = "[([]])"
# s = "{([])}"
# s ="[)(]"
s = "(([]){})"
print(solucion.isValid(s))


# numeroMitadExpresion = len(s)//2
# print(numeroMitadExpresion)
# listaSignoCierre = []
# listaSignoApertura = []
# for indice in range(len(s)):
#   if indice <= numeroMitadExpresion-1:
#     listaSignoApertura.append(s[indice])
#   else:
#     listaSignoCierre.append(s[indice])
# print(s)
# print(listaSignoApertura)
# print(listaSignoCierre)
# for indicePrincipal in range(0,len(s)):
#   print(indicePrincipal,s[indicePrincipal])
#   print("-----------------------------------")
#   for indiceSegundario in range(len(s)-1,-1,-1):
#   # print(signo)
#     print(indiceSegundario,s[indiceSegundario])
#     # if 