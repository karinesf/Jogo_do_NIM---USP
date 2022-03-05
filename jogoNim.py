#Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro.
# Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um.
# Quem tirar as últimas peças possíveis ganha o jogo.
#Existe uma estratégia para ganhar o jogo que é muito simples:
# ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.
# Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada.
# Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo.
cont = 1
pc_ganhou_rodada = 0
usuario_ganhou_rodada = 0


def computador_escolhe_jogada(n, m):
    if n >= m:
        pecas_pc = n % (m + 1)
    elif n < m:
        pecas_pc = n
    else:
        pecas_pc = m
    return pecas_pc


def usuario_escolhe_jogada(n, m):
    while True:
        pecas_usuario = int(input('\nQuantas peças você vai tirar?'))
        if pecas_usuario > m:
            print('\nOops! Jogada inválida! Tente de novo.')
        else:
            return pecas_usuario


def partida():
    global pc_ganhou_rodada
    global usuario_ganhou_rodada
    pontos_usuario = 0
    pontos_pc = 0
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    if n % (m + 1) == 0:
        print('\nVoce começa!')
        while n > 0:
            jogada_usuario = usuario_escolhe_jogada(n, m)
            print(f'\nVoce tirou {jogada_usuario} peça(s).')
            rest_pecas = n - jogada_usuario
            if rest_pecas > 0:
                print(f'Agora restam {rest_pecas} peças no tabuleiro.')
            n = rest_pecas
            if n == 0:
                pontos_usuario += 1
                break
            jogada_pc = computador_escolhe_jogada(n, m)
            print(f'\nO computador tirou {jogada_pc} peça(s).')
            rest_pecas = n - jogada_pc
            if rest_pecas > 0:
                print(f'Agora restam {rest_pecas} peças no tabuleiro.')
            n = rest_pecas
            if n == 0:
                pontos_pc += 1
                break
    else:
        print('\nComputador começa!')
        while n != 0:
            jogada_pc = computador_escolhe_jogada(n, m)
            print(f'\nO computador tirou {jogada_pc} peça(s).')
            rest_pecas = n - jogada_pc
            if rest_pecas > 0:
                print(f'Agora restam {rest_pecas} peças no tabuleiro.')
            n = rest_pecas
            if n == 0:
                pontos_pc += 1
                break
            jogada_usuario = usuario_escolhe_jogada(n, m)
            print(f'\nVoce tirou {jogada_usuario} peça(s).')
            rest_pecas = n - jogada_usuario
            if rest_pecas > 0:
                print(f'Agora restam {rest_pecas} peças no tabuleiro.')
            n = rest_pecas
            if n == 0:
                pontos_usuario += 1
                break
    if n == 0:
        if pontos_pc > pontos_usuario:
            print('\nFim do jogo! O Computador ganhou!')
            pc_ganhou_rodada += 1
        else:
            print('\nFim do jogo! Voce ganhou!')
            usuario_ganhou_rodada += 1
    if cont == 3:
        print('\n**** Final do campeonato! ****')
        print(f'\nPlacar: Você {usuario_ganhou_rodada} X {pc_ganhou_rodada} Computador')
        return 0


def campeonato():
    global cont
    while cont <= 3:
        print(f'\n**** Rodada {cont} ****')
        partida()
        cont += 1


# programa principal
op = 1 or 2
while True:
    print('\nBem-vindo ao jogo do NIM! Escolha:')
    op = int(input('\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))
    if op == 1:
        print('\nVoce escolheu uma partida isolada!')
        partida()
        break
    elif op == 2:
        print('\nVoce escolheu um campeonato!')
        campeonato()
        break
    else:
        print('\nOpção inválida. Tente novamente.')





