# -*- coding: cp1252 -*-
#------------------------introdução------------------------------
print("Seja bem-vindo ao meu jogo da torre de hanoi...")
print("Para jogar basta digitar o numero do pino que deseja retirar o item do topo,  e digitar o numero do pino que deseja colocar esse elemento")
#---------------------criação das pilhas-------------------------
pilha1 = []
pilha2 = []
pilha3 = []
mov = 0
# -----------algoritmo para escolher o numero de discos-----------

escolha = int(input("Digite o numero de discos: "))
pilha1 = list(range(escolha, 0, -1))

# ---formatação de strings para deixar o jogo mais compreensivel---

def printaABagaca():
    modelo = "{:^11}   {:^11}   {:^11}"
    for i in range(escolha, 0, -1):
        t1 = ""
        t2 = ""
        t3 = ""
        if len(pilha1) >= i:
            t1 = pilha1[i - 1]

        if len(pilha2) >= i:

            t2 = pilha2[i - 1]
        if len(pilha3) >= i:

            t3 = pilha3[i - 1]
        print(modelo.format(t1, t2, t3))

#-----------entrada de informação para mover os discos---------------

while pilha3 != escolha:
    printaABagaca()
    print("-----+-------------+-------------+-----")
    print ("Voce executou ",mov," movimentos...")
    qual = int(input("digite o numero da pilha que deseja tirar um elemento: "))
    onde = int(input("Digite para onde quer o mover: "))
    
# --------------movimentação da pilha 1 para a 2-3--------------------

    if qual == 1:
        if (len(pilha1)) == 0:
            print ("Nao eh possivel fazer este movimento...")
        else:
            if onde == 2:
                if len(pilha2) == 0:
                    pilha2.append(pilha1.pop(-1))
                elif pilha2[-1] < pilha1[-1]:
                    print("Nao eh possivel fazer este movimento...")
                elif pilha2[-1] > pilha1[-1]:
                    pilha2.append(pilha1.pop(-1))

            elif onde == 3:
                if len(pilha3) == 0:
                    pilha3.append(pilha1.pop(-1))
                elif pilha3[-1] < pilha1[-1]:
                    print("Nao eh possivel fazer este movimento...")
                elif pilha3[-1] > pilha1[-1]:
                    pilha3.append(pilha1.pop(-1))

# ---------------movimentação da pilha 2 para a 1-3------------------

    elif qual == 2:
        if len(pilha2) == 0:
            print("Nao eh possivel fazer este movimento... ")
        else:
            if onde == 1:
                if len(pilha1) == 0:
                    pilha1.append(pilha2.pop(-1))
                elif pilha1[-1] < pilha2[-1]:
                    print("Nao eh possivel fazer este movimento...")
                elif pilha1[-1] > pilha2[-1]:
                    pilha1.append(pilha2.pop(-1))

            elif onde == 3:
                if len(pilha3) == 0:
                    pilha3.append(pilha2.pop(-1))
                elif pilha3[-1] < pilha2[-1]:
                    print("Nao eh possivel fazer este movimento...")
                elif pilha3[-1] > pilha2[-1]:
                    pilha3.append(pilha2.pop(-1))

# --------------movimentação da pilha 3 para a 1-2--------------------
    elif qual == 3:
        if len(pilha3) == 0:
            print("Nao eh possivel fazer este movimento...")
        else:
            if onde == 1:
                if len(pilha1) == 0:
                    pilha1.append(pilha3.pop(-1))
                elif pilha1[-1] < pilha3[-1]:
                    print("Nao eh possivel fazer este movimento...")
                elif pilha1[-1] > pilha3[-1]:
                    pilha1.append(pilha3.pop(-1))

            elif onde == 2:
                if len(pilha2) == 0:
                    pilha2.append(pilha3.pop(-1))
                elif pilha2[-1] < pilha3[-1]:
                    print("Nao eh possivel fazer este movimento...")
                elif pilha2[-1] > pilha3[-1]:
                    pilha2.append(pilha3.pop(-1))

# ---------criação de um algoritmo para checar a vitoria------------------
    mov = mov+1
    
    if pilha3 == list(range(escolha, 0, -1)):
        print("Voce ganhou! ")
        printaABagaca()
        print("-----+-------------+-------------+-----")
        print ("Voce executou ",mov," movimentos para ganhar!!!")
        break
