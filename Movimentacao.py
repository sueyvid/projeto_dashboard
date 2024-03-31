class Movimentacao:
    '''
    Representa uma movimentação.
    '''
    
    def __init__(self, dados):
        self._id_movimentacao = dados[0] #id_movimentacao
        self._titulo = dados[1] #titulo
        self._data = dados[2] #data
        self._valor = dados[3] #valor
        self._categoria = dados[4] #categoria
        self._tipo = dados[5] #tipo
    
    @property
    def id_movimentacao(self):
        '''
        Retorna identificador
        da movimentação.
        '''
        return self._id_movimentacao

    @property
    def titulo(self):
        '''
        Retorna título
        da movimentação.
        '''
        return self._titulo

    @property
    def data(self):
        '''
        Retorna data
        da movimentação.
        '''
        return self._data

    @property
    def valor(self):
        '''
        Retorna o valor
        da movimentação.
        '''
        return self._valor

    @property
    def categoria(self):
        '''
        Retorna categoria
        do vídeo.
        '''
        return self._categoria

    @property
    def tipo(self):
        '''
        Retorna o tipo
        da movimentação.
        '''
        return self._tipo

    def __str__(self):
        s = f'Título: {self.titulo}\n'
        s += f'Categoria: {self.categoria}\n'
        s += f'Valor: {self.valor}\n'
        s += f'Tipo: {self.tipo}\n'
        s += f'Movimentação em {self.data.day}/{self.data.month}/{self.data.year}\n'
        s += '----------------------------------------------'
        return s
    
    def __repr__(self):
        return f'Movimentação{self.id_video}'