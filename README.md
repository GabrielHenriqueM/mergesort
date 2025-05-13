# Merge Sort – Estrutura de Dados II

Este repositório contém a resolução das **questões propostas pelo professor Júnio Moreira** na disciplina de **Estrutura de Dados II**, do curso de Análise e Desenvolvimento de Sistemas – IFTM Campus Patrocínio.

---

## ✅ Questões Resolvidas

### 🔹 Questão 1
> Escreva uma versão recursiva do algoritmo Merge Sort que ordene um vetor `v[inicio..fim]` em **ordem decrescente**.  
> Sua função deve conter o código da intercalação, considerando que os subvetores `v[inicio..meio]` e `v[meio+1..fim]` já estejam ordenados de forma decrescente.

📁 Arquivo: `q1.py`

---

### 🔹 Questão 2
> Implemente um programa que utilize a função `merge_sort(array)` e realize **testes experimentais** para verificar sua correção.  
> Gere vetores de inteiros aleatórios de vários tamanhos (por exemplo, 10, 100, 1000 elementos).  
> Após a ordenação, verifique automaticamente se o vetor está em ordem crescente. Exiba o resultado de cada teste.

📁 Arquivo: `q2.py`

---

### 🔹 Questão 3
> No código do Merge Sort, o meio é calculado como: `meio = (inicio + fim) // 2`.  
> Refaça a implementação utilizando:
> - `(inicio + fim - 1) // 2`
> - `(inicio + fim + 1) // 2`  
>
> E responda:
> a) Houve diferença nos resultados?  
> b) O algoritmo ainda funciona corretamente?  
> c) Alguma das variações provoca falhas? Justifique.

📁 Arquivo: `q3.py`  
📝 Respostas no final do arquivo como comentário.

---

### 🔹 Questão 4
> Implemente o algoritmo Merge Sort para **listas encadeadas simples**.  
> A função deve ordenar a lista em ordem crescente **sem alocar novas células**, apenas manipulando os ponteiros existentes.

📁 Arquivo: `q4.py`

---

### 🔹 Questão 5
> Utilize a versão **iterativa** do Merge Sort e **compare-a com a versão recursiva**.  
> Faça testes com vetores de tamanhos variados, **meça o tempo de execução** de ambas as versões e apresente os resultados.

📁 Arquivo: `q5.py`  
📝 Comparações e conclusão no final do arquivo como comentário.

---

## 🛠 Linguagem Utilizada
- **Python 3.x**

---

## 👨‍🏫 Professor
- Júnio Moreira

## 🎓 Curso
- Tecnologia em Análise e Desenvolvimento de Sistemas – 4º Período  
- Instituto Federal do Triângulo Mineiro – Campus Patrocínio
