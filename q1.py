def merge_sort_decrescente(arr):
    if len(arr) <= 1:
        return arr 

    meio = len(arr) // 2
    esquerda = merge_sort_decrescente(arr[:meio])
    direita = merge_sort_decrescente(arr[meio:])

    return merge_decrescente(esquerda, direita)

def merge_decrescente(esq, dir):
    resultado = []
    i = j = 0

    while i < len(esq) and j < len(dir):
        if esq[i] > dir[j]:  
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    resultado.extend(esq[i:]) 
    resultado.extend(dir[j:]) 
    return resultado

if __name__ == "__main__":
    print("=== Questão 1: Merge Sort Recursivo Decrescente ===")
    testes = [
        [3, 1, 4, 2],
        [10, 5, 8, 12, 3],
        [1],
        [],
        [5, 5, 5],
        [100, 90, 80, 70, 60]
    ]

    for idx, vetor in enumerate(testes):
        ordenado = merge_sort_decrescente(vetor.copy())
        print(f"Teste {idx+1}:")
        print(f"Original:  {vetor}")
        print(f"Ordenado:  {ordenado}\n")
