from lutadormma import LutadorMMA
from nadador import Nadador
from futebolista import Futebolista
af=False
an=False
al=False
opx=99
opy=99
opz=99
while opx!=0:
    opx=int(input("Escolha uma das opçoes:\n0 - Sair\n1 - Deseja cadastrar um atleta\n2 - Mostrar Informação de atleta\nEscolha uma poção: "))
    if opx==1:
        while opy!=0:
            opy=int(input("Escolha uma das opçoes:\n0 - Retornar ao menu anterior\n1 - Cadastrar Futebolista\n2 - Cadastrar Nadador \n3 - Cadastrar Lutador de MMA\nEscolha uma poção: "))
            if opy==1 and af==False:
                nome=input('Digite o nome do futebolista: ')
                idade= input("Digite a idade: ")
                gol= input("Digite os gols marcados: ")
                f=Futebolista(nome,idade,gol)
                af=True 
            elif opy==1 and af==True:
                print("Futebolista esta cadastrado")
            elif opy==2 and an==False:
                nome=input('Digite o nome do nadador: ')
                idade= input("Digite a idade: ")
                nmeda=input('Digite o numero de medalhas: ')
                noli= input("Digite a quantidade de olimpiadas participadas: ")
                n=Nadador(nome,idade,nmeda,noli)
                an=True
            elif opy==2 and an==True:
                print("Nadador ja esta cadastrado")    
            elif opy==3 and al==False:
                nome=input('Digite o nome do lutador: ')
                idade= input("Digite a idade: ")
                cint=input("Digite a quantidade de cinturoes disputados: ")
                cat=input("Digite a categoria correspondente: ")
                l=LutadorMMA(nome,idade,cint,cat)
                al=True
            elif opy==3 and al==True:
                print("Lutador ja esta cadastrado") 
            elif opy==0:
                print("Saindo")
    if opx==2:
        while opz !=0:
            opz=int(input("Escolha uma das opçoes:\n0 - Retornar ao menu anterior\n1 - Mostrar Futebolista\n2 - Mostrar Nadador \n3 - Mostrar Lutador de MMA\nEscolha uma poção: "))
            if opz==1 and af==True:
                print(f.Faz_o_que(f.nome,f.gol))
            elif opz==2 and an==True:
                print(n.Faz_o_que(n.nome,n.nmeda,n.noli))
            elif opz==3 and al==True:
                print(l.Faz_o_que(l.nome,l.cat,l.cint))
            elif opz==0:
                print("Saindo")
    