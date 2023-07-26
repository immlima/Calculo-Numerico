import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, expand, diff, nroots



t=[0,3,5,8,13,17]
s=[0,271,339,603,993,990]
v=[75,77,62,77,72,77]

ftPm=0.000189394 # Pés em Milhas
ftPkm=0.000304800097536 # Pés em Km 

ftsPmph=0.6818 # Pés por segundo em Milhas por hora
ftsPkmh=1.09728 # Pés por segundo em Km por hora
mphPkmh=1,60934 # Milhas por hora em Km por hora

grau=len(t)

##------------------------------------------------------------------------------------------------------------------------##
"""                                                        LAGRANGE                                                       """
##------------------------------------------------------------------------------------------------------------------------##

ponto=10
p=''
p_s=''
p_v=''
for i in range(grau):
    for j in range(grau):
        if i!=j:
            p+=f'(x-{t[j]})/({t[i]-t[j]})*'

    p_s+=f'({p.rstrip("*")})*{s[i]}+'
    p_v+=f'({p.rstrip("*")})*{round(v[i]*ftsPmph, 4)}+'
    p=''
p_s=p_s.rstrip("+")
p_v=p_v.rstrip("+")


def LAGRANGE_POSICAO(x):
    return eval(p_s)
def LAGRANGE_VELO(x):
    return eval(p_v)

print(f'1)' ) 
print(f'Essa é a posição estimada {LAGRANGE_POSICAO(ponto)},no ponto {ponto}, usando o interpolação de Lagrange')
print(f'Essa é a Velocidade estimada {LAGRANGE_VELO(ponto)},no ponto {ponto}, usando o interpolação de Lagrange')
print(f'')

tick = np.linspace(0, 17)

##------------------------------##

y=[]
for i in t:
    y.append(LAGRANGE_POSICAO(i))
plt.yticks(y)

plt.axhline(0, color='Black')
plt.axvline(0, color='Black')

plt.xlabel('Tempo [s]')
plt.ylabel('Distância')
plt.xticks(t)
plt.grid(True, linestyle='--', linewidth=0.5)

plt.title('Interpolação por Lagrange (Distância [Pés])')
plt.plot(tick, LAGRANGE_POSICAO(tick), label='Distância [Pés]', linewidth=1.5)
plt.legend()
plt.show()
##------------------------------##

y=[]
for i in t:
    y.append(LAGRANGE_POSICAO(i)*ftPm)
    y.append(LAGRANGE_POSICAO(i)*ftPkm)
plt.yticks(y)

plt.axhline(0, color='Black')
plt.axvline(0, color='Black')
plt.xlabel('Tempo [s]')
plt.ylabel('Distância')
plt.xticks(t)
plt.grid(True, linestyle='--', linewidth=0.5)

plt.title('Interpolação por Lagrange (Distância)')
plt.plot(tick, LAGRANGE_POSICAO(tick)*ftPm, label='Distância [Milha]', linewidth=1.5)
plt.plot(tick, LAGRANGE_POSICAO(tick)*ftPkm, label='Distância [Km]', linewidth=1.5)
plt.legend()
plt.show()

##------------------------------##

y=[]
for i in t:
    y.append(LAGRANGE_VELO(i))
    y.append(LAGRANGE_VELO(i)*0.44704)
plt.yticks(y)

plt.axhline(0, color='Black')
plt.axvline(0, color='Black')

plt.xlabel('Tempo [s]')
plt.ylabel('Velocidade')

plt.xticks(t)

plt.grid(True, linestyle='--', linewidth=0.5)

plt.title('Interpolação por Lagrange (Velocidade)')
plt.plot(tick, LAGRANGE_VELO(tick), label='Velocidade [Milhas/h]', linewidth=1.5)
plt.plot(tick, LAGRANGE_VELO(tick)*0.44704, label='Velocidade [km/h]', linewidth=1.5)
plt.legend()
plt.show()


# ##------------------------------------------------------------------------------------------------------------------------##
# """                                                            NEWTON                                                    """
# ##------------------------------------------------------------------------------------------------------------------------##

