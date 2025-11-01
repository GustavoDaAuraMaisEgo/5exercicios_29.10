import os
import random
import time

os.system('cls')
jogadores = []
print('Campeonato mundial de rolar um dado!')

# Usando enumerate para entrada de nomes (começa do 1)
for i, _ in enumerate(range(4), 1):
    nome = str(input(f'Nome do jogador {i}: '))
    jogadores.append(nome)
print('Preparando os dados...')
time.sleep(2)

resultados = {}
# Usando enumerate para mostrar número do jogador na rolagem
for num, jogador in enumerate(jogadores, 1):
    dado = random.randint(1,6)
    resultados[jogador] = dado
    print(f'Jogador {num} ({jogador}) rolou o dado e tirou {dado}.')
    time.sleep(1)
print('Calculando os resultados finais...')
time.sleep(2)

# Ordenar jogadores por pontuação (maior para menor)
jogadores_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

print('------Resultados finais------')
# Usando enumerate para gerar posições automaticamente
for pos, (jogador, pontos) in enumerate(jogadores_ordenados, 1):
    sufixo = 'º' if pos == 1 else 'º'
    print(f'{pos}{sufixo} lugar - {jogador}: {pontos} pontos')