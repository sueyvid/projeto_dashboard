import pandas as pd
from Movimentacao import Movimentacao

class BancoDadosCateira:
    '''
    Representa um Banco de Dados com Pandas
    sobre movimentações em uma conta.

    Tem a capacidade de realizar vários
    tipos de consultas. 

    (Abstrai o uso de um Pandas.Dataframe).
    '''
    
    def __init__(self, nome_arq=None):
        '''
        Inicializa banco de dados a partir
        de um arquivo .csv
        '''

        self._df = None # dataframe Pandas encapsulado
        self._nome = '' # nome do arquivo do Banco de Dados

        if nome_arq:
            self.inicializa(nome_arq)
    
    def inicializa(self, nome_arq):
        '''
        Carrega banco de dados do arquivo,
        deixando-o pronto para buscas.
        '''

        try:
            print(f'Abrindo arquivo {nome_arq}')
            self._nome = nome_arq
            self._df = pd.read_csv(nome_arq)
        except FileNotFoundError as err:
            print(err)
            raise err # levanta exc. novamente para ser tratada em outro módulo
        else:
            ## altera tipo da coluna
            self._df.data = pd.to_datetime(self._df.data)
            # self._df.dt_publicacao = pd.to_datetime(self._df.dt_publicacao)
            # self._df.dt_trending = pd.to_datetime(self._df.dt_trending)

    def _df_para_lista(self, df):
        '''
        Converte Pandas.Dataframe para uma lista
        de tuplas (implementação com tempo de
        execução reduzido).
        Cada tupla na lista contém todos os dados
        de uma movimentação, cada um em uma string:
        (id_movimentacao, titulo, data, valor, categoria, tipo)
        '''
        
        res = [tup for tup in zip(df['id_movimentacao'], df['titulo'],
                                df['data'], df['valor'],
                                df['categoria'], df['tipo'])]
        return res
    
    def _df_para_movimentacoes(self, df):
        '''
        Converte Pandas.Dataframe para uma lista
        de Movimentacoes.
        '''
        lista = self._df_para_lista(df)
        return [Movimentacao(t) for t in lista]

    @property
    def nome(self):
        '''
        Retorna o nome
        do arquivo do 
        banco de dados.
        '''
        return self._nome

    @property
    def categorias(self):
        '''
        Retorna uma lista de strings
        contendo as categorias de movimentações
        no banco de dados.
        '''
        return list(self._df.categoria.unique())
    
    @property
    def total(self):
        '''
        Retorna a quantidade
        de movimentações no banco de dados.
        '''
        return len(self._df)

    def imprime_info(self):
        '''
        Imprime informações sobre o
        banco de dados.
        '''

        print(f'Arquivo: {self.nome}')
        print(f'Possui dados de movimentações em uma conta bancária')
        print(f'Total de movimentações: {self.total}')
        print(f'Período: {self._df.data.min()} até {self._df.data.max()}')
        print(f'Dados das movimentações:')
        for c in self._df.columns.to_list():
            print(c, end=', ')
        print('\n')

    def todos(self):
        '''
        Retorna lista de Movimentações
        com dados de todo o Banco de Dados.
        '''
        return self._df_para_movimentacoes(self._df)

    def busca_por_titulo(self, t):
        '''
        Retorna lista de Movimentações
        com resultados de busca por título.
        '''
        print(f'Busca por título: {t}')
        df = self._df[self._df.titulo.str.contains(t, case=False)]
        return self._df_para_movimentacoes(df)
    
    def busca_por_tipo(self, c):
        '''
        Retorna lista de Movimentações
        com resultados de busca por tipo.
        '''
        print(f'Busca por tipo: {c}')
        df = self._df[self._df.tipo.str.contains(c, case=False)]
        return self._df_para_movimentacoes(df)
    
    def busca_por_categoria(self, c):
        '''
        Retorna lista de Movimentações
        com resultados de busca por categoria.
        '''
        print(f'Busca por categoria: {c}')
        df = self._df[self._df.categoria.str.contains(c, case=False)]
        return self._df_para_movimentacoes(df)
    
    def busca_por_periodo(self, ini, fim):
        '''
        Retorna lista de Movimentações
        com resultados de busca por período.
        '''
        print(f'Busca por período: {ini}, {fim}')
        mascara = (self._df.data.dt.date >= pd.to_datetime(ini)) & (self._df.data.dt.date <= pd.to_datetime(fim))
        df = self._df[mascara]
        return self._df_para_movimentacoes(df)

    # def mostra_mais_assistidos(self, n=10):
    #     '''
    #     Exibe gráfico de barras com
    #     os n vídeos mais assistidos.
    #     '''
    #     df_top_videos = self._df.sort_values(by=['cont_views'], ascending=False).head(n)
    #     graficos.grafico_barras(df_top_videos, 'titulo',
    #                                            'cont_views',
    #                                            'Título',
    #                                            'Views')

    # def mostra_mais_likes(self, n=10):
    #     '''
    #     Exibe gráfico de barras com
    #     os n vídeos com mais likes.
    #     '''
    #     df_top_videos = self._df.sort_values(by=['likes'], ascending=False).head(n)
    #     graficos.grafico_barras(df_top_videos, 'titulo',
    #                                            'likes',
    #                                            'Título',
    #                                            'Likes')

    # def mostra_mais_comentarios(self, n=10):
    #     '''
    #     Exibe gráfico de barras com
    #     os n vídeos com mais comentários.
    #     '''
    #     df_top_videos = self._df.sort_values(by=['cont_comentarios'], ascending=False).head(n)
    #     graficos.grafico_barras(df_top_videos, 'titulo',
    #                                            'cont_comentarios',
    #                                            'Título',
    #                                            'Comentários')
        
def imprime_resultado(res):
    '''
    Função auxiliar para imprimir o resultado
    de uma busca no BancoDadosCateira.
    '''
    for v in res:
        print(v)

def main():
    bd = BancoDadosCateira('Carteira1.csv')
    #bd.imprime_info()
    print(f'Arquivo: {bd.nome}')
    print(f'Total de movimentações: {bd.total}')
    print(f'Categorias no banco de dados: {bd.categorias}')
    
    #res = bd.busca_por_titulo('fla')
    #res = bd.busca_por_tipo('espor')
    #res = bd.busca_por_categoria('SPORTS')
    res = bd.busca_por_periodo('2023-11-01', '2024-11-30')

    print('\nResultado da busca:')
    imprime_resultado(res)

    #bd.mostra_mais_assistidos()
    #bd.mostra_mais_likes()
    #bd.mostra_mais_comentarios()

if __name__ == '__main__':
    main()