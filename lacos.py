"""
Lacos de repetição em Python:
- for: itera sobre uma sequência (como uma lista, tupla, string, etc) ou um objeto iterável
- while: executa um bloco de código enquanto a condição for verdadeira
- break: interrompe o loop atual
- continue: pula para a próxima iteração do loop
"""

# Exemplo de loop for
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# Exemplo de loop while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Exemplo de uso do break
for i in range(10):
    if i == 5:
        break
    print(i)

# Exemplo de uso do continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
