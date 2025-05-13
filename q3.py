
def merge_sort_v1(arr, inicio, fim):
    if inicio >= fim:
        return
    meio = (inicio + fim) // 2
    merge_sort_v1(arr, inicio, meio)
    merge_sort_v1(arr, meio + 1, fim)
    merge(arr, inicio, meio, fim)

def merge_sort_v2(arr, inicio, fim):
    if inicio >= fim:
        return
    meio = (inicio + fim - 1) // 2
    merge_sort_v2(arr, inicio, meio)
    merge_sort_v2(arr, meio + 1, fim)
    merge(arr, inicio, meio, fim)

def merge_sort_v3(arr, inicio, fim):
    if inicio >= fim:
        return
    meio = (inicio + fim + 1) // 2
    merge_sort_v3(arr, inicio, meio)
    merge_sort_v3(arr, meio + 1, fim)
    merge(arr, inicio, meio, fim)

def merge(arr, inicio, meio, fim):
    esq = arr[inicio:meio+1]
    dir = arr[meio+1:fim+1]
    i = j = 0
    k = inicio

    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            arr[k] = esq[i]
            i += 1
        else:
            arr[k] = dir[j]
            j += 1
        k += 1

    while i < len(esq):
        arr[k] = esq[i]
        i += 1
        k += 1

    while j < len(dir):
        arr[k] = dir[j]
        j += 1
        k += 1

print("=== Questão 3 ===")

vetor_original = [9, 3, 7, 1, 5, 8, 2, 4, 6]

v1 = vetor_original.copy()
merge_sort_v1(v1, 0, len(v1)-1)
print("Versão 1:", v1)

v2 = vetor_original.copy()
merge_sort_v2(v2, 0, len(v2)-1)
print("Versão 2:", v2)

v3 = vetor_original.copy()
try:
    merge_sort_v3(v3, 0, len(v3)-1)
    print("Versão 3:", v3)
except RecursionError:
    print("Versão 3: ERRO")

# a) Houve diferença nos resultados?
# Sim, a versão 3 causou erro de recursão.

# b) O algoritmo ainda funciona corretamente?
# Sim, nas versões 1 e 2. A versão 3 não funciona como está.

# c) Alguma das variações provoca falhas? Justifique.
# Sim, a variação (inicio + fim + 1) // 2 pode gerar recursão infinita porque não atinge o caso base corretamente.
