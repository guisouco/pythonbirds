class Pessoa:
    olhos = 2

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
    zeze.olhos = 4
    del zeze.olhos
    print(zeze.__dict__)
    print(guilherme.__dict__)
    Pessoa.olhos = 4
    print(Pessoa.olhos)
    print(zeze.olhos)
    print(guilherme.olhos)
    print(id(Pessoa.olhos), id(zeze.olhos), id(guilherme.olhos))



