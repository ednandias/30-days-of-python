"""
Resumo - Python em 30 Dias
Dia 2: Variáveis e Funções Embutidas (Variables, Builtin Functions)

Resumo do conteúdo teórico. Os exercícios do material original foram omitidos.
"""

# ============================================================
# 1. Funções Embutidas (Built-in Functions)
# ============================================================

# Funções globais disponíveis nativamente em Python, sem necessidade de importação.
# Exemplos comuns: print(), len(), type(), int(), float(), str(), input(), sum(), max(), min()

print("Olá, Mundo!")  # Exibe dados no console
print("Python", "é", "legal")  # Aceita múltiplos argumentos

tamanho = len("Python")  # Retorna o tamanho (quantidade de elementos/caracteres)
print(tamanho)  # 6


# ============================================================
# 2. Variáveis e Regras de Nomenclatura
# ============================================================

# Variáveis armazenam dados na memória do computador.
# Em Python, utilizamos o padrão "snake_case" para nomes compostos.

# Nomes válidos:
nome = "Asabeneh"
primeiro_nome = "Asabeneh"
ano_2021 = 2021
_variavel_privada = "privado"

# Declaração de múltiplos valores em uma única linha:
nome, sobrenome, pais, idade = "Asabeneh", "Yetayeh", "Finlândia", 250

# Exemplo completo com diferentes tipos de dados:
primeiro_nome = "Asabeneh"
ultimo_nome = "Yetayeh"
pais = "Finlândia"
cidade = "Helsinque"
idade = 250
casado = True
habilidades = ["HTML", "CSS", "JS", "React", "Python"]
info_pessoal = {
    "primeiro_nome": "Asabeneh",
    "ultimo_nome": "Yetayeh",
    "pais": "Finlândia",
    "cidade": "Helsinque"
}


# ============================================================
# 3. Tipos de Dados (Data Types)
# ============================================================

# Tipos primitivos e estruturais mais comuns:
# - str (String): Textos
# - int (Integer): Números inteiros
# - float (Float): Números decimais
# - complex (Complex): Números complexos (ex: 1 + 1j)
# - bool (Boolean): True ou False
# - list (Lista): Coleção ordenada e mutável
# - tuple (Tupla): Coleção ordenada e imutável
# - dict (Dicionário): Coleção de pares chave-valor


# ============================================================
# 4. Verificação de Tipos e Conversão (Casting)
# ============================================================

# type() retorna o tipo de dado de uma variável ou valor
print(type(10))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Texto"))     # <class 'str'>
print(type(True))        # <class 'bool'>
print(type([1, 2, 3]))   # <class 'list'>

# Casting: Conversão explícita entre tipos
numero_inteiro = 10
numero_float = float(numero_inteiro)  # 10.0
print(numero_float)

gravidade = 9.81
numero_convertido_int = int(gravidade)  # 9 (descarta a parte decimal)
print(numero_convertido_int)

# String para número
string_numero = "10.6"
convertido_float = float(string_numero)
convertido_int = int(convertido_float)
print(convertido_int)  # 10

# String para lista de caracteres
nome_str = "Python"
lista_caracteres = list(nome_str)
print(lista_caracteres)  # ['P', 'y', 't', 'h', 'o', 'n']


# ============================================================
# 5. Números em Python
# ============================================================

# 1. Inteiros (Integers): ..., -3, -2, -1, 0, 1, 2, 3, ...
# 2. Ponto Flutuante (Floats): ..., -2.5, 0.0, 3.14, ...
# 3. Números Complexos (Complex): 1 + j, 2 + 4j