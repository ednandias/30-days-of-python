"""
Resumo - Python em 30 Dias
Dia 3: Operadores (Operators)

Resumo do conteúdo teórico. Os exercícios do material original foram omitidos.
"""

# ============================================================
# 1. Booleanos (Booleans)
# ============================================================

# Representam um dos dois valores: True (Verdadeiro) ou False (Falso).
# Atenção: As iniciais DEVEM ser maiúsculas em Python.
print(True)   # True
print(False)  # False


# ============================================================
# 2. Operadores de Atribuição (Assignment Operators)
# ============================================================

# O sinal de igual (=) armazena um valor em uma variável.
x = 10
x += 5  # Equivalente a x = x + 5
x -= 2  # Equivalente a x = x - 2
x *= 3  # Equivalente a x = x * 3
x /= 2  # Equivalente a x = x / 2


# ============================================================
# 3. Operadores Aritméticos (Arithmetic Operators)
# ============================================================

# Exemplos com inteiros e floats
print("Adição:", 1 + 2)                 # 3
print("Subtração:", 2 - 1)              # 1
print("Multiplicação:", 2 * 3)          # 6
print("Divisão:", 4 / 2)                # 2.0 (sempre retorna float)
print("Divisão inteira:", 7 // 2)       # 3 (descarta o resto/decimal)
print("Módulo (resto):", 3 % 2)         # 1
print("Exponenciação:", 2 ** 3)         # 8 (2 * 2 * 2)

# Números complexos
numero_complexo = 1 + 1j
print("Multiplicação de complexos:", (1 + 1j) * (1 - 1j))  # (2+0j)

# Exemplo prático: Cálculo de área e peso
raio = 10
area_circulo = 3.14 * raio ** 2
print("Área do círculo:", area_circulo)

massa = 75
gravidade = 9.81
peso = massa * gravidade
print("Peso:", peso, "N")


# ============================================================
# 4. Operadores de Comparação (Comparison Operators)
# ============================================================

# Comparam valores e retornam True ou False
print(3 > 2)    # True
print(3 >= 2)   # True
print(3 < 2)    # False
print(2 < 3)    # True
print(3 == 2)   # False
print(3 != 2)   # True

# Comparando comprimentos de strings
print(len("maca") == len("pera"))  # True


# ============================================================
# 5. Operadores de Identidade e Associação
# ============================================================

# Identidade (is / is not)
print("1 é 1:", 1 is 1)          # True (mesmo objeto na memória)
print("1 não é 2:", 1 is not 2)  # True

# Associação (in / not in)
print("'A' em 'Asabeneh':", "A" in "Asabeneh")         # True
print("'coding' em 'coding for all':", "coding" in "coding for all")  # True


# ============================================================
# 6. Operadores Lógicos (Logical Operators)
# ============================================================

# Utilizam as palavras-chave: and, or, not

# AND: Retorna True apenas se ambas as condições forem verdadeiras
print(3 > 2 and 4 > 3)  # True
print(3 > 2 and 4 < 3)  # False

# OR: Retorna True se pelo menos uma condição for verdadeira
print(3 > 2 or 4 < 3)   # True
print(3 < 2 or 4 < 3)   # False

# NOT: Inverte o valor booleano (negação)
print(not(3 > 2))       # False (3 > 2 é True, o not inverte para False)
print(not True)         # False
print(not False)        # True