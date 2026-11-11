"""
Resumo - Python em 30 Dias
Dia 4: Strings

Resumo do conteúdo teórico. Os exercícios do material original foram omitidos.
"""

# ============================================================
# 1. O que são strings e como criá-las
# ============================================================

# Textos são do tipo string. Podem ser delimitados por aspas simples, duplas ou triplas.
letra = 'P'
print(letra)       # P
print(len(letra))  # 1

saudacao = "Hello, World!"
print(saudacao)       # Hello, World!
print(len(saudacao))  # 13

# Strings multilinha usam três aspas simples (''') ou duplas ("""):
multilinear = '''Eu sou um professor e adoro ensinar.
Não há nada mais gratificante do que empoderar pessoas.'''
print(multilinear)


# ============================================================
# 2. Concatenação de strings
# ============================================================

# É possível juntar strings utilizando o operador de adição (+)
primeiro_nome = "Asabeneh"
ultimo_nome = "Yetayeh"
espaco = " "

nome_completo = primeiro_nome + espaco + ultimo_nome
print(nome_completo)  # Asabeneh Yetayeh

print(len(primeiro_nome))                 # 8
print(len(primeiro_nome) > len(ultimo_nome))  # True


# ============================================================
# 3. Sequências de escape (Escape Sequences)
# ============================================================

# A barra invertida (\) indica caracteres especiais:
# \n: Nova linha
# \t: Tabulação (espaços)
# \\: Barra invertida literal
# \': Aspas simples
# \": Aspas duplas

print("Desafio Python.\nVocê curte?")
print("Dia\tTópicos\tExercícios")
print("Este é um símbolo de barra invertida (\\)")
print("Na programação, começa com \"Hello, World!\"")


# ============================================================
# 4. Formatação de strings
# ============================================================

# --- 4.1. Estilo Antigo (% Operator) ---
# Usa especificadores como %s (string), %d (inteiro), %f (float)
linguagem = "Python"
formatada_antiga = "Eu me chamo %s %s e ensino %s." % (primeiro_nome, ultimo_nome, linguagem)
print(formatada_antiga)

raio = 10
pi = 3.14
area = pi * raio ** 2
formatada_circulo = "A área do círculo com raio %d é %.2f." % (raio, area)
print(formatada_circulo)

# --- 4.2. Novo Estilo (str.format) ---
formatada_novo = "Eu sou {} {}. Eu ensino {}.".format(primeiro_nome, ultimo_nome, linguagem)
print(formatada_novo)

a, b = 4, 3
print("{} / {} = {:.2f}".format(a, b, a / b))

# --- 4.3. Interpolação (f-strings - Python 3.6+) ---
# Método mais moderno e recomendado
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")
print(f"A área do círculo com raio {raio} é {pi * raio ** 2:.2f}.")


# ============================================================
# 5. Strings como sequências de caracteres
# ============================================================

# --- 5.1. Desempacotamento (Unpacking) ---
palavra = "Python"
p, y, t, h, o, n = palavra
print(p)  # P
print(n)  # n

# --- 5.2. Índices positivos e negativos ---
primeira_letra = palavra[0]    # P
ultima_letra = palavra[-1]     # n
penultima_letra = palavra[-2]  # o

# --- 5.3. Fatiamento (Slicing: string[inicio:fim:passo]) ---
tres_primeiras = palavra[0:3]  # Pyt
tres_ultimas = palavra[3:]     # hon
ultimas_negativas = palavra[-3:]  # hon

# --- 5.4. Reversing e pulando caracteres ---
palavra_invertida = palavra[::-1]  # nohtyP
pulando_caracteres = palavra[0:6:2]  # Pto


# ============================================================
# 6. Principais Métodos de Strings
# ============================================================

texto = "trinta dias de python"

# Maiúsculas e minúsculas
print(texto.capitalize())  # Trinta dias de python
print(texto.upper())       # TRINTA DIAS DE PYTHON
print(texto.title())       # Trinta Dias De Python
print(texto.swapcase())    # TRINTA DIAS DE PYTHON

# Buscas e contagens
print(texto.count("y"))          # 3
print(texto.find("d"))           # 7 (retorna -1 se não achar)
print(texto.rfind("y"))          # 16 (última ocorrência)
print(texto.startswith("trinta"))  # True
print(texto.endswith("python"))    # True

# Validações (retornam booleano)
print("Python30".isalnum())     # True (alfanumérico)
print("Python".isalpha())       # True (apenas letras)
print("12345".isdigit())        # True (apenas dígitos)
print(texto.islower())          # True

# Manipulação e transformação
tecnologias = ["HTML", "CSS", "JavaScript", "React"]
unidas = " - ".join(tecnologias)
print(unidas)  # HTML - CSS - JavaScript - React

espacado = "   Python   "
print(espacado.strip())  # Remove espaços nas pontas -> 'Python'

substituido = texto.replace("python", "coding")
print(substituido)  # trinta dias de coding

separado = texto.split(" ")
print(separado)  # ['trinta', 'dias', 'de', 'python']