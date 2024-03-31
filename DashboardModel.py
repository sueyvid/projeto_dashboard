from Movimentacao import Movimentacao
from BancoDeDadosCarteira import BancoDadosCateira

class DashboardModel:
    '''Modelo: calcula infos da conta bancária'''

    def __init__(self):
        self._movimentacoes = None

    @property
    def movimentacoes(self):
        return self._movimentacoes
    
    @movimentacoes.setter
    def movimentacoes(self, list):
        self._movimentacoes = list

    def ver_entradas(self):
        total = 0
        for movement in self._movimentacoes:
            if movement.tipo == 'entrada':
                total += movement.valor
        return total
    
    def ver_despesas(self):
        total = 0
        for movement in self._movimentacoes:
            if movement.tipo == 'saida_variavel' or movement.tipo == 'saida':
                total += movement.valor
        return total

    def ver_saldo(self):
        ent = self.ver_entradas()
        des = self.ver_despesas()
        return ent - des

def main():
    m = DashboardModel()
    bd = BancoDadosCateira('Carteira1.csv')
    res = bd.todos()
    m.movimentacoes = res
    print('Entradas: ' + str(m.ver_entradas()))
    print('Despesas: ' + str(m.ver_despesas()))
    print('Saldo: ' + str(m.ver_saldo()))

if __name__ == '__main__':
    main()