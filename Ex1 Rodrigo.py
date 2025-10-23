import os
os.system('cls')

print('='*35)
print("Bem vindo, Aluno. Faça seu Cadastro ",'')
print('='*35)

cadastro=dict()
cadastro['Nome']=str(input("Digite seu Nome: "))
cadastro['N1']=float(input("Digite a Nota 1: "))
cadastro['N2']=float(input("Digite a Nota 2: "))
cadastro['N3']=float(input("Digite a Nota 3: "))
media=(cadastro['N1']+cadastro['N2']+cadastro['N3'])/3

print('='*60)
if media>=7:
    print(f"Aluno {cadastro['Nome']} aprovado com média {media:.2f}")
else:
    print(f"Aluno {cadastro['Nome']} reprovado com média {media:.2f}")
print('='*60)
print("Gostaria de ver suas notas desse Bimestre?")
resposta=str(input("Digite [S] para SIM ou [N] para NÃO: ")).upper().strip()
if resposta=='S':
    print(f"As notas do Aluno {cadastro['Nome']} são: ")
    print(f"Nota 1: {cadastro['N1']}")
    print(f"Nota 2: {cadastro['N2']}")
    print(f"Nota 3: {cadastro['N3']}")
    print(f"Média: {media:.2f}")
else:
    print("Obrigado por utilizar nosso sistema!")  