import random


##usando DFS

class Ambiente:
    def __init__(self):
        self.estado = {'A': random.choice(['cheio', 'vazio']),
                       'B': random.choice(['cheio', 'vazio'])}
        self.accoes = ['encher', 'esquerda', 'direita']

    def percept(self, agente):
        return agente.localizacao, self.estado[agente.localizacao]

    def local_default(self):
        return random.choice(['A', 'B'])

    def executar_accao(self, accao, agente):
        if accao == 'esquerda':
            agente.desempenho -= 1
            if agente.localizacao == 'B':
                agente.localizacao = 'A'
        elif accao == 'direita':
            agente.desempenho -= 1
            if agente.localizacao == 'A':
                agente.localizacao = 'B'
        elif accao == 'encher':
            agente.desempenho += 10
            self.estado[agente.localizacao] = "cheio"


class Agente:
    def __init__(self, localizacao):
        self.desempenho = 0
        self.localizacao = localizacao

    def programa_metas(self, ambiente):
        caminhoo = []
        visitados = set()

        def dfs(posicao):
            if posicao in visitados:
                return False

            visitados.add(posicao)
            estado = ambiente.estado[posicao]

            if estado == 'vazio':
                caminhoo.append(posicao)
                return True

            for acaoo in ambiente.accoes:
                nova_posicao = posicao
                if acaoo == 'esquerda' and posicao == 'B':
                    nova_posicao = 'A'
                elif acaoo == 'direita' and posicao == 'A':
                    nova_posicao = 'B'

                if dfs(nova_posicao):
                    caminhoo.append(posicao)
                    return True

            return False

        if 'vazio' not in ambiente.estado.values():
            return 'encher', []

        if dfs(self.localizacao):
            caminhoo.reverse()
            return 'encher', caminhoo
        # else:
        # return 'encher', []


# Main
print()
ambient = Ambiente()
print("Estado do Ambiente:", ambient.estado)
localizacao_agente = ambient.local_default()
agent = Agente(localizacao_agente)

while 'vazio' in ambient.estado.values():
    percepcao = ambient.percept(agent)
    print("Percepção:", percepcao)

    acao, caminho = agent.programa_metas(ambient)
    ambient.executar_accao(acao, agent)

    print("Ação a Realizar:", acao)
    print("Pontuação:", agent.desempenho)
    print("Caminho:", caminho)
    print("Estado do Ambiente apos:", ambient.estado)

    if 'vazio' not in ambient.estado.values():
        break
