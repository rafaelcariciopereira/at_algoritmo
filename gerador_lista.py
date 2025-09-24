import random

tamanho = 100_000
lista = [random.randint(0, 100_000) for _ in range(tamanho)]

with open("lista_aleatoria.txt", "w") as arquivo:
    for numero in lista:
        arquivo.write(f"{numero}\n")