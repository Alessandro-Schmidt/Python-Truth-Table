from typing import final
from tabulate import tabulate
import pyfiglet

font = pyfiglet.figlet_format('TDE - RPLM')
autoria = pyfiglet.figlet_format('Alessandro\ne\nVinícius', font = "digital" )
print(font)
print(autoria)


variaveis = [['P','Q', '~P', '~Q'], [True, True, False, False], [True, False, False, True], [False, True, True, False], [False,False, True, True]]
def main():
    print('Considere as duas variáveis')

def implicacao():
    variaveis[0].append('P -> Q')
    i = 1 
    while i!=5:
        variaveis[i].append(variaveis[i][2] or variaveis[i][1])
        i+=1
    
def conjuncao():
    variaveis[0].append('P ^ Q')
    i = 1 
    while i!=5:
        variaveis[i].append(variaveis[i][0] and variaveis[i][1])
        i+=1

def disjuncao():
    variaveis[0].append('P v Q')
    i = 1 
    while i!=5:
        variaveis[i].append(variaveis[i][0] or variaveis[i][1])
        i+=1

def bicondicional():
    variaveis[0].append('P <=> Q')
    i = 1 
    while i!=5:
        if variaveis[i][0] == variaveis[i][1]:
            variaveis[i].append(True)
        else:
            variaveis[i].append(False)
        i+=1

def atribuicaoDeValores():
    print(tabulate(variaveis, headers='firstrow', tablefmt='grid'))

def main():
    print('-'*len('1 - Implicação (P -> Q) ---- 2 - Conjunção (P ^ Q)\n3 - Disjunção (P v Q) ---- 4 - Bicondicional (P<=>Q)'))
    print('Considere o menu de opções possíveis com P ou Q:')
    print('1 - Implicação (P -> Q) ---- 2 - Conjunção (P ^ Q)\n3 - Disjunção (P v Q) ---- 4 - Bicondicional (P<=>Q)')
    print('-'*len('1 - Implicação (P -> Q) ---- 2 - Conjunção (P ^ Q)\n3 - Disjunção (P v Q) ---- 4 - Bicondicional (P<=>Q)'))
    while True:
        escolha = str(input('Digite a expressão ou o número da operação: '))
        if escolha[2] == '-' or escolha == '1': 
            implicacao()
            atribuicaoDeValores()
        elif escolha[2] in 'P ^ Q' or escolha =='2':
            conjuncao()
            atribuicaoDeValores()
        elif escolha[2] == 'v' or escolha =='3':
            disjuncao()
            atribuicaoDeValores()            
        elif escolha[2] =='=' or escolha =='4':
            bicondicional()
            atribuicaoDeValores()
        else: 
            print('\033[31mDigite uma operação válida\033[m')
        sair = str(input('\nDeseja fazer nova operação? [SIM / NAO]: '))
        if sair in 'N':
            break

#implicacao()
#conjuncao()
#disjuncao()
#bicondicional()
#atribuicaoDeValores()
main()