import tkinter as tk
from tkinter import ttk

# To-do:
# [ ] Widget de entrada de dados

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
        self.draw_entrada_dados()

    def draw_basic_widget(self, width, height, x0, y0, x1, y1, widget_type, value):
        tag = widget_type + "_value"
        self.canvas.delete(tag)
        self.canvas.create_rectangle((x0, y0), (x1, y1), fill='navy', tags=tag)
        self.canvas.create_text((x0+(width/2), y0+30), text=widget_type, fill='ghost white', font='Verdana 18', tags=tag)
        self.canvas.create_text((x0+(width/2), y0+100), text=value, fill='ghost white', font='Verdana 18', tags=tag)

    def draw_entrada_dados(self):
        self.janela = tk.Tk()

        frame_tv = tk.Frame(self.janela)
        frame_tv.grid(row=0, column=0)
        tv = ttk.Treeview(frame_tv)
        tv.grid(row=0, column=0)

        frame_entrada = tk.Frame(self.janela)
        frame_entrada.grid(row=1, column=0)
        tk.Label(frame_entrada, text="Título", font='Verdana 18').grid(row=0, column=0)
        tk.Label(frame_entrada, text="Data", font='Verdana 18').grid(row=1, column=0)
        tk.Label(frame_entrada, text="Valor", font='Verdana 18').grid(row=2, column=0)
        tk.Label(frame_entrada, text="Categoria", font='Verdana 18').grid(row=3, column=0)
        tk.Label(frame_entrada, text="Tipo", font='Verdana 18').grid(row=4, column=0)
        
        self.titulo = tk.StringVar()
        self.data = tk.StringVar()
        self.valor = tk.StringVar()
        self.categoria = tk.StringVar()
        self.tipo = tk.StringVar()

        titulo = tk.Entry(frame_entrada, font='Verdana 18', textvariable=self.titulo)
        titulo.grid(row=0, column=1)
        data = tk.Entry(frame_entrada, font='Verdana 18', textvariable=self.data)
        data.grid(row=1, column=1)
        valor = tk.Entry(frame_entrada, font='Verdana 18', textvariable=self.valor)
        valor.grid(row=2, column=1)

        categoria = ttk.Combobox(frame_entrada, font='Verdana 18', textvariable=self.categoria)
        categoria.grid(row=3, column=1)
        tipo = tk.Entry(frame_entrada, font='Verdana 18', textvariable=self.tipo)
        tipo.grid(row=4, column=1)

        botoes = tk.Frame(frame_entrada)
        botoes.grid(row=5, column=0, columnspan=2)
        botao = tk.Button(botoes, text="Adicionar")
        botao.grid(row=0, column=0)
        botao = tk.Button(botoes, text="Remover")
        botao.grid(row=0, column=1)
        botao = tk.Button(botoes, text="Alterar")
        botao.grid(row=0, column=2)

        # width = 300
        # height = 200
        # x0 = 10
        # y0 = 10
        # x1 = x0+width
        # y1 = y0+height
        # widget_type = "Entrada_dados"

        # tag = widget_type + "_value"
        # self.canvas.delete(tag)
        # self.canvas.create_rectangle((x0, y0), (x1, y1), fill='navy', tags=tag)
        # frame = tk.Frame(self.canvas)
        # frame.pack(expand=True, fill=tk.BOTH)

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