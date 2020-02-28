from random import randint
from os import system

print(
    'Ola, esse jogo é para adivinhar os números.\n'
    'Lembrando, o jogo é multiplayer\n'
    'Tenha bom proveito e se divirta\n'
)

jogador1 = input('\nDigite o nome do jogador 1: ')  # Recebe o nome do jogador 1
jogador2 = input('\nDigite o nome do jogador 2: ')  # Recebe o nome do jogador 2
acertos_jogador1 = acertos_jogador2 = numero_jogo = jogador = numero_adivinhar = palpite = 0  # Variáveis usadas


def limpatela():  # Função para limpar a tela no TERMINAL (PROMPT DE COMANDO)
    system('cls')


def escolha_numeros():  # Função para a escolha de números
    global numero_adivinhar
    numero1 = int(
        input(
            '\nIrá querer adivinhar do numero: '  # Recebe o numero de inicio para adivinhar
        )
    )
    while numero1 < 0:  # Confere se o numero é maior que 0
        print(
            'O número deve ser positivo.'
        )

        numero1 = int(
            input(
                '\nIrá querer adivinhar do numero: '
            )
        )

    numero2 = int(
        input(
            '\nAté o número: '  # Recebe o numero final para adivinhar
        )
    )
    while numero2 < 0 or numero2 < numero1:  # Confere se o número2 é maior que 0 e maior que o numero1 (numero_inicial)
        print(
            'O número deve ser positivo e maior que o número de inicio.'
        )
        numero2 = int(
            input(
                '\nAté o número: '
            )
        )
    numero_adivinhar = randint(numero1, numero2)  # Pega um número dentre o numero1 e o numero2 inclusive
    limpatela()  # Chama a função de limpar a tela


def continuar():  # Função para continuar
    continuar_o_jogo = input(
        'Deseja continuar a jogar [S/N]? '  # Recebe a resposta do usuário se ele deseja continuar jogando ou não
    )
    continuar_o_jogo = continuar_o_jogo.upper()  # Transforma a resposta em upper (maiuscula) para evitar erros

    if continuar_o_jogo == 'S':  # Verifica se continuar é igual a S (sim)
        input(
            'Okay, pressione enter para continuar'
        )
        escolha_numeros()  # Chama a função para a escolha dos números
        limpatela()  # Chama a função de limpar a tela

    else:  # Se for diferente de S este bloco é executado
        input(
            'Okay, pressione enter para sair'  # Mensagem para quem rodar no prompt nao ver a janela fechando do nada
        )
        exit()  # Sai do programa


def placar():  # Função para mostrar e calcular o placar
    global acertos_jogador1, acertos_jogador2, numero_jogo
    if jogador % 2 != 0:  # Verifica se foi o jogador 1 que acertou
        acertos_jogador1 += 1  # Acrescenta mais um acerto para o jogador 1
    else:  # Se não foi o jogador 1, logicamente foi o 2 que acertou
        acertos_jogador2 += 1  # Acrescenta mais um acerto para o jogador 2
    numero_jogo += 1  # Acrescente mais um jogo para ambos os jogadores
    print(
        f'O placar está:\n'
        f'{jogador1} = {acertos_jogador1} acertos com {numero_jogo} jogos\n'  # Mostra pontuação do jogador 1
        f'{jogador2} = {acertos_jogador2} acertos com {numero_jogo} jogos\n'  # Mostra pontuação do jogador 2
    )


def recebendo_e_conferindo_palpite():  # Função que confere o palpite do jogador
    global jogador, palpite
    jogador += 1  # Acrescenta um numero no jogador para identificar qual jogador jogou
    palpite = int(
        input(
            'Digite o seu palpite: '  # Recebe o palpite do jogador que está na vez
        )
    )

    if palpite < numero_adivinhar:  # Verifica se o palpite é menor que o numero que o PC escolheu
        print(
            'Seu palpite precisa ser maior\n'
        )

    elif palpite > numero_adivinhar:  # Verifica se o palpite é maior que o numero que o PC escolheu
        print(
            'Seu palpite precida ser menor\n'
        )

    else:  # Este bloco só roda se o palpite foi igual ao número que o PC escolheu
        if jogador % 2 != 0:  # Verifica se foi o jogador 1 que acertou
            print(
                f'\nParabéns, o jogador(a) {jogador1} acertou\n'
            )
        else:  # Se não foi o jogador 1, logicamente foi o 2 que acertou
            print(
                f'\nParabéns, o jogador(a) {jogador2} acertou\n'
            )
        placar()  # Chama a função placar
        continuar()  # Chama a função continuar


escolha_numeros()  # Chama a função de escolher os números
while True:  # Inicia um loop infinito que só é quebrado quando o jogador diz que não deseja continuar
    print(
        f'\nVez do(a) {jogador1}'  # Mostra que é a vez do jogador 1
    )
    recebendo_e_conferindo_palpite()  # Chama a função de recebe e confere o palpite do jogador
    print(
        f'\nVez do(a) {jogador2}'  # Mostra que é a vez do jogador 2
    )
    recebendo_e_conferindo_palpite()  # Chama a função de recebe e confere o palpite do jogador
