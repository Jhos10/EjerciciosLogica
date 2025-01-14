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
        iteradorDos = rutaAuxiliar
        while iteradorListaUno != None and iteradorListaDos != None:


# Nodos de la primera lista
primerNodoPrimeraLista = ListNode(1)
segundoNodoPrimeraLista = ListNode(2)
tercerNodoPrimeraLista = ListNode(4)
primerNodoPrimeraLista.next = segundoNodoPrimeraLista
segundoNodoPrimeraLista = tercerNodoPrimeraLista

# Nodos de la segunda lista
primerNodoSegundaLista = ListNode(1)
segundoNodoSegundaLista = ListNode(3)
tercerNodoSegundaLista = ListNode(4)
primerNodoSegundaLista.next = segundoNodoSegundaLista
segundoNodoSegundaLista.next = tercerNodoSegundaLista




