import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction


def spline(x, y):
    n = len(x)
    a={k: v for k,v in enumerate(y)}
    h={k: x[k+1]- x[k] for k in range(n - 1)}

    A = [[1] + [0]* (n - 1)]
    for i in range(1, n - 1):
        row = [0] * n
        row[i - 1] = h[i - 1]
        row[i] = 2*(h[i - 1] + h[i])
        row[i + 1] = h[i]
        A.append(row)
    A.append( [0] * (n - 1) + [1])

    B= [0]

    for k in range(1, n - 1):
        row = 3 * (a[k+1] - a[k]) / h[k] - 3 * (a[k] - a[k - 1]) / h[k - 1]
        B.append(row)
    B.append(0)

    c = dict(zip(range(n), np.linalg.solve(A, B)))
    print(c)

    b={}
    d={}
    for k in range(n - 1):
        b[k] = (1/h[k]) * (a[k + 1] - a[k]) - (h[k]/3) * (2*c[k]+c[k+1])
        d[k] = (c[k+1] - c[k])/(3*h[k])

    s={}
    for k in range(n - 1):
        eq = f'{Fraction(a[k]).limit_denominator(10)} +{Fraction(b[k]).limit_denominator(10)}*(x{-x[k]:+}) +{Fraction(c[k]).limit_denominator(10)}*(x{-x[k]:+})**2 +{Fraction(d[k]).limit_denominator(10)}*(x{-x[k]:+})**3'
        s[k] = {'eq': eq, 'Dominio': [x[k], x[k+1]]}
    

    for k, v in s.items():
        print(f'S{k}',v)

    return s


x=[-2, -1, 1, 2]
y=[]
y.append( (x[0]+1)**3 )
y.append( (x[1]+1)**3 )
y.append( (x[2]-1)**2 )
y.append( (x[3]-1)**2 )

eqs = spline(x, y)

for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['Dominio'], 100)
    plt.plot(t, p(t), label=f'$S_{key}(x)$ {value["eq"]}')

# plt.scatter(x,y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Splice')
plt.xticks(x)
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.axhline(0, color='Black')
plt.axvline(0, color='Black')
plt.show()