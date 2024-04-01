import tkinter as tk
from tkinter import ttk

# To-do:
# [x] Configurar a entrada de dados
# [x] Terminar o desenho da entrada de dados
# [x] Configurar os headers da TreeView

class DashboardView:
    '''View: interface gráfica Tkinter para dashboard'''

    def __init__(self, root):
        self.root = root # widget mestre
        # self.janela = tk.Tk()
        # self.janela.destroy()
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

        # botão de manipular dados
        self.botao2 = tk.Button(frame2, text="Manipular dados", font=('Verdana', 12))
        self.botao2.pack(anchor='ne', padx=10, pady=10, side=tk.RIGHT)

        # botão de atualizar dados
        self.botao1 = tk.Button(frame2, text="Atualizar dados", font=('Verdana', 12))
        self.botao1.pack(anchor='ne', padx=10, pady=10, side=tk.RIGHT)

        self.state_entrada_dados = 0

        # # frame com grupo de frames
        # frame2 = tk.Frame(frame1, bg='gray3')
        # frame2.pack(expand=True, fill=tk.BOTH)

        # canvas interno
        self.canvas = tk.Canvas(frame1, bg='gray3')
        self.canvas.pack(anchor=tk.CENTER, expand=True, fill=tk.BOTH)

        # self._saldo(frame2, 0, 0)
        # self.draw_entrada_dados()

    def draw_basic_widget(self, width, height, x0, y0, x1, y1, widget_type, value):
        tag = widget_type + "_value"
        self.canvas.delete(tag)
        self.canvas.create_rectangle((x0, y0), (x1, y1), fill='navy', tags=tag)
        self.canvas.create_text((x0+(width/2), y0+30), text=widget_type, fill='ghost white', font='Verdana 18', tags=tag)
        self.canvas.create_text((x0+(width/2), y0+100), text=value, fill='ghost white', font='Verdana 18', tags=tag)

    def _configura_entrada_dados(self):
        pass

    def _configura_tv(self):
        pass

    def tv_add(self, values):
        self.tv.insert('', tk.END, values=(values[0], values[1], values[2], values[3], values[4], values[5]))

    def tv_remove(self):
        if not self.tv.selection():
            raise IndexError()
        for selected_item in self.tv.selection():
            self.tv.delete(selected_item)

    def tv_atualiza(self, values):
        if len(self.tv.selection()) > 1:
            raise IndexError()
        if len(self.tv.selection()) == 1:
            for selected_item in self.tv.selection():
                index = self.tv.index(selected_item)
                self.tv.delete(selected_item)
                self.tv.insert('', index, values=(values[0], values[1], values[2], values[3], values[4], values[5]))

    def _on_closing_window(self):
        self.state_entrada_dados = 0
        self.janela.destroy()

    def try_draw_entrada_dados(self, categorias=('value1', 'value2', 'value3')):
        try:
            self.draw_entrada_dados(categorias)
        except PermissionError as error:
            print(error)
        except:
            print("Deu ruim!")

    def draw_entrada_dados(self, categorias=('value1', 'value2', 'value3')):
        if self.state_entrada_dados == 1:
            raise PermissionError("A janela já existe")
        
        # Janela da entrada de dados
        self.janela = tk.Tk()
        self.exit_button = tk.Button(self.janela, text="Sair", command=self._on_closing_window)
        self.exit_button.pack()
        self.janela.protocol("WM_DELETE_WINDOW", self._on_closing_window)

        # Frame da TreeView
        frame_tv = tk.Frame(self.janela)
        frame_tv.pack()
        self.tv = ttk.Treeview(frame_tv, show="headings")
        self.tv.grid(row=0, column=0)

        # Configura TreeView
        columns = ('id', 'titulo', 'data', 'valor', 'categoria', 'tipo')
        self.tv['columns'] = columns
        self.tv.heading('id', text='ID')
        self.tv.heading('titulo', text='Título')
        self.tv.heading('data', text='Data')
        self.tv.heading('valor', text='Valor')
        self.tv.heading('categoria', text='Categoria')
        self.tv.heading('tipo', text='Tipo')

        self.tv.column('id', width=50, anchor=tk.W)
        self.tv.column('titulo', width=200, anchor=tk.W)
        self.tv.column('data', width=100, anchor=tk.W)
        self.tv.column('valor', width=100, anchor=tk.W)
        self.tv.column('categoria', width=100, anchor=tk.W)
        self.tv.column('tipo', width=100, anchor=tk.W)

        # Configura entrada de dados        
        self.titulo = tk.StringVar()
        self.data = tk.StringVar()
        self.valor = tk.StringVar()
        self.categoria = tk.StringVar()
        self.tipo = tk.StringVar()

        # Frame da entrada de dados
        frame_entrada = tk.Frame(self.janela)
        frame_entrada.pack()
        tk.Label(frame_entrada, text="Título", font='Verdana 18').grid(row=0, column=0)
        tk.Label(frame_entrada, text="Data", font='Verdana 18').grid(row=1, column=0)
        tk.Label(frame_entrada, text="Valor", font='Verdana 18').grid(row=2, column=0)
        tk.Label(frame_entrada, text="Categoria", font='Verdana 18').grid(row=3, column=0)
        tk.Label(frame_entrada, text="Tipo", font='Verdana 18').grid(row=4, column=0)

        titulo = tk.Entry(frame_entrada, font='Verdana 18', textvariable=self.titulo)
        titulo.grid(sticky='WE', row=0, column=1)
        data = tk.Entry(frame_entrada, font='Verdana 18', textvariable=self.data)
        data.grid(sticky='WE', row=1, column=1)
        valor = tk.Entry(frame_entrada, font='Verdana 18', textvariable=self.valor)
        valor.grid(sticky='WE', row=2, column=1)
        categoria = ttk.Combobox(frame_entrada, font='Verdana 18', textvariable=self.categoria)
        categoria.grid(sticky='WE', row=3, column=1)
        frame_rb = tk.Frame(frame_entrada)
        frame_rb.grid(sticky='WE', row=4, column=1)

        # Configra Combobox
        categoria['values'] = categorias

        # Configura Radiobutton
        types = (('Entrada', 'entrada'),
                 ('Saída Fixa', 'saida_fixa'),
                 ('Saída Variável', 'saida_variavel'))
        for type in types:
            rb = ttk.Radiobutton(frame_rb, text=type[0], value=type[1], variable=self.tipo)
            rb.pack(fill='x', padx=5, pady=5)

        # Frame dos botões
        botoes = tk.Frame(frame_entrada)
        botoes.grid(row=5, column=0, columnspan=2)
        botao = tk.Button(botoes, text="Adicionar")
        botao.grid(row=0, column=0)
        botao = tk.Button(botoes, text="Remover")
        botao.grid(row=0, column=1)
        botao = tk.Button(botoes, text="Alterar")
        botao.grid(row=0, column=2)

        self.state_entrada_dados = 1

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