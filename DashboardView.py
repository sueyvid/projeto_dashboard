import tkinter as tk

class DashboardView:
    '''View: interface gráfica Tkinter para dashboard'''

    def __init__(self, root):
        self.root = root # widget mestre

        self._inicializa_gui()
        self._configura_widgets()

    def _configura_widgets(self):
        self.label1['font'] = ('Verdana', 18, 'bold')
        self.label1['fg'] = 'ghost white'

    def _inicializa_gui(self):
        # frame interno
        frame1 = tk.Frame(self.root, bg='navy')
        frame1.pack(expand=True, fill=tk.BOTH)

        # frame do cabeçalho
        frame2 = tk.Frame(frame1, bg='navy')
        frame2.pack(fill=tk.BOTH)

        # nome do frame
        self.label1 = tk.Label(frame2, text="Dashboard Finanças Pessoais", bg='navy')
        self.label1.pack(anchor='nw', padx=10, pady=10, side=tk.LEFT)

        # botão de atualizar dados
        self.botao1 = tk.Button(frame2, text="Atualizar dados", font=('Verdana', 12))
        self.botao1.pack(anchor='ne', padx=10, pady=10)

        # # frame com grupo de frames
        # frame2 = tk.Frame(frame1, bg='gray3')
        # frame2.pack(expand=True, fill=tk.BOTH)

        # canvas interno
        self.canvas = tk.Canvas(frame1, bg='gray3')
        self.canvas.pack(anchor=tk.CENTER, expand=True, fill=tk.BOTH)

        # self._saldo(frame2, 0, 0)

        self._basic_widget(10, 10, "Saldo", "R$ 100,00")
        self._basic_widget(320, 10, "Entradas", "R$ 300,00")
        self._basic_widget(630, 10, "Despesas", "R$ 200,00")

    def _basic_widget(self, pos_x: int, pos_y: int, type: str, value: str):
        rect = {'width': 300, 'height': 200, 'pos_x0': pos_x, 'pos_y0': pos_y, 'pos_x1': None, 'pos_y1': None}
        rect['pos_x1'] = rect['pos_x0']+rect['width']
        rect['pos_y1'] = rect['pos_y0']+rect['height']

        tag = type + "_value"
        self.canvas.delete(tag)
        self.canvas.create_rectangle((rect['pos_x0'], rect['pos_y0']), (rect['pos_x1'], rect['pos_y1']), fill='navy', tags=tag)
        self.canvas.create_text((rect['pos_x0']+150, rect['pos_y0']+30), text=type, fill='ghost white', font='Verdana 18', tags=tag)
        self.canvas.create_text((rect['pos_x0']+150, rect['pos_y0']+100), text=value, fill='ghost white', font='Verdana 18', tags=tag)

    def atualiza_valores(self, type, value):
        if type == 'Saldo':
            self._basic_widget(10, 10, type, value)
        if type == 'Entradas':
            self._basic_widget(320, 10, type, value)
        if type == 'Despesas':
            self._basic_widget(630, 10, type, value)

def main():
    # cria janela principal Tk apenas para teste
    root = tk.Tk()
    root.geometry('1280x720')
    root.title('Teste GUI')

    # instancia o view
    v = DashboardView(root)

    # inicializa aplicação Tk -> a janela deve aparecer,
    # mas não deve reagir aos eventos
    tk.mainloop()

if __name__ == "__main__":
    main()