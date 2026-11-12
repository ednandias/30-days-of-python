"""
Resumo - Python em 30 Dias
Dia 8: Dicionários (Dictionaries)

Resumo do conteúdo teórico. Os exercícios do material original foram omitidos.
"""

# ============================================================
# 1. O que são dicionários e como criá-las
# ============================================================

# Um dicionário é uma coleção desordenada, mutável e indexada por pares (chave: valor).
# As chaves devem ser únicas e imutáveis (como strings, números ou tuplas).

# Formas de criar um dicionário vazio:
dicionario_vazio_1 = {}
dicionario_vazio_2 = dict()

# Dicionário com dados iniciais (os valores podem ser de qualquer tipo):
pessoa = {
    "primeiro_nome": "Asabeneh",
    "ultimo_nome": "Yetayeh",
    "idade": 250,
    "pais": "Finlândia",
    "casado": True,
    "habilidades": ["JavaScript", "React", "Node", "Python"],
    "endereco": {
        "rua": "Space street",
        "cep": "02210"
    }
}

# len() retorna a quantidade de pares (chave: valor) no dicionário.
print(len(pessoa))  # 7


# ============================================================
# 2. Acessando itens do dicionário
# ============================================================

# Acesso direto pela chave (gera KeyError se a chave não existir):
print(pessoa["primeiro_nome"])      # Asabeneh
print(pessoa["habilidades"][0])     # JavaScript
print(pessoa["endereco"]["rua"])    # Space street

# Método get(): Retorna o valor da chave ou None se ela não existir (evita erros).
print(pessoa.get("pais"))           # Finlândia
print(pessoa.get("cidade"))         # None


# ============================================================
# 3. Adicionando e modificando itens
# ============================================================

# Adicionando um novo par (chave: valor):
pessoa["cargo"] = "Instrutor"
pessoa["habilidades"].append("HTML")

# Modificando o valor de uma chave existente:
pessoa["idade"] = 252


# ============================================================
# 4. Verificando chaves e removendo elementos
# ============================================================

# O operador in verifica se uma CHAVE existe no dicionário:
print("pais" in pessoa)      # True
print("telefone" in pessoa)  # False

# Métodos de remoção:
# pop(chave): Remove a chave especificada e retorna seu valor.
pessoa.pop("casado")

# popitem(): Remove e retorna o último par (chave: valor) adicionado.
pessoa.popitem()

# del: Remove o item pela chave informada.
del pessoa["idade"]


# ============================================================
# 5. Métodos Úteis de Dicionários
# ============================================================

# keys(): Retorna todas as chaves do dicionário.
chaves = pessoa.keys()
print(chaves)  # dict_keys([...])

# values(): Retorna todos os valores do dicionário.
valores = pessoa.values()
print(valores)  # dict_values([...])

# items(): Retorna uma lista de tuplas contendo os pares (chave, valor).
itens = pessoa.items()
print(itens)  # dict_items([('primeiro_nome', 'Asabeneh'), ...])

# copy(): Cria uma cópia rasa (shallow copy) para evitar mutações no original.
pessoa_copia = pessoa.copy()

# clear(): Remove todos os elementos do dicionário (mantendo-o vazio).
temporario = {"a": 1, "b": 2}
temporario.clear()  # {}

# del (completo): Exclui a variável do dicionário inteira da memória.
del temporario