# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Imports
import random 
from os import system, name

# Função para limar a tela a cada execução
def limpa_tela():
    # Windows
    if name  == 'nt':
        _= system('cls')
    # Mac ou linux
    else: 
        _= system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Hangman:
     
    # Método Construtor
    def __init__(self, palavra):

        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []
        self.letras_repetidas = []
        self.letra_repetida = False 
    
    # Metodo Advinha letra
    def guess(self,letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
            self.letra_repetida = False
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
            self.letra_repetida = False
        elif letra in (self.letras_erradas) or  letra in (self.letras_escolhidas):
            self.letras_repetidas.append(letra)
            self.letra_repetida = True
        else:
            return False
        return True
    
    # Metodo verifica jogo terminou
    def hangman_over(self):
        return self.hagman_won() or ((len(self.letras_erradas) + len(self.letras_repetidas)) == 6)
        
    # Método para verificar se o jogador venceu
    def hagman_won(self):
        if '_' not in self.hide_palavra():
            return True
        return False

	# Método para não mostrar a letra no board
    def hide_palavra(self):
		
        rtn = ''

        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += '_'
            else:
                rtn += letra
        return rtn
    
    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):

        print(board[len(self.letras_erradas)+len(self.letras_repetidas)])

        print('\nPalavra: ' + self.hide_palavra())

        print("\nLetras erradas:", ", ".join(self.letras_erradas))

        print("\nLetras corretas:", ", ".join(self.letras_escolhidas))

        if self.letra_repetida:  # Adicione este bloco
            print("\nEsta última letra que você inseriu é repetida!\n")

# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_palavra():
    # Ler palavras a partir do arquivo "palavras.txt"
    with open("palavras.txt", "r") as file:
        palavras = file.readlines()

    # Remove os caracteres de nova linha das palavras
    palavras = [palavra.strip() for palavra in palavras]

    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    return palavra

# Metodo para validar tentativa de letra
def tentativa_letra():
    # Validacao de letra se a entrada contém apenas letras
    while True:
        entrada = input("Digite uma letra: ")
        if entrada.isalpha():
            # A entrada contém apenas letras
            tentativa = entrada.lower() # Converte a letra para minúscula
            return tentativa
        else:
            # A entrada não contém apenas letras
            print("Digite apenas uma letra!")


# Método Main - Execução do Programa

def main():
    
    limpa_tela()

    # Cria o objeto e selecona aleatoriamente a palavra

    game = Hangman(rand_palavra())

    while not game.hangman_over():

        # Status do game
        game.print_game_status()

        # Recebe input do terminal
        user_input = tentativa_letra()

        # Verifica se a letra faz parte da palavra
        game.guess(user_input)

    # Imprimi status final do jogo
    game.print_game_status()

    if game.hagman_won():
        print('\nParabéns! Você Venceu!')

    else:
        print('\nGame over! Você perdeu.')
        print('\nA palavra era ' + game.palavra)
		
    print('\nFoi bom jogar com você! Volte sempre :) \n')

# Bloco Main para executar codigo
if __name__ == '__main__' :
    main()
