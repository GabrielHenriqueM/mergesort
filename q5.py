
import random
import time

def merge_sort_recursivo(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    esquerda = merge_sort_recursivo(arr[:meio])
    direita = merge_sort_recursivo(arr[meio:])
    return merge(esquerda, direita)

def merge_sort_iterativo(arr):
    step = 1
    n = len(arr)
    while step < n:
        for i in range(0, n, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            merged = merge(left, right)
            for j in range(len(merged)):
                if i + j < len(arr):
                    arr[i + j] = merged[j]
        step *= 2
    return arr

def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

print("=== Questão 5 ===")

tamanhos = [10, 100, 1000, 5000]
for tamanho in tamanhos:
    vetor1 = [random.randint(0, 10000) for _ in range(tamanho)]
    vetor2 = vetor1[:]

    inicio_r = time.time()
    merge_sort_recursivo(vetor1)
    tempo_r = time.time() - inicio_r

    inicio_i = time.time()
    merge_sort_iterativo(vetor2)
    tempo_i = time.time() - inicio_i

    print(f"Tamanho {tamanho}: Recursivo = {tempo_r:.6f}s | Iterativo = {tempo_i:.6f}s")

# A versão iterativa e a recursiva funcionam corretamente.
# A versão recursiva costuma ser mais intuitiva, mas pode consumir mais memória para listas grandes.
# A versão iterativa evita problemas de estouro de pilha e pode ser ligeiramente mais eficiente em grandes volumes.
