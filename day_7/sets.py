"""
Resumo - Python em 30 Dias
Dia 7: Conjuntos (Sets)

Resumo do conteúdo teórico. Os exercícios do material original foram omitidos.
"""

# ============================================================
# 1. O que são sets e como criá-los
# ============================================================

# Um set é uma coleção desordenada, sem índices e de elementos únicos.
# Útil para eliminar duplicatas e realizar operações matemáticas.

# ATENÇÃO: {} cria um dicionário vazio. Para criar um set vazio, use set():
conjunto_vazio = set()

# Set com elementos iniciais:
frutas = {"banana", "laranja", "manga", "limão"}

# len() retorna a quantidade de elementos únicos.
print(len(frutas))  # 4


# ============================================================
# 2. Adicionando e removendo elementos
# ============================================================

# add(): Adiciona um único elemento.
frutas.add("uva")

# update(): Adiciona múltiplos elementos (recebe um iterável).
frutas.update(["maçã", "morango"])

# remove(): Remove o elemento especificado. Gera KeyError se não existir.
frutas.remove("maçã")

# discard(): Remove o elemento se ele existir (não gera erro se não encontrar).
frutas.discard("abacate")

# pop(): Remove e retorna um elemento arbitrário (já que sets não têm ordem).
fruta_removida = frutas.pop()


# ============================================================
# 3. Convertendo Listas em Sets
# ============================================================

# A conversão elimina valores duplicados automaticamente.
lista_frutas = ["banana", "laranja", "banana", "limão"]
frutas_unicas = set(lista_frutas)
print(frutas_unicas)  # Elementos duplicados removidos (sem ordem garantida)


# ============================================================
# 4. Operações Matemáticas de Conjuntos
# ============================================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# --- 4.1. União (union() ou |) ---
# Retorna todos os elementos de ambos (sem duplicatas).
uniao = set_a.union(set_b)       # {1, 2, 3, 4, 5}
# uniao = set_a | set_b

# --- 4.2. Interseção (intersection() ou &) ---
# Retorna apenas os elementos presentes em ambos os conjuntos.
intersecao = set_a.intersection(set_b)  # {3}
# intersecao = set_a & set_b

# --- 4.3. Diferença (difference() ou -) ---
# Retorna elementos que estão no primeiro set, mas não no segundo.
diferenca = set_a.difference(set_b)     # {1, 2}
# diferenca = set_a - set_b

# --- 4.4. Diferença Simétrica (symmetric_difference() ou ^) ---
# Retorna elementos que estão em apenas um dos conjuntos (exclui a interseção).
dif_simetrica = set_a.symmetric_difference(set_b)  # {1, 2, 4, 5}
# dif_simetrica = set_a ^ set_b


# ============================================================
# 5. Verificações de Relação (Subset, Superset e Disjoint)
# ============================================================

pequeno = {2, 3}
grande = {1, 2, 3, 4}

# issubset(): Verifica se todos os elementos do set estão no outro.
print(pequeno.issubset(grande))     # True

# issuperset(): Verifica se o set contém todos os elementos do outro.
print(grande.issuperset(pequeno))   # True

# isdisjoint(): Retorna True se os sets não possuem nenhum elemento em comum.
pares = {0, 2, 4}
impares = {1, 3, 5}
print(pares.isdisjoint(impares))    # True