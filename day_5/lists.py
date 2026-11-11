"""
Resumo - Python em 30 Dias
Dia 5: Listas (Lists)

Resumo do conteúdo teórico. Os exercícios do material original foram omitidos.
"""

# ============================================================
# 1. O que são listas?
# ============================================================

# Uma lista é uma coleção:
# - Ordenada: mantém a ordem dos elementos.
# - Mutável: permite adicionar, remover e alterar elementos.
# - Permite valores duplicados.
# - Pode armazenar diferentes tipos de dados.

frutas = ["banana", "laranja", "manga", "limão"]
dados_mistos = ["Nan", 30, True, {"cidade": "São Paulo"}]

# Existem duas formas comuns de criar uma lista vazia:
lista_vazia_1 = []
lista_vazia_2 = list()

# len() retorna a quantidade de elementos.
print(len(frutas))  # 4


# ============================================================
# 2. Acessando elementos: índices positivos
# ============================================================

# Os índices começam em zero:
# índice:    0          1         2        3
# valor:  banana    laranja    manga    limão

primeira_fruta = frutas[0]
segunda_fruta = frutas[1]
ultima_fruta = frutas[3]

# Para descobrir o índice do último elemento:
ultimo_indice = len(frutas) - 1
ultima_fruta = frutas[ultimo_indice]


# ============================================================
# 3. Acessando elementos: índices negativos
# ============================================================

# Índices negativos começam pelo final:
# -1 = último elemento
# -2 = penúltimo elemento
# -3 = antepenúltimo elemento

primeira_fruta = frutas[-4]
ultima_fruta = frutas[-1]
penultima_fruta = frutas[-2]


# ============================================================
# 4. Desempacotando listas (unpacking)
# ============================================================

# É possível atribuir os elementos da lista a variáveis.
itens = ["item1", "item2", "item3", "item4", "item5"]

primeiro, segundo, terceiro, *restante = itens

print(primeiro)   # item1
print(segundo)    # item2
print(terceiro)   # item3
print(restante)   # ['item4', 'item5']

# O * captura os elementos restantes em uma nova lista.
# Também é possível capturar os elementos do início e do fim:
primeiro, segundo, *meio, ultimo = [1, 2, 3, 4, 5, 6]
print(meio)  # [3, 4, 5]


# ============================================================
# 5. Fatiamento (slicing)
# ============================================================

# Sintaxe: lista[inicio:fim:passo]
# - inicio: índice onde começa (incluído).
# - fim: índice onde termina (não incluído).
# - passo: intervalo entre os elementos.
# O fatiamento retorna uma nova lista.

frutas = ["banana", "laranja", "manga", "limão"]

todas = frutas[0:4]
tambem_todas = frutas[:]
laranja_manga = frutas[1:3]
a_partir_da_laranja = frutas[1:]
elementos_alternados = frutas[::2]

# Também é possível usar índices negativos.
ultimas_tres = frutas[-3:]
laranja_e_manga = frutas[-3:-1]

# Passo negativo permite percorrer a lista de trás para frente.
frutas_invertidas = frutas[::-1]


# ============================================================
# 6. Modificando elementos
# ============================================================

# Listas são mutáveis: podemos alterar um elemento pelo índice.
frutas = ["banana", "laranja", "manga", "limão"]
frutas[0] = "abacate"
frutas[-1] = "uva"

print(frutas)  # ['abacate', 'laranja', 'manga', 'uva']


# ============================================================
# 7. Verificando se um elemento existe
# ============================================================

# O operador in retorna True ou False.
frutas = ["banana", "laranja", "manga", "limão"]

print("banana" in frutas)  # True
print("uva" in frutas)     # False


# ============================================================
# 8. Adicionando elementos: append()
# ============================================================

# append() adiciona um único elemento ao final da lista.
frutas = ["banana", "laranja"]
frutas.append("manga")

print(frutas)  # ['banana', 'laranja', 'manga']


# ============================================================
# 9. Inserindo elementos: insert()
# ============================================================

# insert(indice, elemento) insere o elemento na posição indicada.
# Os elementos que já estavam nessa posição ou depois dela
# são deslocados para a direita.

frutas = ["banana", "manga"]
frutas.insert(1, "laranja")

print(frutas)  # ['banana', 'laranja', 'manga']


# ============================================================
# 10. Removendo elementos: remove()
# ============================================================

# remove(valor) remove a primeira ocorrência do valor informado.
frutas = ["banana", "laranja", "manga", "banana"]
frutas.remove("banana")

print(frutas)  # ['laranja', 'manga', 'banana']


# ============================================================
# 11. Removendo elementos: pop()
# ============================================================

# pop() remove e retorna o último elemento, por padrão.
# pop(indice) remove e retorna o elemento do índice informado.

