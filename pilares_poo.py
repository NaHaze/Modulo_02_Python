#Herança
print("\nExemplo de herança:")

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, Au"
class Gato(Animal):
    def emitir_som(self):
        return "Miau"
    
dog = Cachorro(nome="Bola")
cat = Gato(nome="Tutu")

print("\nExemplo de Polimorfismo" )
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplos de Encapsulamento")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo #atributo privado "__saldo"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=300)
print(f"Saldo da conta {conta.consultar_saldo()}")

conta_pessoa_fisica = ContaBancaria(saldo=100)

print(f"\n Abstração: ")

from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar (self):
        pass
    @abstractmethod
    def desligar (self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass
    def ligar(self):
        return "Carro ligado usando chave"
    def desligar(self):
        return"Carro desligado usando chave"
    
carro_preto = Carro()
print(carro_preto.ligar())
print(carro_preto.ligar())

print(f"\n Herança Múltipla: ")
