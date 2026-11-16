"""
Resumo - Python em 30 Dias
Dia 9: Condicionais (Conditionals)

Resumo do conteúdo teórico. Os exercícios do material original foram omitidos.
"""

# ============================================================
# 1. Estrutura condicional: if
# ============================================================

# O bloco de código é executado apenas se a condição for verdadeira (Truthy).
# Atenção à indentação (espaçamento) após os dois-pontos (:).
a = 3
if a > 0:
    print("A é um número positivo")


# ============================================================
# 2. Estrutura condicional: if-else
# ============================================================

# Se a condição do if for falsa, o bloco do else é executado.
a = -3
if a > 0:
    print("A é positivo")
else:
    print("A é negativo ou zero")


# ============================================================
# 3. Múltiplas condições: if-elif-else
# ============================================================

# Usado quando precisamos testar várias condições sequencialmente.
a = 0
if a > 0:
    print("A é positivo")
elif a < 0:
    print("A é negativo")
else:
    print("A é zero")


# ============================================================
# 4. Short Hand (If Ternário)
# ============================================================

# Sintaxe compacta para tomada de decisão em uma única linha.
a = 3
print("A é positivo") if a > 0 else print("A é negativo")


# ============================================================
# 5. Condições Aninhadas (Nested Conditions)
# ============================================================

# Condições dentro de outras condições.
a = 4
if a > 0:
    if a % 2 == 0:
        print("A é positivo e par")
    else:
        print("A é positivo e ímpar")


# ============================================================
# 6. Condicionais com Operadores Lógicos (and / or)
# ============================================================

# Combinando múltiplas condições para evitar aninhamentos excessivos (and):
a = 4
if a > 0 and a % 2 == 0:
    print("A é positivo e par")

# Verificando se pelo menos uma condição é verdadeira (or):
usuario = "admin"
nivel_acesso = 3

if usuario == "admin" or nivel_acesso >= 4:
    print("Acesso concedido!")
else:
    print("Acesso negado!")