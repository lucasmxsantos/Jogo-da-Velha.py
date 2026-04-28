def imprimir_tabuleiro(tabuleiro):
    print("\n")
    for i in range(3):
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
        if i < 2:
            print("---|---|---")
    print("\n")

def verificar_vencedor(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
            
    for i in range(3):
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
            
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
        
    return False

def verificar_empate(tabuleiro):
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                return False
    return True

def jogada_valida(tabuleiro, linha, coluna):
    if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2:
        if tabuleiro[linha][coluna] == ' ':
            return True
    return False

def jogar():
    tabuleiro = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    
    jogador_atual = 'X'
    jogo_ativo = True

    print("**** JOGO DA VELHA ****")
    imprimir_tabuleiro(tabuleiro)

    while jogo_ativo == True:
        print(f"Vez do jogador: {jogador_atual}")
        
        linha = int(input("Escolha a linha (0, 1 ou 2): "))
        coluna = int(input("Escolha a coluna (0, 1 ou 2): "))

        if jogada_valida(tabuleiro, linha, coluna) == True:
            tabuleiro[linha][coluna] = jogador_atual
            imprimir_tabuleiro(tabuleiro)

            if verificar_vencedor(tabuleiro, jogador_atual) == True:
                print(f"O jogador {jogador_atual} venceu.")
                jogo_ativo = False
                
            elif verificar_empate(tabuleiro) == True:
                print("Empate!")
                jogo_ativo = False
                
            else:
                if jogador_atual == 'X':
                    jogador_atual = 'O'
                else:
                    jogador_atual = 'X'
        else:
            print("Jogada inválida, tente novamente.\n")