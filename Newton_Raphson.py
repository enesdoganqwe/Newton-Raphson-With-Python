import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import math

x = sym.Symbol("x")

def turev(fx):
    df = sym.diff(fx)
    ddf  = sym.diff(df)
    return df,ddf

def cizim():
    noktalar = np.linspace(0.5,3,50)
    y = []
    y_df = []
    for x in noktalar:
        fx = (x-1)**2*(x-2)*(x-3)
        df = (x - 3)*(x - 2)*(2*x - 2) + (x - 3)*(x - 1)**2 + (x - 2)*(x - 1)**2
        y.append(fx)
        y_df.append(df)
    plt.scatter([1,1.6,2.637],[0,0,0])
    plt.plot(noktalar,y)
    plt.plot(noktalar,y_df,"--")
    plt.legend(["Fx","Df"])
    plt.show()

fx = (x-1)**2*(x-2)*(x-3)
df, ddf = turev(fx)

x = 3
while True:
    df = (x - 3)*(x - 2)*(2*x - 2) + (x - 3)*(x - 1)**2 + (x - 2)*(x - 1)**2
    ddf= 2*(x - 3)*(x - 2) + 2*(x - 3)*(2*x - 2) + 2*(x - 2)*(2*x - 2) + 2*(x - 1)**2
    DELTAx=-df/ddf
    x=x+DELTAx
    if abs(df)<(10**(-10)):
        df = round(df,5)
        break
    
print("En iyi x değeri = ",x)
print("Birinci türev değeri = ",df)
print("İkinci türev değeri = ",ddf)
cizim()

