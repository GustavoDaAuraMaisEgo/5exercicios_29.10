import os
os.system('cls')

print('='*35)
print("Bem vindo. Faça o Cadastro dos Alunos")
print('='*35)

cadastro = dict()

for c in range(1, 5):
    print(f"----- {c}° Aluno -----")
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    os.system('cls')
    media = (nota1 + nota2 + nota3 + nota4) / 4
    cadastro[nome] = media
    print("-------------------")

os.system('cls')
print("----- Boletim dos Alunos -----")
for k, v in cadastro.items():
    print(f"O aluno {k} teve média {v:.1f}")
print("------------------------------")

while True:
    consulta = str(input("Deseja consultar a média de algum aluno? (s/n): ")).lower().strip()
    if consulta == 's':
        os.system('cls')
        aluno = str(input("Digite o nome do aluno: "))
        if aluno in cadastro:
            
            if cadastro[aluno] >= 7.0:
                print(f"A média do aluno {aluno} é {cadastro[aluno]:.1f} - Aprovado")
            else:
                print(f"A média do aluno {aluno} é {cadastro[aluno]:.1f} - Reprovado")
        else:
            print("Aluno não encontrado.")
    elif consulta == 'n':
        os.system('cls')
        print("Encerrando o programa. Obrigado!")
        break
    else:
        
        print("Opção inválida.Por favor, Digite 's' para sim ou 'n' para não.")