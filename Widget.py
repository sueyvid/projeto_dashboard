class Widget:
    '''
    Representa um Widget.
    '''
    def __init__(self):
        # Geometria
        self._width = None
        self._height = None
        self._x0 = None
        self._y0 = None
        self._x1 = None
        self._y1 = None

        # Infos
        self._type = None
        self._value = None

    @property
    def width(self):
        '''
        Retorna a largura
        do Widget.
        '''
        return self._width
    
    @property
    def height(self):
        '''
        Retorna a altura
        do Widget.
        '''
        return self._height
    
    @property
    def x0(self):
        '''
        Retorna a posição
        x0 do Widget.
        '''
        return self._x0
    
    @property
    def y0(self):
        '''
        Retorna a posição
        y0 do Widget.
        '''
        return self._y0
    
    @property
    def x1(self):
        '''
        Retorna a posição
        x1 do Widget.
        '''
        return self._x1
    
    @property
    def y1(self):
        '''
        Retorna a posição
        y1 do Widget.
        '''
        return self._y1
    
    @property
    def widget_type(self):
        '''
        Retorna o tipo
        do Widget.
        '''
        return self._type
    
    @widget_type.setter
    def widget_type(self, type):
        '''
        Define o tipo
        do Widget
        '''
        self._type = type
  
    @property
    def value(self):
        '''
        Retorna o valor
        do Widget.
        '''
        return self._value
    
    @value.setter
    def value(self, value):
        '''
        Define o valor
        do Widget.
        '''
        self._value = value

    def calculate_position(self, index, width, height): # não variando o tamanho dos widgets
        # tamanho do widget
        x_expand = 1

        # encontrar a posição através do índice
        x = index % 3
        y = index // 3

        # tratamento de erro
        if width == 1:
            width = 1280
        if height == 1:
            height = 720

        # definir posição em pixels do widget
        x0 = x*width/3 + 10
        y0 = y*height/3 + 10

        # definir o tamanho em pixels do widget através dos parâmetros de tamanho
        width_px = x_expand*(width/3) - 20
        height_px = 200

        # Atribuir valores
        self._width = width_px
        self._height = height_px
        self._x0 = x0
        self._y0 = y0
        self._x1 = self._width + self._x0
        self._y1 = self._height + self._y0

        
