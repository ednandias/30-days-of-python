"""
30 Days of Python — Day 6: Tuples
================================

Guia de estudo sobre tuplas em Python.

Uma tupla (tuple) é uma coleção:
- ordenada: os elementos mantêm suas posições;
- imutável: não podemos substituir, adicionar ou remover elementos
  diretamente depois que a tupla é criada;
- que pode armazenar diferentes tipos de dados.

Execute este arquivo para ver os exemplos:
    python lesson.py

Dica: experimente alterar os valores dos exemplos e executar novamente.
"""

# ---------------------------------------------------------------------
# 1. Criando tuplas
# ---------------------------------------------------------------------

# Tupla vazia
empty_tuple = ()
another_empty_tuple = tuple()

# Tupla com elementos
fruits = ("banana", "orange", "mango", "lemon")

# Os parênteses são comuns, mas a vírgula é o que define uma tupla.
# Para criar uma tupla com apenas um elemento, use a vírgula:
single_item_tuple = ("banana",)

# Sem a vírgula, isto é apenas uma string entre parênteses:
not_a_tuple = ("banana")

# Uma tupla pode guardar tipos diferentes:
mixed_tuple = ("Python", 30, True, 3.14)


# ---------------------------------------------------------------------
# 2. Descobrindo o tamanho de uma tupla
# ---------------------------------------------------------------------

# len() retorna a quantidade de elementos.
fruits_length = len(fruits)


# ---------------------------------------------------------------------
# 3. Acessando elementos: índices positivos e negativos
# ---------------------------------------------------------------------

# Índices positivos começam em zero.
first_fruit = fruits[0]
second_fruit = fruits[1]

# Índices negativos começam pelo final.
last_fruit = fruits[-1]
second_last_fruit = fruits[-2]

# Atenção: acessar um índice que não existe gera IndexError.


# ---------------------------------------------------------------------
# 4. Fatiamento (slicing)
# ---------------------------------------------------------------------

# A sintaxe é: tupla[inicio:fim]
# O índice final NÃO é incluído no resultado.
first_two_fruits = fruits[0:2]
from_second_to_end = fruits[1:]
all_fruits = fruits[:]

# Também podemos usar índices negativos.
last_two_fruits = fruits[-2:]
middle_fruits = fruits[1:-1]

# Com passo: tupla[inicio:fim:passo]
every_other_fruit = fruits[::2]
reversed_fruits = fruits[::-1]


# ---------------------------------------------------------------------
# 5. Tuplas são imutáveis
# ---------------------------------------------------------------------

# A linha abaixo causaria TypeError. Remova o comentário para testar:
# fruits[0] = "apple"

# Não podemos usar métodos de lista como append(), insert() ou remove()
# diretamente em uma tupla.


# ---------------------------------------------------------------------
# 6. Convertendo entre tupla e lista para fazer alterações
# ---------------------------------------------------------------------

# list() cria uma lista a partir da tupla.
fruits_list = list(fruits)

# Agora podemos alterar a lista.
fruits_list[0] = "apple"
fruits_list.append("grape")

# tuple() cria uma nova tupla a partir da lista.
updated_fruits = tuple(fruits_list)


# ---------------------------------------------------------------------
# 7. Verificando se um elemento existe
# ---------------------------------------------------------------------

# O operador in retorna True ou False.
has_orange = "orange" in fruits
has_apple = "apple" in fruits


# ---------------------------------------------------------------------
# 8. Métodos de tupla: count() e index()
# ---------------------------------------------------------------------

numbers = (1, 2, 3, 2, 4, 2)

# count() conta quantas vezes um valor aparece.
number_of_twos = numbers.count(2)

# index() retorna a posição da primeira ocorrência.
first_position_of_two = numbers.index(2)


# ---------------------------------------------------------------------
# 9. Juntando tuplas
# ---------------------------------------------------------------------

vegetables = ("tomato", "potato", "carrot")
animal_products = ("milk", "egg", "cheese")

# O operador + cria uma NOVA tupla.
food_stuff = fruits + vegetables + animal_products


# ---------------------------------------------------------------------
# 10. Desempacotamento (unpacking)
# ---------------------------------------------------------------------

# Cada variável recebe o elemento correspondente.
person = ("Ana", 28, "Brasil")
name, age, country = person

# O * captura os elementos restantes em uma lista.
first, *middle, last = ("a", "b", "c", "d", "e")


# ---------------------------------------------------------------------
# 11. Excluindo uma tupla
# ---------------------------------------------------------------------

# Não podemos excluir apenas um elemento da tupla.
# del remove a variável (o nome que aponta para a tupla).
temporary_tuple = ("a", "b", "c")
del temporary_tuple


# ---------------------------------------------------------------------
# 12. Exemplos reunidos
# ---------------------------------------------------------------------

def show_examples():
    """Mostra alguns resultados dos exemplos deste guia."""
    print("\n--- Guia de tuplas ---")
    print("Tupla de frutas:", fruits)
    print("Quantidade de frutas:", fruits_length)
    print("Primeira fruta:", first_fruit)
    print("Última fruta:", last_fruit)
    print("Primeiras duas frutas:", first_two_fruits)
    print("Frutas em ordem inversa:", reversed_fruits)
    print("Tupla convertida e modificada:", updated_fruits)
    print("Existe orange?", has_orange)
    print("Existe apple?", has_apple)
    print("O número 2 aparece:", number_of_twos, "vezes")
    print("Alimentos:", food_stuff)
    print(f"Pessoa: {name}, {age} anos, {country}")
    print("Desempacotamento com *:", first, middle, last)


# ---------------------------------------------------------------------
# 13. Exercícios para praticar
# ---------------------------------------------------------------------

def exercises():
    """
    Faça os exercícios abaixo sem consultar soluções prontas.
    Use os exemplos anteriores como referência.
    """

    # Nível 1
    # 1. Crie uma tupla vazia.
    # 2. Crie uma tupla com nomes de irmãos e irmãs.
    # 3. Junte duas tuplas: brothers e sisters.
    # 4. Descubra quantos irmãos você tem usando len().
    # 5. Crie uma nova tupla que também contenha o nome dos seus pais.
    #
    # Nível 2
    # 6. Desempacote os irmãos e os pais em variáveis separadas.
    # 7. Crie tuplas de frutas, vegetais e produtos de origem animal.
    # 8. Junte as três tuplas em food_stuff_tp.
    # 9. Converta food_stuff_tp em uma lista.
    # 10. Extraia o(s) elemento(s) do meio usando slicing.
    # 11. Extraia os três primeiros e os três últimos elementos.
    # 12. Verifique se 'Estonia' e 'Iceland' estão na tupla nordic_countries.

    nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

    # Comece escrevendo seu código abaixo:
    pass


if __name__ == "__main__":
    show_examples()
    print("\nOs exercícios estão na função exercises().")
    print("Abra o arquivo e complete os desafios no seu próprio ritmo.")
