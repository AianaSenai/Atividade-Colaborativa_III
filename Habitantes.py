import os
os.system("cls|| clear")
from dataclasses import dataclass
@dataclass
#Nome Alunos: Araúna Noemi
#Aiana Santos
#Rayane Costa

class Dados:
    sexo: int
    idade : int
    salario: float
while True:
    print("""
    1- Adicionar pessoas
    2- Exibir Resultados e Sair
    """)

    opcao = int (input ("Digite a opçao escolhida: ") )
    match (opcao):
        case 1:
            lista_inicial = []
            cliente = Dados(
                sexo = input("Digite seu sexo:  \n1-M \n2-F \n:"),
                idade = int(input("Digite sua idade: ")),
                salario = float(input("Digite o seu salario: "))
            )
            lista_inicial.append(cliente)

            nome_arquivo ="prefeitura.txt"

            with open(nome_arquivo,"a") as arquivo_prefeitura:
                for pessoa in lista_inicial:
                    arquivo_prefeitura.write(f"{pessoa.sexo}, {pessoa.idade}, {pessoa.salario}\n")
            os.system("cls||clear")
        case 2:
            os.system("cls||clear")
            lista_final = []
            lista_sexo= []
            lista_idade= []
            lista_salario= []
            lista_inicial = []
            contador = 0
            nome_arquivo ="prefeitura.txt"
            with open(nome_arquivo ,"r") as arquivo_prefeitura:
                for linha in arquivo_prefeitura:
                    sexo, idade, salario= linha.strip().split(",")
                    lista_inicial.append(Dados(sexo = sexo, idade = int(idade), salario = float(salario)))
            for dado in lista_inicial:
                if (dado.sexo == "2") and (dado.salario>=5000):
                    contador +=1 
                lista_idade.append(dado.idade)
                lista_salario.append(dado.salario)
                print (f"Sexo: {dado.sexo}")
                print (f"Idade: {dado.idade}")
                print(f"Salario: {dado.salario}")
            media_salario = sum (lista_salario)/ len (lista_salario)
            idade_maior = max(lista_idade)
            idade_menor = min (lista_idade)
            print(f"Media de Salario: {media_salario}")
            print(f"Salario maior que 50000: {contador}")
            lista_final.append(media_salario)
            lista_final.append(idade_maior)
            lista_final.append(idade_menor)
            lista_final.append(contador)
            nome_arquivo_1 ="pesquisa_habitantes.txt"
            with open(nome_arquivo_1,"w") as arquivo_prefeitura:
                arquivo_prefeitura.write(f"Media de salario: {media_salario} \n")
                arquivo_prefeitura.write(f"Maior idade: {idade_maior} \n")
                arquivo_prefeitura.write(f"Menor idade: {idade_menor} \n")
                arquivo_prefeitura.write(f"Mulheres que recebem 5K +: {contador} \n")
            break
          
        case _:
            print("Opçao invalida")
    