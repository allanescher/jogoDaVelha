import os

def main():
    sair = 'C'
    #loop para reiniciar o jogo
    while sair.upper() == 'C':
        #criação da lista
        lista_variaveis = [1,2,3,4,5,6,7,8,9]
        #chamar função para imprimir tabela
        imprimir_tabela(lista_variaveis)
        #chamar função para coletar as jogadas
        imprimir_jogada(lista_variaveis)
        sair = input('Para continuar digite "C": ')
    
#função para imprimir a tabela do jogo
def imprimir_tabela(lista_variaveis):
    #comando para limpar a tela
    os.system('cls')
    linha1 =" {0} | {1} | {2} "
    print(linha1.format(lista_variaveis[0], lista_variaveis[1], lista_variaveis[2]))
    print("-- +-- +--")
    print(linha1.format(lista_variaveis[3], lista_variaveis[4], lista_variaveis[5]))
    print("-- +-- +--")
    print(linha1.format(lista_variaveis[6], lista_variaveis[7], lista_variaveis[8]))
    
#funcao para passar as informações do jogador e parar o loop quando definir o ganhador ou empate
def imprimir_jogada(lista_variaveis):
    contador = 0
    while contador < 9:
        contador += 1
        #informações jogador 1
        jogador = '1'
        if jogada_jogador(lista_variaveis, 'O', jogador) == '1':
            ganhador = '1'
            break
        #parar o código caso ocorra empate
        if contador == 9:
            break
        contador += 1
        #informações jogador 2
        jogador = '2'
        if jogada_jogador(lista_variaveis, 'X', jogador) == '2':
            ganhador = '2'
            break
        
    if contador == 9 and ganhador == '':
        print('Jogo empatado')

#função que verifica se o valor digitado pelos jogadores é duplicado
def verifica_valor_duplicado(lista_variaveis, verificar_valor):
    erro = '1'
    while erro != '':
        #verifica se o valor digitada é maior que nove ou menor que 0, para não dar erro na lista
        if verificar_valor > 9 or verificar_valor <= 0:
            verificar_valor = int(input("Jogador informe outro número, este número não esta na tabela: "))
        else:
            #verifica se o valor na lista esta preenchido com alguma jogada
            if lista_variaveis[verificar_valor - 1] == 'X' or lista_variaveis[verificar_valor - 1] == 'O':
                verificar_valor = int(input("Jogador informe outro número, você ainda esta digitando em uma posição já preenchida: "))
            else:
                erro = ''
            
    return verificar_valor    

#funcao para conferir se houve ganhador,passando como retorno o ganhador
def verifica_ganhador(lista_variaveis, x_o):
    ganhador = ''
    if (lista_variaveis[0] == x_o and lista_variaveis[1] == x_o and lista_variaveis[2] == x_o or
    lista_variaveis[3] == x_o and lista_variaveis[4] == x_o and lista_variaveis[5] == x_o or
    lista_variaveis[6] == x_o and lista_variaveis[7] == x_o and lista_variaveis[8] == x_o or
    lista_variaveis[0] == x_o and lista_variaveis[3] == x_o and lista_variaveis[6] == x_o or
    lista_variaveis[1] == x_o and lista_variaveis[4] == x_o and lista_variaveis[7] == x_o or
    lista_variaveis[2] == x_o and lista_variaveis[5] == x_o and lista_variaveis[8] == x_o or
    lista_variaveis[0] == x_o and lista_variaveis[4] == x_o and lista_variaveis[8] == x_o or
    lista_variaveis[2] == x_o and lista_variaveis[4] == x_o and lista_variaveis[6] == x_o):
        if x_o == 'O':
            ganhador = '1'
        elif x_o == 'X':
            ganhador = '2'
            
    return ganhador

#funcao para receber o valor da jogada, imprimir a tabela com a jogada e verifica o ganhador
def jogada_jogador(lista_variaveis, x_o, jogador):
    ganhador = ''
    #recebe informação da jogada
    jogada_jogador = int(input('Jogador ' + jogador + ' (' + x_o +  ') informe o número: '))
    verificar_valor = jogada_jogador
    #chama funcao para conferir valor duplicado
    jogada_jogador = verifica_valor_duplicado(lista_variaveis, verificar_valor)
    #atribuir o valor da jogada a lista
    lista_variaveis[jogada_jogador - 1] = x_o
    imprimir_tabela(lista_variaveis)
    #verifica se houve ganhador
    if verifica_ganhador(lista_variaveis, x_o) == jogador and verifica_ganhador(lista_variaveis, x_o) != '':
        print('Ganhador ' + jogador + ' ' + ' vencedor')
        ganhador = jogador

    return ganhador

#main para iniciar o código
main()