ponto=15
def Interpolacao_Newton(t, s, ponto):
    grau=len(t)
    ordem=1
    newton_posicao=[]
    newton_posicao.append(s)
    linha=[]
    for n in range(grau-1):
        for m in range(len(newton_posicao[n])-1):
            dd= ((newton_posicao[n][m+1]-newton_posicao[n][m])/(t[m+ordem]-t[m]))
            linha.append(dd)
        newton_posicao.append(linha)
        ordem+=1
        linha=[]

    p=f'{newton_posicao[0][0]}'
    for i in range(1,len(newton_posicao)):
        p+=f'+({round(newton_posicao[i][0], 4) })'
        for j in range(i):
            p+=f'*(x-({t[j]}))'
    

    def NEWTON_POSICAO(x):
        return eval(p)
    return NEWTON_POSICAO(ponto)

print(f'2)' ) 
print(f'Essa é a Posição estimada: {Interpolacao_Newton(t,s,ponto)},no ponto {ponto}, usando o interpolação de Newton')
print(f'Essa é a Velocidade estimada: {Interpolacao_Newton(t,v,ponto)},no ponto {ponto}, usando o interpolação de Newton')
print(f'')


tick = np.linspace(0, 17)
##------------------------------##
plt.title('Interpolação por Newton (Distância [Pés])')

y=[]
for i in t:
    y.append(Interpolacao_Newton(t,s,i))
y.append(Interpolacao_Newton(t,s,ponto))
plt.yticks(y)

plt.axhline(0, color='Black')
plt.axvline(0, color='Black')

plt.xlabel('Tempo [s]')
plt.ylabel('Distância [Pés]')
plt.xticks(t)
plt.grid(True, linestyle='--', linewidth=0.5)

plt.plot(tick, Interpolacao_Newton(t,s,tick), label='Distância [Pés]', linewidth=1.5)
plt.plot(ponto, Interpolacao_Newton(t,s,ponto), label=f'P( {ponto} , {round(Interpolacao_Newton(t,s,ponto), 3) } )', color='green', marker='o' )

plt.legend()
plt.show()

##------------------------------##
plt.title('Interpolação por Newton (Distância)')

y=[]
for i in t:
    y.append(round(Interpolacao_Newton(t,s,i)*ftPm, 3))
    y.append(round(Interpolacao_Newton(t,s,i)*ftPkm, 3))
y.append(round(Interpolacao_Newton(t,s,ponto)*ftPm, 3))
y.append(round(Interpolacao_Newton(t,s,ponto)*ftPkm, 3))

plt.yticks(y)

plt.axhline(0, color='Black')
plt.axvline(0, color='Black')
plt.xlabel('Tempo [s]')
plt.ylabel('Distância')
plt.xticks(t)
plt.grid(True, linestyle='--', linewidth=0.5)

plt.plot(tick, Interpolacao_Newton(t,s,tick)*ftPm, label='Distância [Milha]', linewidth=1.5)
plt.plot(ponto, Interpolacao_Newton(t,s,ponto)*ftPm, label=f'P( {ponto} , {round(Interpolacao_Newton(t,s,ponto)*ftPm, 3)} )', color='green', marker='o' )

plt.plot(tick, Interpolacao_Newton(t,s,tick)*ftPkm, label='Distância [Km]', linewidth=1.5)
plt.plot(ponto, Interpolacao_Newton(t,s,ponto)*ftPkm, label=f'P( {ponto} , {round(Interpolacao_Newton(t,s,ponto)*ftPkm, 3)} )', color='red', marker='o' )

plt.legend()
plt.show()

##------------------------------##
plt.title('Interpolação por Newton (Velocidade)')

y=[]
for i in t:
    y.append(Interpolacao_Newton(t,v,i)*ftsPmph)
    y.append(Interpolacao_Newton(t,v,i)*ftsPkmh)
y.append(Interpolacao_Newton(t,v,ponto)*ftsPmph)
y.append(Interpolacao_Newton(t,v,ponto)*ftsPkmh)
plt.yticks(y)

plt.axhline(0, color='Black')
plt.axvline(0, color='Black')

plt.xlabel('Tempo [s]')
plt.ylabel('Velocidade')

plt.xticks(t)

plt.grid(True, linestyle='--', linewidth=0.5)

plt.plot(tick, Interpolacao_Newton(t,v,tick)*ftsPmph, label='Velocidade [Milhas/h]', linewidth=1.5)
plt.plot(ponto, Interpolacao_Newton(t,v,ponto)*ftsPmph, label=f'P( {ponto} , {round(Interpolacao_Newton(t,v,ponto)*ftsPmph, 1)} )', color='green', marker='o' )

