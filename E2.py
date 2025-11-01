import os
import random
import time

os.system('cls')
jogadores = []
print('Campeonato mundial de rolar um dado!')

for c in range(4):
    nome = input(f'Nome do jogador {c+1}: ').strip() or f'Jogador{c+1}'
    jogadores.append(nome)

print('Preparando os dados...')
time.sleep(1)

# rolar dados
resultados = {}
for jogador in jogadores:
    dado = random.randint(1, 6)
    resultados[jogador] = dado
    print(f'O jogador {jogador} rolou o dado e tirou {dado}.')
    time.sleep(0.6)

print('\nCalculando os resultados finais...')
time.sleep(1)
