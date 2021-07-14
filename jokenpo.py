from lista_encadeada import ListaEncadeada
from premios import premioF, premioM, premioD, premioEspecialFacil, \
    premioEspecialMedio, premioEspecialDificil, premioGeral
from jogadas import *
from random import randint
from time import sleep

qtd_vit_erro = ListaEncadeada()
jogada = ListaEncadeada()
pontuacao = 0

class Jogo(ListaEncadeada):

    global qtd_vit_erro
    global jogada

    def __init__(self, jogador):
        super().__init__()
        self.jogador = jogador

    def jogo(self):
        print('''Suas opcões:
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
*                                 *
*      [0] Pedra                  *
*      [1] Papel                  *
*      [2] Tesoura                *
*      [3] Sair                   *
*                                 *
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
''')
        global pontuacao
        while True:
            print('''
            *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            *    Selecione sua dificuldade    *
            *                                 *
            *           [1] Fácil             *
            *           [2] Média             *
            *           [3] Difícil           *
            *                                 *
            *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
            ''')
            escolha = int(input('Digite sua escolha: '))
            if escolha == 1 or escolha == 2 or escolha == 3:
                if escolha == 1:
                    sleep(0.5)
                    print('Você escolheu a modalidade FÁCIL e pode perder até 5 vezes!')
                elif escolha == 2:
                    sleep(0.5)
                    print('Você escolheu a modalidade MÉDIO e pode perder até 3 vezes!')
                elif escolha == 3:
                    sleep(0.5)
                    print('Você escolheu a modalidade DIFÍCIL e pode perder apenas 1 vez!')

                for i in range(1, 11):
                    num = str(i) + 'ª jogada'
                    print(num)
                    sleep(0.5)
                    jogada.adicionar(num)
                    com = randint(0, 2)
                    jog = int(input('CHOOSE YOUR DESTINY: '))
                    if jog == 3:
                        print('O jogador desistiu')
                        break
                    print('JO')
                    sleep(0.5)
                    print('KEN')
                    sleep(0.5)
                    print('PÔ')
                    sleep(0.5)

                    # Empate
                    if com == jog:
                        if com == 0 and jog == 0:
                            print('Você empatou')
                            empate_pedra_x_pedra()
                            pontuacao += 5
                        elif com == 1 and jog == 1:
                            print('Você empatou')
                            empate_papel_x_papel()
                            pontuacao += 5
                        elif com == 2 and jog == 2:
                            print('Você empatou')
                            empate_tesoura_x_tesoura()
                            pontuacao += 5

                    # Vitória
                    elif com == 0 and jog == 1:
                        print('Você ganhou essa jogada!')
                        vitoria_papel_x_pedra()
                        qtd_vit_erro.adicionar('ok')
                        print('Parabéns!'
                              'Aqui está o seu prêmio')
                        if escolha == 1:
                            premioF(i)
                            pontuacao += 10
                        elif escolha == 2:
                            premioM(i)
                            pontuacao += 10
                        elif escolha == 3:
                            premioD(i)
                            pontuacao += 10

                        if escolha == 1 and qtd_vit_erro.contar('ok') == 10:
                            premioEspecialFacil()
                        elif escolha == 2 and qtd_vit_erro.contar('ok') == 10:
                            premioEspecialMedio()
                        elif escolha == 3 and qtd_vit_erro.contar('ok') == 10:
                            premioEspecialDificil()

                        if pontuacao == 300:
                            premioGeral()

                    elif com == 1 and jog == 2:
                        print('Você ganhou essa jogada!')
                        vitoria_tesoura_x_papel()
                        qtd_vit_erro.adicionar('ok')
                        print('Parabéns!'
                              'Aqui está o seu prêmio')
                        if escolha == 1:
                            premioF(i)
                            pontuacao += 10
                        elif escolha == 2:
                            premioM(i)
                            pontuacao += 10
                        elif escolha == 3:
                            premioD(i)
                            pontuacao += 10

                        if escolha == 1 and qtd_vit_erro.contar('ok') == 10:
                            premioEspecialFacil()
                        elif escolha == 2 and qtd_vit_erro.contar('ok') == 10:
                            premioEspecialMedio()
                        elif escolha == 3 and qtd_vit_erro.contar('ok') == 10:
                            premioEspecialDificil()

                        if pontuacao == 300:
                            premioGeral()

                    elif com == 2 and jog == 0:
                        print('Você ganhou essa jogada!')
                        vitoria_pedra_x_tesoura()
                        qtd_vit_erro.adicionar('ok')
                        print('Parabéns!'
                              'Aqui está o seu prêmio')
                        if escolha == 1:
                            premioF(i)
                            pontuacao += 10
                        elif escolha == 2:
                            premioM(i)
                            pontuacao += 10
                        elif escolha == 3:
                            premioD(i)
                            pontuacao += 10

                        if escolha == 1 and qtd_vit_erro.contar('ok') == 10:
                            premioEspecialFacil()
                        elif escolha == 2 and qtd_vit_erro.contar('ok') == 10:
                            premioEspecialMedio()
                        elif escolha == 3 and qtd_vit_erro.contar('ok') == 10:
                            premioEspecialDificil()

                        if pontuacao == 300:
                            premioGeral()

                    # Derrota
                    elif jog == 0 and com == 1:
                        print('Você perdeu essa jogada!')
                        derrota_pedra_x_papel()
                        qtd_vit_erro.adicionar('x')
                        if escolha == 1 and qtd_vit_erro.contar('x') == 6:
                            print('Você foi derrotado!')
                            qtd_vit_erro.deletar()
                            print('Reiniciando Jogo!')
                            break
                        elif escolha == 2 and qtd_vit_erro.contar('x') == 4:
                            print('Você foi derrotado!')
                            qtd_vit_erro.deletar()
                            print('Reiniciando Jogo!')
                            break
                        elif escolha == 3 and qtd_vit_erro.contar('x') == 2:
                            print('Você foi derrotado!')
                            qtd_vit_erro.deletar()
                            print('Reiniciando Jogo!')
                            break

                    elif jog == 1 and com == 2:
                        print('Você perdeu essa jogada!')
                        derrota_papel_x_tesoura()
                        qtd_vit_erro.adicionar('x')
                        if escolha == 1 and qtd_vit_erro.contar('x') == 6:
                            print('Você foi derrotado!')
                            qtd_vit_erro.deletar()
                            print('Reiniciando Jogo!')
                            break
                        elif escolha == 2 and qtd_vit_erro.contar('x') == 4:
                            print('Você foi derrotado!')
                            qtd_vit_erro.deletar()
                            print('Reiniciando Jogo!')
                            break
                        elif escolha == 3 and qtd_vit_erro.contar('x') == 2:
                            print('Você foi derrotado!')
                            qtd_vit_erro.deletar()
                            print('Reiniciando Jogo!')
                            break

                    elif jog == 2 and com == 0:
                        print('Você perdeu essa jogada!')
                        derrota_tesoura_x_pedra()
                        qtd_vit_erro.adicionar('x')
                        if escolha == 1 and qtd_vit_erro.contar('x') == 6:
                            print('Você foi derrotado!')
                            qtd_vit_erro.deletar()
                            print('Reiniciando Jogo!')
                            break
                        elif escolha == 2 and qtd_vit_erro.contar('x') == 4:
                            print('Você foi derrotado!')
                            qtd_vit_erro.deletar()
                            print('Reiniciando Jogo!')
                            break
                        elif escolha == 3 and qtd_vit_erro.contar('x') == 2:
                            print('Você foi derrotado!')
                            qtd_vit_erro.deletar()
                            print('Reiniciando Jogo!')
                            break
            else:
                print('Opção inválida!')
                sleep(0.5)
                print('Reiniciando Jogo!')
                sleep(0.5)

            if len(jogada) == 10:
                break

    def conquistas(self):
        global pontuacao
        print('Sua pontuação é de ' + str(pontuacao) + ' pontos.')
