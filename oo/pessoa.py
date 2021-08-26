class Pessoa:
    def __init__(self, *filhos, nome=None, idade=19):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    guilherme = Pessoa(nome='Guilherme')
    zeze = Pessoa(guilherme, nome='Zeze')
    print(Pessoa.cumprimentar(zeze))
    print(id(zeze))
    print(zeze.cumprimentar())
    print(zeze.nome)
    print(zeze.idade)
    for filhos in zeze.filhos:
        print(filhos.nome)
    zeze.sobrenome = 'Di Camargo'
    del zeze.filhos
    print(zeze.__dict__)
    print(guilherme.__dict__)

