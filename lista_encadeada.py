from no import No

class ListaEncadeada:
    
    def __init__(self):
        self.cabeca = None
        self._tamanho = 0
    
    def adicionar(self, elemento):
        if self.cabeca:
            ponteiro = self.cabeca
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = No(elemento)
        else:
            self.cabeca = No(elemento)
        self._tamanho += 1

    def __len__(self):
        return self._tamanho

    def _getno(self, indice):
        ponteiro = self.cabeca
        for i in range(indice):
            if ponteiro:
                ponteiro = ponteiro.proximo
            else:
                raise IndexError('índice da lista fora de alcance')
        return ponteiro

    def __getitem__(self, indice):
        ponteiro = self._getno(indice)
        if ponteiro:
            return ponteiro.dado
        else:
            raise IndexError('índice da lista fora de alcance')

    def __setitem__(self, indice, elemento):
        ponteiro = self._getno(indice)
        if ponteiro:
            ponteiro.dado = elemento
        else:
            raise IndexError('índice da lista fora de alcance')
    
    def indice(self, elemento):
        ponteiro = self.cabeca
        i = 0
        while(ponteiro):
            if ponteiro.dado == elemento:
                return i
            ponteiro = ponteiro.proximo
            i += 1
        raise ValueError(f'{elemento} não foi encontado na lista')

    def inserir(self, indice, elemento):
        no = No(elemento)
        if indice == 0:
            no.proximo = self.cabeca
            self.cabeca = no
        else:
            ponteiro = self._getno(indice - 1)
            no.proximo = ponteiro.proximo
            ponteiro.proximo = no
        self._tamanho += 1

    def remover(self, elemento):
        if self.cabeca == None:
            raise ValueError(f'{elemento} não foi encontado na lista')
        elif self.cabeca.dado == elemento:
            self.cabeca = self.cabeca.proximo
            self._tamanho -= 1
            return True
        else:
            antecessor = self.cabeca
            ponteiro = self.cabeca.proximo
            while(ponteiro):
                if ponteiro.dado == elemento:
                    antecessor.proximo = ponteiro.proximo
                    ponteiro.proximo = None
                    self._tamanho -= 1
                    return True
                antecessor = ponteiro
                ponteiro = ponteiro.proximo
        raise ValueError(f'{elemento} não foi encontado na lista')

    def contar(self, elemento):
        c = 0
        ponteiro = self.cabeca
        while (ponteiro):
            if ponteiro.dado == elemento:
                c += 1
            ponteiro = ponteiro.proximo
        return c

    def deletar(self):
        while (self.cabeca):
            if self.cabeca == None:
                raise ValueError('A lista está vazia!')
            elif self.cabeca.dado:
                self.cabeca.proximo = self.cabeca
                self.cabeca = None
        self._tamanho = 0

    def __repr__(self):
        r = ''
        s = 'Fim!'
        ponteiro = self.cabeca
        while(ponteiro):
            r += str(ponteiro.dado) + ' -> '
            ponteiro = ponteiro.proximo
        t = r + s
        if r != '':
            return t
        else:
            return 'A lista está vazia!'

    def __str__(self):
        return self.__repr__()
