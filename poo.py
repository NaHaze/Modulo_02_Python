# objetos são instancias de classes.
# classes e objetos

#Classes (modelo,  uma regra)
  # dentro de classes temos:
    # atributos: propriedades desta classe
    # métodos: ações (o que poderão fazer)
#Quando está fora de uma classe é uma função e quando está dentro de uma classe se referencia como método(construtor)
# Toda classe vai ter este método
# O self é uma referencia a sua propria classe, é uma porta de acesso pra que consiga utilizar os métodos
#e os atributos desta classe.
# O -> None ela é uma dica, por padrão é utilizada, ele define que este método não tem retorno.
# O Objeto é uma instância desta classe, ele é criado a partir daquela classe, respeitando os métodos e 
#atributos que a classe tem.

#classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

#Objetos
pessoa1 = Pessoa("Ana", 28)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa("Amélia", 30)
mensagem = pessoa2.saudacao()
print(mensagem)