class BancoDeDados:
    '''Cria um arquivo chamado movimentacoes.txt que pode ser manipulado pelos métodos da Classe.'''

    def __init__(self):
        self.arq = "movimentacoes.txt"
        self._inicializa("")

    def _inicializa(self, dados: str):
        '''Método privado para criar o arquivo vazio.'''

        with open(self.arq, "w") as arquivo:
            arquivo.write(dados)

    def read(self) -> str:
        '''Lê o arquivo retornando uma string.'''

        with open(self.arq, "r") as arquivo:
            dados = arquivo.read()
        return dados
    
    def write(self, dados: str):
        '''Reescreve o arquivo, recebe uma string ou uma lista de strings.'''

        if type(dados) == str:
            with open(self.arq, "w") as arquivo:
                arquivo.write(dados)
                arquivo.write("\n")
        if type(dados) == list:
            result = self._convert_list_to_str(dados)
            with open(self.arq, "w") as arquivo:
                arquivo.write(result)

    def append(self, dados: str):
        '''Adiciona uma nova linha ao arquivo, recebe uma string ou uma lista de strings.'''

        if type(dados) == str:
            with open(self.arq, "a") as arquivo:
                arquivo.write(dados)
                arquivo.write("\n")
        if type(dados) == list:
            result = self._convert_list_to_str(dados)
            with open(self.arq, "a") as arquivo:
                arquivo.write(result)

    def _convert_list_to_str(self, dados: list) -> str:
        '''Converte uma lista em string.'''

        text = ""
        for linha in dados:
            text += linha + "\n"
        return text
    
def main():
    b = BancoDeDados()
    
    # dados = "Linha 1\nLinha 2\nLinha 3"
    # b.write(dados)

    dados = ["Linha 1", "Linha 2", "Linha 3"]
    # b.append(dados)
    b.write(dados)
    b.append("Linha 4")
    b.append("Linha 5")

    print(b.read())

if __name__ == "__main__":
    main()