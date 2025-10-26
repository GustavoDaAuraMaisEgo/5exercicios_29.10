import os
import random
import time

os.system('cls' if os.name == 'nt' else 'clear')
jogadores = []
print('Campeonato mundial de rolar um dado!')

for c in range (0,4):
    nome = str(input(f'Nome do jogador {c+1}: '))
    jogadores.append(nome)
print('Preparando os dados...')
time.sleep(2)

resultados = {}
for jogador in jogadores:
    dado = random.randint(1,6)
    resultados[jogador] = dado
    print(f'O jogador {jogador} rolou o dado e tirou {dado}.')
    time.sleep(1)
print('Calculando os resultados finais...')
time.sleep(2)

print('------Resultados finais------')
for jogador, resultado in resultados.items():
    print(f'\nO {jogador} ficou em primeiro lugar' if resultado == max(resultados.values()) else f'O {jogador} ficou com {resultado} pontos.')
    print(f'\nO {jogador} ficou em segundo lugar' if resultado == sorted(resultados.values(), reverse=True)[1] else f'O {jogador} ficou com {resultado} pontos.')
    print(f'\nO {jogador} ficou em terceiro lugar' if resultado == sorted(resultados.values(), reverse=True)[2] else f'O {jogador} ficou com {resultado} pontos.')
    print(f'\nO {jogador} ficou em quarto lugar' if resultado == min(resultados.values()) else f'O {jogador} ficou com {resultado} pontos.')