plt.plot(tick, Interpolacao_Newton(t,v,tick)*ftsPkmh, label='Velocidade [km/h]', linewidth=1.5)
plt.plot(ponto, Interpolacao_Newton(t,v,ponto)*ftsPkmh, label=f'P( {ponto} , {round(Interpolacao_Newton(t,v,ponto)*ftsPkmh, 1)} )', color='red', marker='o' )

plt.legend()
plt.show()

##------------------------------------------------------------------------------------------------------------------------##
"""                                                            Hermite                                                    """
## ------------------------------------------------------------------------------------------------------------------------##

ponto=3

t2=[]

def Polinomio_Hermite(t, s, ponto):
    grau=len(t)
    hermite_tabela=[]
    linha=[]
    for i in range(grau):
        linha.append(s[i])
        linha.append(s[i])
    hermite_tabela.append(linha)

    linha=[]
    for i in range(grau):
        t2.append(t[i])
        t2.append(t[i])

    linha=[]

    for i in range(2*grau-1):
        if i % 2==0:
            linha.append(v[int(i/2)])
        else:
            dd= ((hermite_tabela[0][i+1]-hermite_tabela[0][i])/(t2[i+1]-t2[i]))
            linha.append(dd)  

    hermite_tabela.append(linha)

    ordem=2
    linha=[]
    for n in range(1,2*grau-1):
        for m in range(len(hermite_tabela[n])-1):
            dd= ((hermite_tabela[n][m+1]-hermite_tabela[n][m])/(t2[m+ordem]-t2[m]))
            linha.append(dd)
        hermite_tabela.append(linha)
        ordem+=1
        linha=[]

    # print(hermite_tabela)
    p=f'{hermite_tabela[0][0]}'

    for i in range(1,len(hermite_tabela)):
        p+=f'+({hermite_tabela[i][0]})'  
        for j in range(i):
            p+=f'*(x-({t2[j]}))'

    # print(p)
    X = symbols('x')
    p=expand(p.replace('x',f'{X}'))
    print(p)
    
    pd = diff(p)
    # print(pd)

    pdd = diff(pd)
    # print(pdd)

    Maior55=0
    possiveis_Maior55= nroots(f'{pd-(55/ftsPmph)}')
    for i in range(len(possiveis_Maior55)):
        if possiveis_Maior55[i]>0:
            Maior55=possiveis_Maior55[i] 
            tMaior55=len(possiveis_Maior55)-(i+1)
            break

    def hermite_eval(x):
        return [eval(str(p)), eval(str(pd)), eval(str(pdd)) ]
                

    possiveis_pontos = nroots(f'{pdd}')
    possiveis_pontos.append(0)
    possiveis_pontos.append(17)
    
    possiveis_max=[]
    for i in range(len(possiveis_pontos)):
        if possiveis_pontos[i]>0:
            # print(possiveis_pontos[i])
            possiveis_max.append( hermite_eval(possiveis_pontos[i])[1] )

    # print(possiveis_max) 
    # print(np.amax(possiveis_max)) 
    # print(possiveis_max.index(np.amax(possiveis_max)))
    # print(possiveis_pontos[possiveis_max.index(np.amax(possiveis_max))])

   
    return [hermite_eval(ponto), 
                [Maior55, tMaior55 ],
                [possiveis_pontos[ possiveis_max.index( np.amax(possiveis_max) )], np.amax(possiveis_max) ]
            ]

tick = np.linspace(0, 17)
##------------------------------##
plt.title('Interpolação por Hermite')

y=[]
# for i in t:
#     y.append(Polinomio_Hermite(t,s,i))
# # y.append(Polinomio_Hermite(t,s,ponto))
# plt.yticks(y)

plt.axhline(0, color='Black')
plt.axvline(0, color='Black')

plt.xlabel('Tempo [s]')
plt.ylabel('Distância [Pés]')
plt.xticks(t)
plt.grid(True, linestyle='--', linewidth=0.5)

