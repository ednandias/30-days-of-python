"""
Resumo - Python em 30 Dias
Dia 10: Laços de Repetição (Loops)

Resumo do conteúdo teórico. Os exercícios do material original foram omitidos.
"""

# ============================================================
# 1. Laço While (While Loop)
# ============================================================

# Executa um bloco de código repetidamente enquanto a condição for verdadeira (Truthy).
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# While-Else: O bloco else é executado quando a condição do while se torna falsa.
contador = 0
while contador < 3:
    contador += 1
else:
    print("O loop while terminou. Contador:", contador)


# ============================================================
# 2. Controle de Fluxo: break e continue (While)
# ============================================================

# break: Interrompe e sai do loop imediatamente.
contador = 0
while contador < 5:
    if contador == 3:
        break
    print(contador)
    contador += 1

# continue: Pula a iteração atual e avança para a próxima.
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue  # Pula o número 3
    print(contador)


# ============================================================
# 3. Laço For (For Loop)
# ============================================================

# Usado para iterar sobre sequências (listas, tuplas, strings, sets, dicionários).

# Iterando sobre uma lista:
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

# Iterando sobre uma string:
palavra = "Python"
for letra in palavra:
    print(letra)

# Iterando sobre um dicionário (retorna as chaves por padrão):
pessoa = {"primeiro_nome": "Asabeneh", "idade": 250}
for chave in pessoa:
    print(chave)

# Iterando sobre chaves e valores com .items():
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


# ============================================================
# 4. A Função range()
# ============================================================

# Gera uma sequência numérica: range(inicio, fim, passo)
# O valor final é exclusivo (não incluído).

for i in range(5):        # De 0 a 4 (começa em 0 por padrão)
    print(i)

for i in range(1, 6):     # De 1 a 5
    print(i)

for i in range(0, 10, 2):  # De 0 a 8 com passo 2 (pares)
    print(i)


# ============================================================
# 5. Laços Aninhados (Nested For Loops)
# ============================================================

# Um loop dentro de outro loop.
matriz = [[1, 2], [3, 4]]
for linha in matriz:
    for elemento in linha:
        print(elemento)


# ============================================================
# 6. For-Else e a instrução pass
# ============================================================

# For-Else: O bloco else é executado após o término completo do loop for.
for i in range(3):
    print(i)
else:
    print("O loop for terminou com sucesso.")

# pass: Usado como um espaço reservado (placeholder) quando a sintaxe exige código,
# mas nenhuma ação deve ser executada.
for i in range(5):
    pass