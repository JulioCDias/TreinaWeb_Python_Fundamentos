"""
Tipos de Dados em Python:
- str: para texto (ex: "Olá, Mundo!")
- int: para números inteiros (ex: 42)
- float: para números decimais (ex: 3.14)
- bool: para valores booleanos (ex: True ou False)
- list: para listas de itens (ex: [1, 2, 3])
- dict: para dicionários (ex: {"chave": "valor"})
- tuple: para tuplas (ex: (1, 2, 3))
- set: para conjuntos (ex: {1, 2, 3})
- NoneType: para o valor None (ex: None)
- complex: para números complexos (ex: 1 + 2j)
"""

nome = "Julio"
idade = 30
sobrenome = "Dias"
print(f"Olá, meu nome é {nome} {sobrenome} e tenho {idade} anos.")


seuNome = input("Digite seu nome: ")
print(f"Olá, {seuNome}! Bem-vindo ao mundo da programação em Python!")

print(type(nome))
print(type(idade))
print(type(sobrenome))

# Variáveis em Python:
# - Devem começar com uma letra ou um sublinhado (_)
# - Podem conter letras, números e sublinhados
# - São case-sensitive (diferenciam maiúsculas de minúsculas)
# - Não podem ser palavras reservadas (ex: if, else, for, etc.)

# Exemploo de declaração de variáveis:
numero = 10
letras = "abc"
booleano = True
lista = [1, 2, 3]
dicionario = {"chave": "valor"}
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
none_value = None
complexo = 1 + 2j

print(numero)
print(letras)
print(booleano)
print(lista)
print(dicionario)
print(tupla)
print(conjunto)
print(none_value)
print(complexo)

print(type(numero))
print(type(letras))
print(type(booleano))
print(type(lista))
print(type(dicionario))
print(type(tupla))
print(type(conjunto))
print(type(none_value))
print(type(complexo))
