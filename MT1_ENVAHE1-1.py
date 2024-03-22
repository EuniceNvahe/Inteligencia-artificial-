import random

class Ambiente:
    def __init__(self):
        self.estado = {'A': random.choice(['cheio', 'vazio']),
                       'B': random.choice(['cheio', 'vazio']),
                       'C': random.choice(['cheio', 'vazio'])}
        self.accoes = ['encher', 'direita', 'baixo', 'cima']

    def percepcao(self, agente):
        return (agente.localizacao, self.estado[agente.localizacao])

    def localizacao_default(self):
        return random.choice(['A', 'B', 'C'])

    def executar_accao(self, accao, agente):
        if accao == 'direita':
            #agente.desempenho -= 1
            if agente.localizacao == 'A':
                agente.desempenho -= 1
                agente.localizacao = 'B'
        elif accao == 'baixo':
            #agente.desempenho -= 1
            if agente.localizacao == 'B':
                agente.desempenho -= 1
                agente.localizacao = 'C'
        elif accao == 'cima':
            #agente.desempenho -= 1
            if agente.localizacao == 'C':
                agente.desempenho -= 1
                agente.localizacao = 'A'
        elif accao == 'encher':
            if 'vazio' in self.estado.values():
                #agente.desempenho += 10
                for balde in self.estado:
                    if self.estado[balde] == 'vazio':
                        agente.desempenho += 10
                        self.estado[balde] = "cheio"
                        print("Percepção:", self.percepcao(agente))
                        print("Ação a Realizar:", accao)
                        print("Desempenho:", agente.desempenho)
                        print("Estado do Ambiente apos accao do agente:", self.estado)
                        print()



class Agente:
    def __init__(self, localizacao):
        self.desempenho = 0
        self.localizacao = localizacao
        self.modelo = {'A': None, 'B': None, 'C': None}

    def atualizar_modelo(self, percepcao):
        localizacao, estado = percepcao
        self.modelo[localizacao] = estado

    def programa_modelo(self, percepcao):
        self.atualizar_modelo(percepcao)
        if 'vazio' in self.modelo.values():
            return 'encher'
        elif self.localizacao == 'A' and self.modelo['B'] == 'vazio':
            return 'direita'
        elif self.localizacao == 'B' and self.modelo['C'] == 'vazio':
            return 'baixo'
        elif self.localizacao == 'C' and self.modelo['A'] == 'vazio':
            return 'cima'
        else:
            return 'encher'



ambiente = Ambiente()
print("Estado inicial do Ambiente:", ambiente.estado)

localizacao_agente = ambiente.localizacao_default()
agente = Agente(localizacao_agente)

while 'vazio' in ambiente.estado.values():
    percepcao = ambiente.percepcao(agente)
    acao = agente.programa_modelo(percepcao)
    ambiente.executar_accao(acao, agente)


print("Estado final do Ambiente: ", ambiente.estado)
print(f"localizacao do agente: {localizacao_agente}")


#implementacao de agente baseado em modelo de Mini-teste1 de Eunice Nvahe


