import tkinter as tk
from DashboardModel import DashboardModel
from DashboardView import DashboardView
from BancoDeDadosCarteira import BancoDadosCateira

class DashboardController:
    '''
    Controlador: informa ao Modelo as operações a serem realizadas
    e recupera o resultado para atualizar o View.
    É o objeto aplicação de fato; aquele que controla as ações.
    '''

    def __init__(self):
        self.model = None # inicialmente o controlador não tem view e nem model associados
        self.view = None

        # cria janela principal Tk apenas para teste
        self.root = tk.Tk()
        self.root.title('Dashboard Finceiro Pessoal')
        self.root.geometry('1280x720')

    def inicializa(self, model, view):
        '''
        Método faz parte da interface pública: atribui view e model
        e em seguida, configura o controlador com o view e model.
        '''
        self.model = model
        self.view = view
        self._configura()

    def _configura(self):
        self.view.botao1['command'] = self._processa_entrada

    def _processa_entrada(self):
        bd = BancoDadosCateira('Carteira1.csv')
        res = bd.todos()
        self.model.movimentacoes = res
        entradas = 'R$ ' + str(self.model.ver_entradas()) + ',00'
        despesas = 'R$ ' + str(self.model.ver_despesas()) + ',00'
        saldo = 'R$ ' + str(self.model.ver_saldo()) + ',00'
        self.view.atualiza_valores('Saldo', saldo)
        self.view.atualiza_valores('Entradas', entradas)
        self.view.atualiza_valores('Despesas', despesas)

    def executa(self):
        '''Método principal da interface pública da classe.'''
        tk.mainloop()


def main():
    # cria controller
    controller = DashboardController()

    # cria modelo
    model = DashboardModel()

    # cria view
    view = DashboardView(controller.root)

    # chama os métodos necessários do controller
    # para inicar a aplicação
    controller.inicializa(model, view)
    controller.executa()
                
if __name__ == "__main__":
    main()