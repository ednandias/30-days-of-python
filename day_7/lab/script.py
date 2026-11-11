""" 
================================================================================

                                  LEVEL 1

================================================================================
"""

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Canonical', 'System76', 'Red Hat'])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)

# 5. What is the difference between remove and discard
# [Remove] throws an error if the value isn't found, [discard] does not. 

""" 
================================================================================

                                  LEVEL 2

================================================================================
"""

# 1. Join A and B
print(A.union(B))

# 2. Find A intersection B
print(A.intersection(B))

# 3. Is A subset of B
print(A.issubset(B))

# 4. Are A and B disjoint sets
print(A.isdisjoint(B))

# 5. Join A with B and B with A
print(A.union(B))
print(B.union(A))

# 6. What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# 7. Delete the sets completely
del A
del B

""" 
================================================================================

                                  LEVEL 3

================================================================================
"""

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(len(set(age)))
print(len((age)))

# 2. Explain the difference between the following data types: string, list, tuple and set
"""
Resumo - Diferenças entre as Coleções e Tipos Básicos em Python
"""

# ============================================================
# 1. String (str)
# ============================================================
# - Definição: Sequência imutável de caracteres (texto).
# - Mutabilidade: Imutável (não pode ser alterada após criada).
# - Ordem: Ordenada (suporta índices e fatiamento / slicing).
# - Duplicatas: Permite caracteres repetidos.
# - Sintaxe: 'texto', "texto" ou '''texto'''

texto = "Python"
print(texto[0])  # P


# ============================================================
# 2. List (list)
# ============================================================
# - Definição: Coleção ordenada e flexível de itens de qualquer tipo.
# - Mutabilidade: Mutável (permite alterar, adicionar e remover itens).
# - Ordem: Ordenada (suporta índices e fatiamento).
# - Duplicatas: Permite elementos duplicados.
# - Sintaxe: [item1, item2]

lista = ["maçã", "banana", "maçã"]
lista[0] = "laranja"  # Permitido


# ============================================================
# 3. Tuple (tuple)
# ============================================================
# - Definição: Coleção ordenada de itens (semelhante à lista, mas fixa).
# - Mutabilidade: Imutável (não pode ser modificada após a criação).
# - Ordem: Ordenada (suporta índices e fatiamento).
# - Duplicatas: Permite elementos duplicados.
# - Sintaxe: (item1, item2)  (com vírgula obrigatória para 1 item: (item,))

tupla = ("maçã", "banana", "maçã")
# tupla[0] = "laranja"  # Erro! (TypeError)


# ============================================================
# 4. Set (set)
# ============================================================
# - Definição: Coleção não ordenada de elementos únicos.
# - Mutabilidade: Mutável (permite adicionar/remover itens), mas os elementos em si devem ser imutáveis.
# - Ordem: Não ordenada (não suporta índices).
# - Duplicatas: NÃO permite elementos duplicados (remove duplicatas automaticamente).
# - Sintaxe: {item1, item2} ou set() para vazio.

conjunto = {"maçã", "banana", "maçã"}
print(conjunto)  # {'banana', 'maçã'} (sem duplicatas e sem ordem garantida)

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
print(set('I am a teacher and I love to inspire and teach people.'.split()))