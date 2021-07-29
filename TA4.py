# Heat Transfer

import matplotlib.pyplot as plt
from math import pi

'''
x1 = float(input("x1(m) = "))
x2 = float(input("x2(m) = "))

T1 = int(input("T1(K) = "))
T2 = int(input("T2(K) = "))

D = float(input("D(m) = "))
A = (pi * D **2)/4

k = {
    "Copper"            : 400,
    "Aluminum"          : 250,
    "Silver"            : 420,
    "Platinum"          : 70,
    "Iron"              : 60,
    "Stainless Steel"   : 20
}
# key:value
#k.update(Gold = 320)
k["Gold"] = 320

Q = {}

for i in k.keys(): # i=0,1,2,..
    Q[i] = (2 * k[i] * A * (T1 - T2))/(x2 - x1)
    plt.plot(k[i],Q[i],"*",label=i)

plt.legend()
plt.show()
'''


def Q_in(A, x1, x2, T1, T2, k):
    return (2 * k * A * (T1 - T2))/(x2 - x1)

def PlotQ():
    x1 = float(input("x1(m) = "))
    x2 = float(input("x2(m) = "))

    T1 = int(input("T1(K) = "))
    T2 = int(input("T2(K) = "))

    D = float(input("D(m) = "))
    A = (pi * D **2)/4

    k = {
        "Copper"            : 400,
        "Aluminum"          : 250,
        "Silver"            : 420,
        "Platinum"          : 70,
        "Iron"              : 60,
        "Stainless Steel"   : 20
    }
    # key:value
    #k.update(Gold = 320)
    k["Gold"] = 320

    Q = {}

    for i in k.keys(): # i=0,1,2,..
        Q[i] = Q_in(A, x1, x2, T1, T2, k[i])
        plt.plot(k[i],Q[i],"*",label=i)
        plt.xlabel("k (W/m.K) ", fontsize = 12)
        plt.ylabel("Q (W)", fontsize = 12)
    plt.legend(fontsize = 10)
    plt.show()
    plt.title("Heat Transfer", fontsize = 11)
    plt.xlim(xmin = 0)
    plt.ylim(ymin = 0)
    plt.grid()
    plt.show() 


PlotQ()