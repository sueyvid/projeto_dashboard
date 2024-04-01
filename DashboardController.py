import tkinter as tk
from DashboardModel import DashboardModel
from DashboardView import DashboardView
from BancoDeDadosCarteira import BancoDadosCateira
from Widget import Widget
import datetime as dt

# To-do:
# [ ] Pegar a entrada de dados e adicionar no modelo e na TreeView
# [ ] Escrever os dados no banco de dados
# [ ] Atualizar a TreeView

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
        self._widgets = list()
        self._cria_widgets()
        for w in self._widgets:
            self.view.draw_basic_widget(w.width, w.height, w.x0, w.y0, w.x1, w.y1, w.widget_type, w.value)
        self._atualiza_relogio()

        self.view.botao1['command'] = self._processa_dados_bd
        self.view.root.bind('<Configure>', self._atualiza_widget)
        self.view.botao2['command'] = self.view.try_draw_entrada_dados
        # self.view.janela.protocol("WM_DELETE_WINDOW", self.view.on_closing_window)
        # formato de uma função lambda "lambda event: self._processa_dados_bd()""

        # combobox.bind('<<ComboboxSelected>>', callback)

    def _atualiza_relogio(self):
        now = dt.datetime.now()
        w = self._widgets[3]
        w.value = now.strftime('%H:%M:%S')
        self.view.draw_basic_widget(w.width, w.height, w.x0, w.y0, w.x1, w.y1, w.widget_type, w.value)
        self.view.root.after(1000, self._atualiza_relogio)

    def _cria_widgets(self):
        # armazena o tamanho da janela
        width = self.view.root.winfo_width()
        height = self.view.root.winfo_height()

        # widgets básicos
        for i in range(3):
            # instancia um widget
            w = Widget()
            self._widgets.append(w)
            i = self._widgets.index(w)

            # chama o calculate_position
            w.calculate_position(i, width, height)
        
        # Define os tipos e valores dos widgets
        self._widgets[0].widget_type = "Saldo"
        self._widgets[1].widget_type = "Entradas"
        self._widgets[2].widget_type = "Despesas"
        for w in self._widgets:
            w.value = "---"

        # widget de relógio
        time = dt.datetime.now()
        hour = time.hour
        minute = time.minute
        second = time.second
        w = Widget()
        self._widgets.append(w)
        index = self._widgets.index(w)
        w.calculate_position(index, width, height)
        w.widget_type = "Relógio"
        w.value = str(hour) + ":" + str(minute) + ":" + str(second)

    def _atualiza_widget(self, e):
        # armazena o tamanho da janela
        width = self.view.root.winfo_width()
        height = self.view.root.winfo_height()

        for w in self._widgets:
            w.calculate_position(self._widgets.index(w), width, height)
            self.view.draw_basic_widget(w.width, w.height, w.x0, w.y0, w.x1, w.y1, w.widget_type, w.value)

    def _processa_entrada_dados(self):
        pass

    def _escreve_dados_no_bd(self):
        pass

    def _atualiza_dados(self):
        pass

    def _processa_dados_bd(self):
        bd = BancoDadosCateira('Carteira1.csv')
        res = bd.todos()
        self.model.movimentacoes = res

        # width = self.view.root.winfo_width()
        entradas = 'R$ ' + str(self.model.ver_entradas()) + ',00'
        despesas = 'R$ ' + str(self.model.ver_despesas()) + ',00'
        saldo = 'R$ ' + str(self.model.ver_saldo()) + ',00'

        for w in self._widgets:
            if w.widget_type == "Saldo":
                w.value = saldo
            if w.widget_type == "Entradas":
                w.value = entradas
            if w.widget_type == "Despesas":
                w.value = despesas
            self.view.draw_basic_widget(w.width, w.height, w.x0, w.y0, w.x1, w.y1, w.widget_type, w.value)

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