import jogadores


def coletaDados():
    jogador = [1]*10
    print(jogador[1])
    listajogadores: list = [1]*15
    id = int(input('Qual o Id do jogador?'))
    nome = input('Qual é o nome do jogador?')
    vitorias = int(input('Quantas vitorias o jogador tem?'))
    jogador[id] = jogadores.Jogadores(id, nome, vitorias)
    listajogadores.insert(id, jogador[id])
    print(jogador[id].id, jogador[id].nome, jogador[id].vitorias)
    print(listajogadores[id])
    return listajogadores[id]

