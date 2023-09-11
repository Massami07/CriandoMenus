import rankeamento
import coletardados


def menuativador():
    ativador = 25
    while ativador != 0:
        print('Menu de acesso')
        print('Selecione a opçao que voce deseja acessar')
        print('1-Cadastrar jogador')
        print('2-Mostrar rank do jogador')
        print('0-Sair')
        ativador = int(input("Qual opção do menu você deseja acessar?"))

        if ativador == 1:
            jogador = coletardados.coletaDados()


        elif ativador == 2:
            id = int(input("Qual o id do jogador?"))
            rankeamento.rankear(jogador.nome, jogador.vitorias)

        elif ativador == 0:
            break

        else:
            print("Numero invalido")
