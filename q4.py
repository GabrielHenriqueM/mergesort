
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def merge_sort_lista(head):
    if not head or not head.proximo:
        return head

    def dividir(meio):
        slow = meio
        fast = meio.proximo
        while fast and fast.proximo:
            slow = slow.proximo
            fast = fast.proximo.proximo
        meio2 = slow.proximo
        slow.proximo = None
        return meio, meio2

    def intercalar(l1, l2):
        dummy = No(0)
        atual = dummy
        while l1 and l2:
            if l1.valor < l2.valor:
                atual.proximo = l1
                l1 = l1.proximo
            else:
                atual.proximo = l2
                l2 = l2.proximo
            atual = atual.proximo
        atual.proximo = l1 or l2
        return dummy.proximo

    meio1, meio2 = dividir(head)
    return intercalar(merge_sort_lista(meio1), merge_sort_lista(meio2))

def print_lista(no):
    while no:
        print(no.valor, end=" -> ")
        no = no.proximo
    print("None")

print("=== Questão 4 ===")
inicio = No(7)
inicio.proximo = No(3)
inicio.proximo.proximo = No(5)
inicio.proximo.proximo.proximo = No(1)
inicio.proximo.proximo.proximo.proximo = No(4)

ordenado = merge_sort_lista(inicio)
print_lista(ordenado)

