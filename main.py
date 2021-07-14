from jokenpo import Jogo
from load_inicial import showTitleScreen
from time import sleep

showTitleScreen()

print('Bem vindo ao Menu de Opções!')
sleep(0.5)
print('''
[ 1 ] Iniciar Jogo
[ 2 ] Regras
[ 3 ] Conquistas
[ 4 ] Sair
''')

nome_jogador = str(input('Digite seu nome: '))
jogador = Jogo(nome_jogador)

while True:
    op = int(input('Digite sua escolha: '))

    if op == 1:
        sleep(0.5)
        print('Olá você está prestes a enfrentar "O Mãozinha" da família Adams!')
        sleep(0.5)
        print('Iniciando Jogo')
        sleep(0.5)
        print('Boa Sorte... Você vai precisar!')
        jogador.jogo()

    elif op == 2:
        print('''
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* 
*                               Regras do jogo                                *
*  No Jankenpon, os jogadores devem simultaneamente esticar a mão,            *
*  na qual cada um formou um símbolo (que significa pedra, papel ou tesoura). *
*  Então, os jogadores comparam os símbolos da seguinte forma:                * 
*                                                                             *          
*               Pedra ganha da tesoura (amassando-a ou quebrando-a).          *
*                      Tesoura ganha do papel (cortando-o).                   *  
*                       Papel ganha de pedra (enrolando-a).                   *
*                                                                             * 
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* 
        ''')

    elif op == 3:
        jogador.conquistas()

    elif op == 4:
        print('Obrigado por Jogar.')
        break

    else:
        print('Opção inválida')
