import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

A=[]
B=[]


"""
S0(x0)=f(x0)
S0(-2)=f(x=-2)=((-2)+)**3= -1

S1(x1)=f(x1)
S1(-2)=f(x=-1)
a(-1)**3 + b(-1)**2 + c(-1) + d 

-a + b - c + d = 0
"""

A.append([-1,1,-1,1])
B.append(0)

"""
DERIVADAS

S0'(x)=3*(x+1)**2
S0''(x)=6*(x+1)

S1'(x)=3*a(x)**2 + 2*b*(x) + c
S1''(x)=6*a(x) + 2*b

S2'(x)=2*(x-1)
S2''(x)=2
"""

"""(1)
S0(x1)=S1(x1)
0=-a + b - c + d
S1(x2)=S2(x2)
a*(1)**3 + b*(1)**2 - c*(1) + d

a + b + c + d = 0

"""
#####
A.append([1,1,1,1])
B.append(0)


"""(2)
S0'(x1)=S1'(x1)
3*(x1+1)**2 = 3*a(x1)**2 + 2*b*(x1) + c
3*((-1)+1)**2=3*a((-1))**2 + 2*b*((-1)) + c
 
3*a -2*b +c = 0
"""
####
# A.append([3,-2,1,0])
# B.append(0)

"""
S1'(x2)=S2'(x2)
3*a(x)**2 + 2*b*(x) + c = 2*(x-1)
3*a(2)**2 + 2*b*(2) + c =2*((2)-1)

 
3*a +2*b +c = 0
"""
A.append([3,2,1,0])
B.append(0)




"""(3)
S0''(x1) = S1''(x1)
6*(x+1) = 6*a(x) + 2*b
6*((1)+1) = 6*a(-1) + 2*b
0 = -6*a + 2*b
"""

####
A.append([-6,2,0,0])
B.append(0)

"""
S1''(x2) = S2''(x2)
6*a(1) + 2*b = 2 

6*a(1) + 2*b = 2
"""
####
# A.append([6,2,0,0])
# B.append(2)



# print(A)
# print(B)

plt.axhline(0, color='Black')
plt.axvline(0, color='Black')

s={}
x=[-2, -1, 1, 2]

coef=np.linalg.solve(A, B)

eq = f'(x+1)**3'
s[0] = {'eq': eq, 'Dominio': [x[0], x[1]]}

eq = f'({Fraction(coef[0]).limit_denominator(10)})*(x)**3 +({Fraction(coef[1]).limit_denominator(10)})*(x)**2 +({Fraction(coef[2]).limit_denominator(10)})*(x) +({Fraction(coef[3]).limit_denominator(10)})'
s[1] = {'eq': eq, 'Dominio': [x[1], x[2]]}

eq = f'(x-1)**2'
s[2] = {'eq': eq, 'Dominio': [x[2], x[3]]}

for k, v in s.items():
    print(f'S{k}',v)

for key, value in s.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['Dominio'], 100)
    plt.plot(t, p(t), label=f'$S_{key}(x)$={value["eq"]}', linewidth=1.5)

# plt.scatter(x,y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Interpolação por Spline Cúbica')
plt.xticks(x)
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.figtext(0.5, 0.0099, f"Os coeficientes são: a = {Fraction(coef[0]).limit_denominator(10)}, b = {Fraction(coef[1]).limit_denominator(10)}, c = {Fraction(coef[2]).limit_denominator(10)}, d = {Fraction(coef[3]).limit_denominator(10)}", ha="center", fontsize=10, bbox={"alpha":0.5, "pad":5})

plt.show()