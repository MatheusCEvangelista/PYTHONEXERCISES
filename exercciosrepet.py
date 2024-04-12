num=0 
soma=0  
for num in range(0,500,3):
    if num!=0:
        if(num%3==0 and num%2==1):
            soma=soma+num
            print(soma)


##################################################################

import time

print('10:00')
for m in range(9,-1,-1):
    for s in range(59,-1,-1):
        print('%d:%d'%(m,s))


######################################################

vet=[]
for i in range(5):
    vet.append(input('Informe um valor: '))

print('\nVetor')
for i in range(5):
    print(vet[i])

print('\nVetor')
print(vet)

###################################
vet=[]

N= int(input('Entre com uma quantidade:'))

for i in range (N):
    vet.append(int(input('Entre com um numero: ')))

print('\nVetor')
for i in range (N):
    print(vet(N))

#####################################
vet=[]
n=int(input('Entre com uma quantidade '))
quant=0
for i in range (n):
   vet.append(int((input('Entre com um valor'))))
   if vet[i]%2==0:
    soma=0
    soma=soma+vet[i]
    quant=quant+1

media=soma/quant
print(media)

###########################################

def receba():
    x=int(input('Entre com um valor:'))
    y=int(input('Entre com outro valor: '))
    resp=exibicao(x,y)
    print('O menor é:%d'%resp   )

def exibicao(x,y):  
    
    if x<y:
        return x
    elif x>y:
        return y
    elif x==y:
        print('Iguais')
        
#############################
def vetor(vet):
    soma=0
    for i in range (2):
        soma+=vet[i]
    return soma
    
vet=[]
for i in range (2):
    vet.append(int(input('Entre com valores')))
        
 
print(soma(vet))

############################################
def vetor(vet):
    soma=0
    media=0
    for i in range (2):
        soma+=vet[i]
        media=soma/2
    return media
    
vet=[]
for i in range (2):
    vet.append(int(input('Entre com valores')))
        
 
print(vetor(vet))

#################
opc=int(input("Escolha uma opção de 1 a 3 para realizar operações: 1-Tabuada, 2-Imc, 3-Fatorial. Digite -1 para sair"))
def pereba():
    while opc!=-1:
        if opc==1:
            n=int(input('Insira um número: '))
            tabuada(n)
        elif opc==2:
            peso=int(input('Entre com seu peso: '))
            altura=float(input('Entre com sua altura: '))
            calculo=soma
            resp= imc(peso,altura)
        elif opc==3:
            n=int(input('Insira um número:'))
            fatorial(n)
    else:
        print('saida')


def tabuada(x):
    for i in range (11):
        print(n,'*',i,'=',n*i)


def imc(x,y):
    calc=x/(y**2)
    return calc
    
def fatorial(x):
    mult=x
    for x in range (x,1,-1):
        mult=mult*x

    print(mult)

    ###########################################

def principal():
        n=int(input('Insira um numero:'))
        somatoria(n)

def somatoria(n):
    a=1
    somatot1=0
    somatot2=0
    for a in range (a,n,1):
        soma=0
        soma2=0
        soma=soma+a
        soma2=soma2+(a*a)
        print(soma,'/',soma2)
        somatot1=(somatot1+soma)
        somatot2=(somatot2+soma2)
        print(somatot1,'/',somatot2)

principal()
#####################################################
palavras=[]
with open("palavras.txt", "r",encoding="utf-8")as arquivo:
    for linha in arquivo:
        linha=linha.strip()
        palavras.append(linha)

print(palavras)
print(palavras[1].upper())
################################################################
vetidade=[]
vetpessoas=[]

for i in range (3):
    n=int(input('Entre com valores: '))
    vet.append(input('Insira o nome de Pessoas'))
    if n<=0:
        print('Opção inválida')
    vetidade.append(n)
media=0
mediatot=0
for i in range (3):
    media=media+vetidade[i]
mediatot=media/3
print('A média é %d'%(mediatot))

quant=0
for i in range (3):
    if vet[i]>mediatot:
        quant=quant+1
print('A quantidade de pessoas é %d'%(quant))

for i in range (3):
    if vet[i]<mediatot:
        