frutas = ["banana", "laranja", "manga", "limão"]

removida = frutas.pop()
print(removida)  # limão

removida = frutas.pop(0)
print(removida)  # banana


# ============================================================
# 12. Removendo elementos: del
# ============================================================

# del remove um elemento pelo índice ou uma faixa de elementos.
frutas = ["banana", "laranja", "manga", "limão", "uva"]

del frutas[0]      # remove o primeiro elemento
del frutas[1:3]    # remove os índices 1 e 2; o índice 3 não é incluído

# del também pode excluir a própria variável:
del frutas


# ============================================================
# 13. Esvaziando uma lista: clear()
# ============================================================

# clear() remove todos os elementos, mas mantém a lista existente.
frutas = ["banana", "laranja", "manga"]
frutas.clear()

print(frutas)  # []


# ============================================================
# 14. Copiando listas: copy()
# ============================================================

# CUIDADO: atribuir uma lista a outra variável não cria uma cópia.
# As duas variáveis passam a referenciar a mesma lista.

original = ["banana", "laranja"]
referencia = original
referencia.append("manga")

print(original)  # ['banana', 'laranja', 'manga']

# copy() cria uma cópia independente no nível dos elementos da lista.
original = ["banana", "laranja"]
copia = original.copy()
copia.append("manga")

print(original)  # ['banana', 'laranja']
print(copia)     # ['banana', 'laranja', 'manga']


# ============================================================
# 15. Juntando listas
# ============================================================

# Operador + cria uma nova lista concatenando as listas.
numeros_positivos = [1, 2, 3]
numeros_negativos = [-3, -2, -1]
numeros = numeros_negativos + [0] + numeros_positivos

# extend() adiciona os elementos de outra coleção ao final
# da lista original, modificando-a.
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_a.extend(lista_b)

print(lista_a)  # [1, 2, 3, 4, 5, 6]


# ============================================================
# 16. Contando ocorrências: count()
# ============================================================

# count(valor) retorna quantas vezes o valor aparece na lista.
idades = [22, 19, 24, 25, 24, 24]
print(idades.count(24))  # 3


# ============================================================
# 17. Encontrando a posição: index()
# ============================================================

# index(valor) retorna o índice da primeira ocorrência do valor.
idades = [22, 19, 24, 25, 24]
print(idades.index(24))  # 2


# ============================================================
# 18. Invertendo a ordem: reverse()
# ============================================================

# reverse() inverte a própria lista (não retorna uma nova lista).
frutas = ["banana", "laranja", "manga"]
frutas.reverse()

print(frutas)  # ['manga', 'laranja', 'banana']


# ============================================================
# 19. Ordenando listas: sort() e sorted()
# ============================================================

# sort() ordena a própria lista, modificando-a.
# Por padrão, a ordem é crescente/alfabética.
numeros = [4, 1, 3, 2]
numeros.sort()
print(numeros)  # [1, 2, 3, 4]

# reverse=True ordena em ordem decrescente.
numeros.sort(reverse=True)
print(numeros)  # [4, 3, 2, 1]

# sorted() retorna uma nova lista ordenada e preserva a original.
frutas = ["banana", "laranja", "manga", "limão"]
frutas_ordenadas = sorted(frutas)
frutas_ordenadas_desc = sorted(frutas, reverse=True)

print(frutas)                 # lista original preservada
print(frutas_ordenadas)       # ['banana', 'laranja', 'limão', 'manga']
print(frutas_ordenadas_desc)  # ordem inversa


# ============================================================
# 20. Resumo rápido
# ============================================================

# Criar lista:          [] ou list()
# Quantidade:           len(lista)
# Acessar elemento:     lista[indice]
# Fatiar:               lista[inicio:fim:passo]
# Verificar existência: elemento in lista
# Alterar elemento:     lista[indice] = valor
# Adicionar ao final:   lista.append(valor)
# Inserir por índice:   lista.insert(indice, valor)
# Remover por valor:    lista.remove(valor)
# Remover por índice:   lista.pop(indice)
# Excluir com del:      del lista[indice]
# Esvaziar:             lista.clear()
# Copiar:               lista.copy()
# Concatenar:           lista1 + lista2
# Adicionar outra lista: lista1.extend(lista2)
# Contar ocorrências:   lista.count(valor)
# Encontrar índice:     lista.index(valor)
# Inverter:             lista.reverse()
# Ordenar modificando:  lista.sort()
# Ordenar sem modificar: sorted(lista)

# Atenção:
# - append() adiciona um elemento; extend() adiciona os elementos
#   de outra coleção individualmente.
# - remove() procura pelo valor; pop() remove por posição.
# - sort() modifica a lista; sorted() cria uma lista ordenada.
# - del lista exclui a variável; clear() apenas esvazia a lista.
