import tkinter as tk

class DashboardView:
    '''View: interface gráfica Tkinter para dashboard'''

    def __init__(self, root):
        self.root = root # widget mestre
        # self.root.overrideredirect(True)

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

    def draw_basic_widget(self, width, height, x0, y0, x1, y1, widget_type, value):
        tag = widget_type + "_value"
        self.canvas.delete(tag)
        self.canvas.create_rectangle((x0, y0), (x1, y1), fill='navy', tags=tag)
        self.canvas.create_text((x0+(width/2), y0+30), text=widget_type, fill='ghost white', font='Verdana 18', tags=tag)
        self.canvas.create_text((x0+(width/2), y0+100), text=value, fill='ghost white', font='Verdana 18', tags=tag)

    # def draw_clock_widget(self, width, height, x0, y0, x1, y1, widget_type, value):
    #     tag = widget_type + "_value"
    #     self.canvas.delete(tag)
    #     self.canvas.create_rectangle((x0, y0), (x1, y1), fill='navy', tags=tag)
    #     self.canvas.create_text((x0+(width/2), y0+30), text=widget_type, fill='ghost white', font='Verdana 18', tags=tag)
    #     self.canvas.create_text((x0+(width/2), y0+100), text=value, fill='ghost white', font='Verdana 18', tags=tag)

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