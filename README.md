# Jogo da Forca (Hangman)

Este projeto é uma implementação do popular jogo da forca (Hangman) usando Python e programação orientada a objetos. O jogo seleciona aleatoriamente uma palavra de um arquivo de texto e o jogador deve adivinhar a palavra, letra por letra.

## Código

O código é dividido em várias funções e uma classe `Hangman` que encapsula a lógica do jogo. A classe possui os seguintes métodos:

- `__init__`: Construtor da classe, inicializa os atributos necessários.
- `guess`: Método para verificar se a letra adivinhada pelo jogador está correta, incorreta ou repetida.
- `hangman_over`: Verifica se o jogo terminou (se o jogador ganhou ou perdeu).
- `hangman_won`: Verifica se o jogador ganhou o jogo.
- `hide_palavra`: Oculta as letras não adivinhadas da palavra.
- `print_game_status`: Imprime o status atual do jogo, incluindo o tabuleiro, letras erradas e corretas.

O código também inclui funções auxiliares fora da classe:

- `limpa_tela`: Limpa a tela do terminal para manter a saída organizada.
- `rand_palavra`: Seleciona uma palavra aleatória do arquivo de texto.
- `tentativa_letra`: Solicita ao usuário que insira uma letra e valida a entrada.

## Como jogar

1. Certifique-se de ter Python instalado em seu sistema.
2. Crie um arquivo chamado `palavras.txt` no mesmo diretório do script. Adicione várias palavras em linhas separadas neste arquivo.
3. Execute o script Python no terminal (`python nome_do_arquivo.py`).
4. O jogo exibirá o tabuleiro e solicitará que o jogador insira uma letra.
5. Continue inserindo letras até que o jogo termine (você ganhe ou perca).

## Regras

- O jogador pode inserir apenas uma letra de cada vez.
- Se a letra já foi inserida anteriormente, o programa informará que a letra é repetida.
- O jogador tem 6 tentativas (erros) antes de perder o jogo.

Divirta-se jogando o Jogo da Forca!

# Direitos de Uso
Este repositório têm como objetivo apresentar meus projeto do **LAB 04 do Curso de Python da DSA**. Então, dentro deste repositório você pode utilizar deste conteúdo sem nenhuma restrição contanto que não me responsebilize por eventuais causas ou danos morais perante minha responsabilidade.	

Exigido | Permitido | Proibido
:---: | :---: | :---:
Aviso de licença e direitos autorais | Uso comercial | Responsabilidade Assegurada
 || Modificação ||	
 || Distribuição ||	
 || Sublicenciamento || 
 