import os
import matplotlib.pyplot as plt

A=[ [5,3,-2,1],
    [1,-4,2,3],
    [1,2,-3,1],
    [2,1,-2,3]]

b=[-6,10,-10,-7]

e=10**-15

x=[0,0,0,0]
xm1=[0,0,0,0]
txt=""

#----------------Jacobi--------------#
txt=txt+"#----------------Jacobi--------------#\n"
interacao_jacobi=0
eixo_grafico_x=[0]
eixo_grafico_x0=[0]
eixo_grafico_x1=[0]
eixo_grafico_x2=[0]
eixo_grafico_x3=[0]
# print(f"i:{interacao_jacobi} | x0={x[0]} x1={x[1]} x2={x[2]} x3={x[3]} ")
txt=txt+f"i:{interacao_jacobi} | x0={x[0]} x1={x[1]} x2={x[2]} x3={x[3]} \n"
while (1):
    interacao_jacobi=interacao_jacobi+1
    x[0]=(b[0]                 -A[0][1]*xm1[1] -A[0][2]*xm1[2] -A[0][3]*xm1[3])/A[0][0]
    x[1]=(b[1] -A[1][0]*xm1[0]                 -A[1][2]*xm1[2] -A[1][3]*xm1[3])/A[1][1]
    x[2]=(b[2] -A[2][0]*xm1[0] -A[2][1]*xm1[1]                 -A[2][3]*xm1[3])/A[2][2]
    x[3]=(b[3] -A[3][0]*xm1[0] -A[3][1]*xm1[1] -A[3][2]*xm1[2]                )/A[3][3]
    
    eixo_grafico_x.append(interacao_jacobi)
    eixo_grafico_x0.append(x[0])
    eixo_grafico_x1.append(x[1])
    eixo_grafico_x2.append(x[2])
    eixo_grafico_x3.append(x[3])
 
    txt=txt+f"i:{interacao_jacobi} | x0={x[0]} x1={x[1]} x2={x[2]} x3={x[3]} | Erro x0={abs(xm1[0]-x[0])} x1={abs(xm1[1]-x[1])} x2={abs(xm1[2]-x[2])} x3={abs(xm1[3]-x[3])}\n"
    # print(f"i:{interacao_jacobi} | x0={x[0]} x1={x[1]} x2={x[2]} x3={x[3]} ")
    # print(f"| Erro x0={abs(xm1[0]-x[0])} x1={abs(xm1[1]-x[1])} x2={abs(xm1[2]-x[2])} x3={abs(xm1[3]-x[3])}")
    # print('')
    if (abs(xm1[0]-x[0])<e and abs(xm1[1]-x[1])<e and abs(xm1[2]-x[2])<e and abs(xm1[3]-x[3])<e):
        x=[0,0,0,0]
        break    
    else:
        xm1=x
        x=[0,0,0,0]

print(f"N° de interações : {interacao_jacobi}")

plt.plot(eixo_grafico_x,eixo_grafico_x0, lw=1, color='red', marker='.',label='X₁')
plt.plot(eixo_grafico_x,eixo_grafico_x1, lw=1, color='blue', marker='.',label='X₂')
plt.plot(eixo_grafico_x,eixo_grafico_x2, lw=1, color='yellow', marker='.',label='X₃')
plt.plot(eixo_grafico_x,eixo_grafico_x3, lw=1, color='green', marker='.',label='X₄')

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Jacobi')
plt.xticks(x)
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.axhline(0, color='Black')
plt.axvline(0, color='Black')
plt.show()


#----------------Gauss-Seidel--------------#
txt=txt+"\n\n#----------------Gauss-Seidel--------------#\n"
interacao_Seidel=0
xm1=[0,0,0,0] 
x=[0,0,0,0] 
eixo_grafico_x=[0]
eixo_grafico_x0=[0]
eixo_grafico_x1=[0]
eixo_grafico_x2=[0]
eixo_grafico_x3=[0]
# print(f"i:{interacao_Seidel} | x0={x[0]} x1={x[1]} x2={x[2]} x3={x[3]} ")
# print('')
txt=txt+f"i:{interacao_Seidel} | x0={x[0]} x1={x[1]} x2={x[2]} x3={x[3]} \n"
while (1):
    interacao_Seidel=interacao_Seidel+1
    
    x[0]=(b[0]               -A[0][1]*xm1[1] -A[0][2]*xm1[2] -A[0][3]*xm1[3])/A[0][0]
    x[1]=(b[1] -A[1][0]*x[0]                 -A[1][2]*xm1[2] -A[1][3]*xm1[3])/A[1][1]
    x[2]=(b[2] -A[2][0]*x[0] -A[2][1]*x[1]                   -A[2][3]*xm1[3])/A[2][2]
    x[3]=(b[3] -A[3][0]*x[0] -A[3][1]*x[1]   -A[3][2]*x[2]                  )/A[3][3]

    eixo_grafico_x.append(interacao_Seidel)
    eixo_grafico_x0.append(x[0])
    eixo_grafico_x1.append(x[1])
    eixo_grafico_x2.append(x[2])
    eixo_grafico_x3.append(x[3])
    
    txt=txt+f"i:{interacao_Seidel} | x0={x[0]} x1={x[1]} x2={x[2]} x3={x[3]} | Erro x0={abs(xm1[0]-x[0])} x1={abs(xm1[1]-x[1])} x2={abs(xm1[2]-x[2])} x3={abs(xm1[3]-x[3])}\n"

    # print(f"i:{interacao_Seidel} | x0={x[0]} x1={x[1]} x2={x[2]} x3={x[3]}  {xm1}")
    # print(f"| Erro x0={abs(xm1[0]-x[0])} x1={abs(xm1[1]-x[1])} x2={abs(xm1[2]-x[2])} x3={abs(xm1[3]-x[3])}")
    # print('')

    if (abs(xm1[0]-x[0])<e and abs(xm1[1]-x[1])<e and abs(xm1[2]-x[2])<e and abs(xm1[3]-x[3])<e):
        break    
    else:
        xm1=x
        x=[0,0,0,0]

