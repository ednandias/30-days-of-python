"""
Resumo - Python em 30 Dias
Dia 6: Tuplas (Tuples)

Resumo do conteúdo teórico. Os exercícios do material original foram omitidos.
"""

# ============================================================
# 1. O que são tuplas e como criá-las
# ============================================================

# Uma tupla é uma coleção ordenada e imutável de elementos.
# Características: ordenada, imutável, permite duplicatas e diferentes tipos de dados.

# Formas de criar uma tupla vazia:
tupla_vazia_1 = ()
tupla_vazia_2 = tuple()

# Tupla com elementos:
frutas = ("banana", "laranja", "manga", "limão")

# ATENÇÃO: Para criar uma tupla com apenas um elemento, é obrigatório o uso de vírgula:
tupla_unico_elemento = ("banana",)

# len() retorna a quantidade de elementos.
print(len(frutas))  # 4


# ============================================================
# 2. Acessando elementos por índice
# ============================================================

# Índices positivos (começam em 0):
primeira_fruta = frutas[0]  # banana
segunda_fruta = frutas[1]   # laranja

# Índices negativos (começam pelo final, -1 é o último):
ultima_fruta = frutas[-1]   # limão
penultima_fruta = frutas[-2]  # manga


# ============================================================
# 3. Fatiamento (Slicing)
# ============================================================

# Sintaxe: tupla[inicio:fim:passo]
# O fatiamento retorna uma NOVA tupla.

todas_frutas = frutas[:]
laranja_e_manga = frutas[1:3]
a_partir_da_laranja = frutas[1:]
ultimas_tres = frutas[-3:]
frutas_invertidas = frutas[::-1]


# ============================================================
# 4. Convertendo entre Tupla e Lista
# ============================================================

# Como tuplas são imutáveis, para modificá-las convertemos em lista:
frutas_lista = list(frutas)
frutas_lista[0] = "abacate"
frutas_modificadas = tuple(frutas_lista)

print(frutas_modificadas)  # ('abacate', 'laranja', 'manga', 'limão')


# ============================================================
# 5. Verificando se um elemento existe
# ============================================================

# O operador in retorna True ou False.
print("laranja" in frutas)  # True
print("maçã" in frutas)     # False


# ============================================================
# 6. Métodos de Tuplas: count() e index()
# ============================================================

# count(valor): Retorna quantas vezes o elemento aparece.
numeros = (1, 2, 2, 3, 2, 4)
print(numeros.count(2))  # 3

# index(valor): Retorna o índice da primeira ocorrência do elemento.
print(frutas.index("manga"))  # 2


# ============================================================
# 7. Unindo tuplas e exclusão (del)
# ============================================================

# O operador + concatena tuplas gerando uma nova tupla.
vegetais = ("tomate", "batata")
frutas_e_vegetais = frutas + vegetais
print(frutas_e_vegetais)

# del exclui a variável inteira da memória (não é possível remover itens isolados).
temporaria = (1, 2, 3)
del temporaria