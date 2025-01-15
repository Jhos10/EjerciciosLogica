from typing import Optional
# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        rutaAuxiliar = None
        iteradorListaUno = primerNodoPrimeraLista
        iteradorListaDos = primerNodoSegundaLista
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        while iteradorListaUno != None or iteradorListaDos != None:
            if iteradorListaUno == None and iteradorListaDos != None:
                iteradorDos.next = iteradorListaDos
                iteradorListaDos = iteradorListaDos.next
                iteradorDos = iteradorDos.next
            elif iteradorListaDos == None and iteradorListaUno != None:
                iteradorDos.next = iteradorListaUno
                iteradorListaUno = iteradorListaUno.next
                iteradorDos = iteradorDos.next
            elif  iteradorListaUno.val < iteradorListaDos.val:
                if rutaAuxiliar == None:
                    rutaAuxiliar = iteradorListaUno
                    iteradorDos = rutaAuxiliar
                    iteradorListaUno = iteradorListaUno.next
                elif rutaAuxiliar != None:
                    iteradorDos.next = iteradorListaUno
                    iteradorListaUno = iteradorListaUno.next
                    iteradorDos = iteradorDos.next
            elif iteradorListaDos.val < iteradorListaUno.val:
                if rutaAuxiliar == None:
                    rutaAuxiliar = iteradorListaDos
                    iteradorDos = rutaAuxiliar
                    iteradorListaDos = iteradorListaDos.next
                elif rutaAuxiliar != None:
                    iteradorDos.next = iteradorListaDos
                    iteradorListaDos = iteradorListaDos.next
                    iteradorDos = iteradorDos.next
            elif iteradorListaUno.val == iteradorListaDos.val:
                if rutaAuxiliar == None:
                    rutaAuxiliar = iteradorListaUno
                    iteradorDos = rutaAuxiliar
                    iteradorListaUno = iteradorListaUno.next
                    iteradorDos.next = iteradorListaDos
                    iteradorDos = iteradorDos.next
                    iteradorListaDos = iteradorListaDos.next
                elif rutaAuxiliar != None:
                    iteradorDos.next = iteradorListaUno
                    iteradorListaUno = iteradorListaUno.next
                    iteradorDos = iteradorDos.next
                    iteradorDos.next = iteradorListaDos
                    iteradorListaDos = iteradorListaDos.next
                    iteradorDos = iteradorDos.next
                    
        
        iteradorRutaAuxiliar = rutaAuxiliar
        listaNumeros = []
        while iteradorRutaAuxiliar != None:
            listaNumeros.append(iteradorRutaAuxiliar.val)
            iteradorRutaAuxiliar = iteradorRutaAuxiliar.next
        
        print(listaNumeros)

        return rutaAuxiliar



                        

# Nodos de la primera lista
# primerNodoPrimeraLista = ListNode(2)
# segundoNodoPrimeraLista = ListNode(2)
# tercerNodoPrimeraLista = ListNode(4)
primerNodoPrimeraLista = ListNode(-9)
segundoNodoPrimeraLista = ListNode(3)
# tercerNodoPrimeraLista = ListNode(4)
primerNodoPrimeraLista.next = segundoNodoPrimeraLista
# segundoNodoPrimeraLista.next = tercerNodoPrimeraLista

# Nodos de la segunda lista
# primerNodoSegundaLista = ListNode(1)
# segundoNodoSegundaLista = ListNode(3)
# tercerNodoSegundaLista = ListNode(4)
primerNodoSegundaLista = ListNode(5)
segundoNodoSegundaLista = ListNode(7)
# tercerNodoSegundaLista = ListNode(4)
primerNodoSegundaLista.next = segundoNodoSegundaLista
# segundoNodoSegundaLista.next = tercerNodoSegundaLista

solucion = Solution()
print(solucion.mergeTwoLists(primerNodoPrimeraLista,primerNodoSegundaLista))



