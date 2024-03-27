from collections import deque
import random


##usando BFS

class Ambiente:
    def __init__(self):
        self.estado = {'A': random.choice(['cheio', 'vazio']),
                       'B': random.choice(['cheio', 'vazio'])}
        self.accoes = ['encher', 'esquerda', 'direita']

    def percepcao(self, agente):
        return agente.localizacao, self.estado[agente.localizacao]

    def localizacao_default(self):
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
        fila = deque([(self.localizacao, [])])
        visitados = {self.localizacao}

        while fila:
            posicao, caminhoo = fila.popleft()
            estado = ambiente.estado[posicao]

            if estado == 'vazio':
                return 'encher', caminhoo

            for accao in ambiente.accoes:
                nova_posicao = posicao
                novo_caminho = caminhoo + [accao]

                if accao == 'esquerda' and posicao == 'B':
                    nova_posicao = 'A'
                elif accao == 'direita' and posicao == 'A':
                    nova_posicao = 'B'

                if nova_posicao not in visitados:
                    fila.append((nova_posicao, novo_caminho))
                    visitados.add(nova_posicao)

        # return 'encher', []


# Main
print()
ambient = Ambiente()
print("Estado do Ambiente:", ambient.estado)

if all(estado == 'vazio' for estado in ambient.estado.values()):
    balde = random.choice(['A', 'B'])
    ambient.executar_accao('encher', Agente(balde))

localizacao_agente = ambient.localizacao_default()
agent = Agente(localizacao_agente)

while 'vazio' in ambient.estado.values():
    percepcao = ambient.percepcao(agent)
    print("Percepção:", percepcao)

    acao, caminho = agent.programa_metas(ambient)
    ambient.executar_accao(acao, agent)

    print("Ação a Realizar:", acao)
    print("Pontuação:", agent.desempenho)
    print("Estado do Ambiente apos:", ambient.estado)
