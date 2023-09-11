def rankear(jogador, vitorias):
    if vitorias >= 15:
        print('O jogador', jogador, '. O jogador está no rank Campeão!!!')

    elif 10 <= vitorias <= 14:
        print('O jogador', jogador, '. O jogador está no rank Mestre!!!')

    elif 5 <= vitorias <= 9:
        print('O jogador', jogador, '. O jogador está no rank Experiente!!!')

    else:
        print('O jogador', jogador, '. O jogador está no rank Iniciante !!!')