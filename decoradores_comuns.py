#@classmethod
#@staticmethod

class MinhaClasse:
    valor = 10

    def __init__(self, nome) -> None:
        self.nome = nome  #atributo da instância

    #requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"
    
    @classmethod
    def metodo_classe(cls):
        return f"Método de classe chamado para valor={cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return f"Método estático sendo chamado"
    

obj = MinhaClasse(nome="Classe exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, config):
        marca, modelo, ano = config.split(",")
        return cls(marca, modelo, int(ano))
    
config1 = "Toyota, Corolla, 2022"
carro1 = Carro.criar_carro(config1)
print(f"Marca: {carro1.marca}\nModelo:{carro1.modelo}\nAno: {carro1.ano}")

class Matematica:
    @staticmethod
    def somar(n1, n2):
        return n1 + n2
    
print(Matematica.somar(n1=22, n2=15))