import matplotlib.pyplot as plt
from numpy import *
import numpy as np
import os

#Original
A=[
[2.94,2.87,2.33,-2.96],
[1.48, 2.48,2.80, -1.52],
[6.31,-7.05,2.98,7.65],
[8.27,8.39,8.64,1.98]]
b=[[5.30], [7.88], [8.67], [5.73]]

NxM=len(A[0])
U = A
L = np.zeros([NxM, NxM])

def print_L(L):
    NxM=len(L[0])
    for x in range(NxM):
        L[x, x] = 1
    return L

txt=f"""Trabalho 1 - Decomposição LU
Alunos: Mateus Lima Pinho
        Sabrina Costa Faria

# ------------------------------# 
Matriz L
{L}

Matriz U
{np.array(matrix(U))}

Vetor b
{np.array(matrix(b))}
"""

for k in range(0, NxM):
    maior=None
    for s in range(k, NxM):
        if (k<=s):
            if maior!=None:
                if abs(U[s][k])>abs(U[maior][k]):
                    maior=s       
            else:
                maior=s
    if k!=maior:
        txt=txt+f"""\nTroca de linha L{k+1}  por L{maior+1}"""
        AUX=U[k]
        U[k]=U[maior]
        U[maior]=AUX    

        L[[k, maior]] = L[[maior, k]]

        AUX=b[k]
        b[k]=b[maior]
        b[maior]=AUX
                    
        txt=txt+f"""
Pivo = {A[k][k]}
Matriz L
{L}
Matriz U
{np.array(matrix(U))}
Vetor b
{np.array(matrix(b))}

"""


    for lin in range(0, NxM):
        
        if (k<lin):

            m = round(float(A[lin][k]/A[k][k]),3) 
            L[lin][k] = m
            for col in range(0, NxM):
                A[lin][col] = round(float(A[lin][col] - (m*A[k][col])), 2)
                b[lin][0] = round(float(b[lin][0] - (m*b[k][0])), 2)
                U[lin][col] = round(float(A[lin][col]), 2)
            
            txt=txt+f"""
# {k+1}° Interação---------------# 
Pivo = {A[k][k]}
m = {m}
Matriz L
{L}
Matriz U
{np.array(matrix(U))}
Vetor b
{np.array(matrix(b))}
"""

txt=txt+f"""
# ------------------------------# 
Matriz L
{print_L(L)}
Matriz U
{np.array(matrix(U))}
Vetor b
{np.array(matrix(b))}
"""

y=np.zeros(NxM)
for i in range (0,NxM):
    soma=0
    for j in range (0,NxM):
        soma+= L[i][j]*y[j]
    y[i]=float('%.3f'%((b[i]-soma)/L[i][i]) )

x=np.zeros(NxM)
for i in range (NxM-1,-1,-1):
    soma=0
    for j in range (0, NxM):
        soma+= U[i][j]*x[j]
    x[i]=float('%.3f'%((y[i]-soma)/U[i][i]) )

x = np.flip(x)
txt=txt+f"""
x= 
{ x }

y= 
{ y }
"""

x, y = zip(*sorted(zip(x, y)))

with open(os.path.join(".","Saida.txt"),"w",encoding='utf8') as my_file:
    my_file.write(txt)

plt.plot(x,y, lw=1, color='red', marker='.',)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Decomposição LU')
plt.xticks(x)
plt.yticks(y)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.axhline(0, color='Black')
plt.axvline(0, color='Black')
plt.show()