import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    return merge_crescente(esquerda, direita)

def merge_crescente(esq, dir):
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

def esta_ordenado(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

print("=== Questão 2: Testes experimentais ===")

tamanhos = [10, 100, 1000]

for tam in tamanhos:
    vetor = [random.randint(0, 10000) for _ in range(tam)]
    ordenado = merge_sort(vetor)
    if esta_ordenado(ordenado):
        print(f"Vetor de tamanho {tam}: OK ")
    else:
        print(f"Vetor de tamanho {tam}: FALHOU ")