print(f"N° de interações : {interacao_Seidel}")

plt.plot(eixo_grafico_x,eixo_grafico_x0, lw=1, color='red', marker='.',label='X₁')
plt.plot(eixo_grafico_x,eixo_grafico_x1, lw=1, color='blue', marker='.',label='X₂')
plt.plot(eixo_grafico_x,eixo_grafico_x2, lw=1, color='yellow', marker='.',label='X₃')
plt.plot(eixo_grafico_x,eixo_grafico_x3, lw=1, color='green', marker='.',label='X₄')

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gauss-Seidel')
plt.xticks(x)
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.axhline(0, color='Black')
plt.axvline(0, color='Black')
plt.show()
#----------------SOR--------------#

#fdeRelaxamento=[1.2 , 1.1955]
fdeRelaxamento=[1.16 , 1.18, 1.19, 1.1955, 1.2, 1.22, 1.24]

# print(f"i:{interacao_SOR} | x0={x[0]} x1={x[1]} x2={x[2]} x3={x[3]} ")
# print('')
for w in fdeRelaxamento:
    txt=txt+"\n\n#----------------SOR--------------#\n"
    interacao_SOR=0
    xm1=[0,0,0,0] 
    x=[0,0,0,0] 
    eixo_grafico_x=[0]
    eixo_grafico_x0=[0]
    eixo_grafico_x1=[0]
    eixo_grafico_x2=[0]
    eixo_grafico_x3=[0]
    txt=txt+f"i com w={w} :{interacao_SOR} | x0={x[0]} x1={x[1]} x2={x[2]} x3={x[3]} | R1={b[0]} R2={b[1]} R3={b[2]} R4={b[3]}\n\n"
    while (1):
        interacao_SOR=interacao_SOR+1
        
        R1=(b[0] -A[0][0]*xm1[0] -A[0][1]*xm1[1] -A[0][2]*xm1[2] -A[0][3]*xm1[3])
        x[0]=xm1[0]+(w/A[0][0])*R1

        R2=(b[1] -A[1][0]*x[0]   -A[1][1]*xm1[1] -A[1][2]*xm1[2] -A[1][3]*xm1[3])
        x[1]=xm1[1]+(w/A[1][1])*R2

        R3=(b[2] -A[2][0]*x[0]   -A[2][1]*x[1]   -A[2][2]*xm1[2] -A[2][3]*xm1[3])
        x[2]=xm1[2]+(w/A[2][2])*R3

        R4=(b[3] -A[3][0]*x[0]   -A[3][1]*x[1]   -A[3][2]*x[2]   -A[3][3]*xm1[3])
        x[3]=xm1[3]+(w/A[3][3])*R4

        eixo_grafico_x.append(interacao_SOR)
        eixo_grafico_x0.append(x[0])
        eixo_grafico_x1.append(x[1])
        eixo_grafico_x2.append(x[2])
        eixo_grafico_x3.append(x[3])
        
        txt=txt+f"""i com w={w} :{interacao_SOR} | x0={x[0]} x1={x[1]} x2={x[2]} x3={x[3]} | R1={R1} R2={R2} R3={R3} R4={R4}
Erro x0={abs(xm1[0]-x[0])} x1={abs(xm1[1]-x[1])} x2={abs(xm1[2]-x[2])} x3={abs(xm1[3]-x[3])}\n
"""

        # print(f"i:{interacao_SOR} | x0={x[0]} x1={x[1]} x2={x[2]} x3={x[3]}  {xm1}")
        # print(f"Erro x0={abs(xm1[0]-x[0])} x1={abs(xm1[1]-x[1])} x2={abs(xm1[2]-x[2])} x3={abs(xm1[3]-x[3])}")
        # print('')

        if (abs(xm1[0]-x[0])<e and abs(xm1[1]-x[1])<e and abs(xm1[2]-x[2])<e and abs(xm1[3]-x[3])<e):    
            break
        else:
            xm1=x
            x=[0,0,0,0]
    print(f"N° de interações com w={w} : {interacao_SOR}")
    plt.plot(eixo_grafico_x,eixo_grafico_x0, lw=1, color='red', marker='.',label='X₁')
    plt.plot(eixo_grafico_x,eixo_grafico_x1, lw=1, color='blue', marker='.',label='X₂')
    plt.plot(eixo_grafico_x,eixo_grafico_x2, lw=1, color='yellow', marker='.',label='X₃')
    plt.plot(eixo_grafico_x,eixo_grafico_x3, lw=1, color='green', marker='.',label='X₄')

    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title(f'SOR com w={w}')
    plt.xticks(x)
    plt.legend()
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.axhline(0, color='Black')
    plt.axvline(0, color='Black')
    plt.show()



if os.path.exists(os.path.join(".","Saida.txt")):
    os.remove(os.path.join(".","Saida.txt"))
with open(os.path.join(".","Saida.txt"),"w",encoding='utf8') as my_file:
    my_file.write(txt)