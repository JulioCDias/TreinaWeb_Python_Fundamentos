"""
Orientação a Objetos é um paradigma de programação que utiliza "objetos" para modelar dados e funcionalidades. Em Python, tudo é um objeto, o que torna a orientação a objetos uma parte fundamental da linguagem.
- Classe: é um molde para criar objetos. Define atributos (variáveis) e métodos (funções) que os objetos criados a partir da classe terão.
- Objeto: é uma instância de uma classe. Ele possui os atributos e métodos definidos na classe.
- Atributos: são as características ou propriedades de um objeto. Podem ser definidos dentro da classe e acessados pelos objetos.
- Métodos: são as ações ou comportamentos que um objeto pode realizar. São definidos dentro da classe e podem acessar os atributos do objeto.
- Encapsulamento: é o conceito de esconder os detalhes internos de um objeto e fornecer uma interface
pública para interagir com ele. Em Python, isso é feito usando convenções de nomenclatura (ex: _atributo para indicar que é privado).
- Herança: é o mecanismo pelo qual uma classe pode herdar atributos e métodos de outra
classe. A classe que herda é chamada de classe filha ou subclasse, e a classe que é herdada é chamada de classe pai ou superclasse.
- Polimorfismo: é a capacidade de um objeto de uma classe ser tratado como um
objeto de outra classe. Isso é possível através da herança e permite que métodos sejam usados de forma intercambiável entre classes relacionadas.
- Abstração: é o processo de ocultar os detalhes complexos e mostrar apenas as funcionalidades essenciais de um objeto. Em Python, isso pode ser alcançado usando classes abstratas e métodos abstratos.

# Exemplo de classe e objeto em Python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância
    def apresentar(self):  # Método de instância
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("Julio", 30)
pessoa1.apresentar()  # Chamada do método apresentar


"""


class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        if self.especie == "cachorro":
            return "Au au!"
        elif self.especie == "gato":
            return "Miau!"
        else:
            return "Som desconhecido."

    class meta:
        descricao = "Classe que representa um animal."
