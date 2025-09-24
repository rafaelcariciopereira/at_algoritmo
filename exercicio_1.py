import time
import matplotlib.pyplot as plt

numeros = []
with open("lista_aleatoria.txt", "r") as arquivo:
    for linha in arquivo:
        numero = int(linha.strip())
        numeros.append(numero)


def selection_sort(lista):
    tempo_inicio = time.time()
    n = len(lista)
    i = 0

    while i < n - 1:
        menor_valor = min(lista[i:])  
        menor_index = lista.index(menor_valor, i)  

        if menor_index != i:
            lista[i], lista[menor_index] = lista[menor_index], lista[i]

        i += 1

    tempo_final = time.time()
    return {"lista": lista, "tempo_execucao": tempo_final - tempo_inicio}


def insertion_sort(lista):
    tempo_inicio = time.time()
    
    for i in range(1, len(lista)):
        valor_atual = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j] > valor_atual:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = valor_atual
    
    tempo_final = time.time()
    return {"lista": lista, "tempo_execucao": tempo_final - tempo_inicio}


def bubble_sort(lista):
    tempo_inicio = time.time()
    n = len(lista)
    
    for fim in range(n - 1, 0, -1):
        for i in range(fim):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    
    tempo_final = time.time()
    return {"lista": lista, "tempo_execucao": tempo_final - tempo_inicio}


def merge_sort(lista):
    def merge_inplace(lista, inicio, meio, fim):
        esquerda = lista[inicio:meio+1]
        direita = lista[meio+1:fim+1]

        i = j = 0
        k = inicio

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

    def merge_sort_aux(lista, inicio, fim):
        if inicio < fim:
            meio = (inicio + fim) // 2
            merge_sort_aux(lista, inicio, meio)
            merge_sort_aux(lista, meio + 1, fim)
            merge_inplace(lista, inicio, meio, fim)

    tempo_inicio = time.time()
    merge_sort_aux(lista, 0, len(lista) - 1)
    tempo_final = time.time()

    return {"lista": lista, "tempo_execucao": tempo_final - tempo_inicio}


def quick_sort(lista):
    def particiona(lista, inicio, fim):
        pivo = lista[fim]
        i = inicio - 1
        for j in range(inicio, fim):
            if lista[j] <= pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        return i + 1

    def quick_sort_aux(lista, inicio, fim):
        if inicio < fim:
            indice_pivo = particiona(lista, inicio, fim)
            quick_sort_aux(lista, inicio, indice_pivo - 1)
            quick_sort_aux(lista, indice_pivo + 1, fim)

    tempo_inicio = time.time()
    quick_sort_aux(lista, 0, len(lista) - 1)
    tempo_final = time.time()

    return {"lista": lista, "tempo_execucao": tempo_final - tempo_inicio}

def calculador_tempo_execucao(funcao_sort, lista):
    inicio_tempo = time.time()
    lista_ordenada = funcao_sort(lista)
    final_tempo = time.time()
    return {"lista":lista_ordenada, "tempo_execucao": final_tempo - inicio_tempo }
def mostrar_resultados(nome_algoritmo, resultados, tamanhos):
    print(f"----- {nome_algoritmo} -----")
    for i, tempo in enumerate(resultados):
        print(f"Tamanho {tamanhos[i]:>6}: {tempo['tempo_execucao']:.6f} segundos")
    print("----------------------------\n")


tamanhos = [100, 500, 1000, 5000, 10000, 50000, 100000]

lista_testes_selection_sort = [selection_sort(numeros[:t]) for t in tamanhos]
mostrar_resultados("SELECTION SORT", lista_testes_selection_sort, tamanhos)

lista_testes_insertion_sort = [insertion_sort(numeros[:t]) for t in tamanhos]
mostrar_resultados("INSERTION SORT", lista_testes_insertion_sort, tamanhos)

lista_testes_bubble_sort = [bubble_sort(numeros[:t]) for t in tamanhos]
mostrar_resultados("BUBBLE SORT", lista_testes_bubble_sort, tamanhos)

lista_testes_merge_sort = [calculador_tempo_execucao(merge_sort, numeros[:t]) for t in tamanhos]
mostrar_resultados("MERGE SORT", lista_testes_merge_sort, tamanhos)

lista_testes_quick_sort = [calculador_tempo_execucao(quick_sort, numeros[:t]) for t in tamanhos]
mostrar_resultados("QUICK SORT", lista_testes_quick_sort, tamanhos)

tamanhos = [len(item["lista"]) for item in lista_testes_selection_sort]

tempos_selection = [item["tempo_execucao"] for item in lista_testes_selection_sort]
tempos_insertion = [item["tempo_execucao"] for item in lista_testes_insertion_sort]
tempos_bubble    = [item["tempo_execucao"] for item in lista_testes_bubble_sort]
tempos_merge     = [item["tempo_execucao"] for item in lista_testes_merge_sort]
tempos_quick     = [item["tempo_execucao"] for item in lista_testes_quick_sort]

plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempos_selection, marker='o', linestyle='-', label='Selection Sort')
plt.plot(tamanhos, tempos_insertion, marker='s', linestyle='-', label='Insertion Sort')
plt.plot(tamanhos, tempos_bubble, marker='^', linestyle='-', label='Bubble Sort')
plt.plot(tamanhos, tempos_merge, marker='D', linestyle='-', label='Merge Sort')
plt.plot(tamanhos, tempos_quick, marker='x', linestyle='-', label='Quick Sort')

plt.xlabel('Tamanho da Lista (n)', fontsize=12)
plt.ylabel('Tempo de Execução (segundos)', fontsize=12)
plt.title('Comparação de Algoritmos de Ordenação', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()