# print(Polinomio_Hermite(t,s,tick))
plt.plot(tick, Polinomio_Hermite(t,s,tick)[0][0], label='Distância [Pés]', linewidth=1.5)
plt.plot(tick, Polinomio_Hermite(t,s,tick)[0][1], label='Velocidade [Pés/s]', linewidth=1.5)
plt.plot(Polinomio_Hermite(t,s,ponto)[2][0], Polinomio_Hermite(t,s,ponto)[2][1], label=f'P( {Polinomio_Hermite(t,s,ponto)[2][0]} , {round(Polinomio_Hermite(t,s,ponto)[2][1], 3) } )', color='red', marker='o' )
plt.plot(Polinomio_Hermite(t,s,ponto)[1][0], 55, label=f'P( {Polinomio_Hermite(t,s,ponto)[1][0]} , 55 )', color='blue', marker='o' )


print(f'3)' ) 
print(f'Primeira vez que o carro passa de 55 Milhas/h foi aos {Polinomio_Hermite(t,s,ponto)[1][0]} segundos e ocorre mais {Polinomio_Hermite(t,s,ponto)[1][1]} vezes' )
print(f'')
print(f'4)' ) 
print(f'A velocidade máxima estimada para o carro foi {Polinomio_Hermite(t,s,ponto)[2][1]*ftsPmph} Milhas/h no {Polinomio_Hermite(t,s,ponto)[2][0]} segundos' )
print(f'')

plt.legend()
plt.show()


##------------------------------------------------------------------------------------------------------------------------##
"""                                                            Comparaçao                                                 """
## ------------------------------------------------------------------------------------------------------------------------##

plt.title('Distância [Milha]')

plt.axhline(0, color='Black')
plt.axvline(0, color='Black')

plt.xlabel('Tempo [s]')
plt.ylabel('Distância [Pés]')
plt.xticks(t)
plt.grid(True, linestyle='--', linewidth=0.5)


plt.plot(tick, LAGRANGE_POSICAO(tick), label='Lagrange [Pés]', linewidth=5)
plt.plot(tick, Interpolacao_Newton(t,s,tick), label='Newton [Pés]', linewidth=1.5)
plt.plot(tick, Polinomio_Hermite(t,s,tick)[0][0], label='Hermite [Pés]', linewidth=1.5, color='red')

plt.legend()
plt.show()

#----------------------------------------------------#
plt.title('Distância [Milha]')

plt.axhline(0, color='Black')
plt.axvline(0, color='Black')

plt.xlabel('Tempo [s]')
plt.ylabel('Distância [Milha]')
plt.xticks(t)
plt.grid(True, linestyle='--', linewidth=0.5)

plt.plot(tick, LAGRANGE_POSICAO(tick)*ftPm, label='Lagrange [Milha]', linewidth=5)
plt.plot(tick, Interpolacao_Newton(t,s,tick)*ftPm, label='Newton [Milha]', linewidth=1.5)
plt.plot(tick, Polinomio_Hermite(t,s,tick)[0][0]*ftPm, label='Hermite [Milha]', linewidth=1.5, color='red')

plt.legend()
plt.show()

#----------------------------------------------------#

plt.title('Distância [Km]')

plt.axhline(0, color='Black')
plt.axvline(0, color='Black')

plt.xlabel('Tempo [s]')
plt.ylabel('Distância [Km]')
plt.xticks(t)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.plot(tick, LAGRANGE_POSICAO(tick)*ftPkm, label='Lagrange [Km]', linewidth=5)
plt.plot(tick, Interpolacao_Newton(t,s,tick)*ftPkm, label='Newton [Km]', linewidth=1.5)
plt.plot(tick, Polinomio_Hermite(t,s,tick)[0][0]*ftPkm, label='Hermite [Km]', linewidth=1.5, color='red')

plt.legend()
plt.show()

#----------------------------------------------------#

plt.title('Velocidade [Milhas/h]')

plt.axhline(0, color='Black')
plt.axvline(0, color='Black')

plt.xlabel('Tempo [s]')
plt.ylabel('Velocidade [Milhas/h]')
plt.xticks(t)

plt.plot(tick, LAGRANGE_VELO(tick)*ftsPmph, label='Lagrange [Milhas/h]', linewidth=5)
plt.plot(tick, Interpolacao_Newton(t,v,tick)*ftsPmph, label='Newton [Milhas/h]', linewidth=1.5)
plt.plot(tick, Polinomio_Hermite(t,s,tick)[0][1]*ftsPmph, label='Hermite [Milhas/h]', linewidth=1.5, color='red')

plt.legend()
plt.show()
