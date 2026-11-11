"""
Resumo - Python em 30 Dias
Dia 1: Introdução (Introduction)

Resumo do conteúdo teórico. Os exercícios do material original foram omitidos.
"""

# ============================================================
# 1. A função print()
# ============================================================

# A função print() é usada para exibir saídas no console.
print("Hello World!")   # Imprime uma string simples


# ============================================================
# 2. Operações Aritméticas Básicas
# ============================================================

print("Adição:", 2 + 3)         # 5
print("Subtração:", 3 - 1)      # 2
print("Multiplicação:", 2 * 3)  # 6
print("Divisão:", 3 / 2)        # 1.5 (retorna float)
print("Exponenciação:", 3 ** 2) # 9 (3 elevado a 2)
print("Módulo (resto):", 3 % 2) # 1
print("Divisão inteira:", 3 // 2) # 1 (descarta a parte decimal)


# ============================================================
# 3. Verificação de Tipos de Dados (type())
# ============================================================

# A função type() retorna o tipo de dado de um valor ou objeto.
print(type(10))                    # <class 'int'> - Inteiro
print(type(3.14))                  # <class 'float'> - Ponto flutuante
print(type(1 + 3j))                # <class 'complex'> - Número complexo
print(type("Asabeneh"))            # <class 'str'> - String
print(type([1, 2, 3]))             # <class 'list'> - Lista
print(type({"name": "Asabeneh"}))  # <class 'dict'> - Dicionário
print(type({9.8, 3.14, 2.7}))      # <class 'set'> - Conjunto (Set)