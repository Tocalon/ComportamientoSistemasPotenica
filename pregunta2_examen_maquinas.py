
import math
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import conj
 
Potencia=5*10**6
Rin=0.002
Xin=0.05
V1_pu=1
V1nom=24.9*10**3
V2nom=7.2*10**3
a=24.9*10**3/7.2*10**3
Vg=1+1j*0


def pregunta2(potencia0, potencia1):

    valuesA = [a * (1 - 0.05),  a * (1 - 0.025),  a * 1,  a * (1 + 0.025),  a * (1 + 0.05)]
    resultV20=[]
    resultV21=[]
    for valuesA in valuesA:
        I_linea20 = potencia0 / V1nom
        Imp20 = 0.15 * 25000 + 1j * 0.6 * 25000
        Vtc20 = V1nom - (I_linea20 * Imp20 * valuesA)
        V20 = Vtc20 / V1nom
        resultV20.append(V20)
        
        I_linea21 = potencia1 / V1nom
        Imp21 = 0.15 * 25000 + 1j * 0.6 * 25000
        Vtc21 = V1nom - (I_linea21 * Imp21 * valuesA)
        V21 = Vtc21 / 24.9*10**3
        resultV21.append(V21)

    valuesA = [a * (1 - 0.05),  a * (1 - 0.025),  a * 1,  a * (1 + 0.025),  a * (1 + 0.05)]
    results30=[] 
    results31=[]
    for valuesA in valuesA:
        I_linea30 = potencia0 / V1nom
        Imp30 = 0.15 * 25000 + 1j * 0.6 * 25000
        Vtc30 = V1nom - (I_linea30 * Imp30 * valuesA)
        V30 = Vtc30 / V1nom
        results30.append(V30)
        
        I_linea31 = potencia1 / V1nom
        Imp31 = 0.15 * 25000 + 1j * 0.6 * 25000
        Vtc31 = V1nom- (I_linea31 * Imp31 * valuesA)
        V31 = Vtc31 / 24.9*10**3
        results31.append(V31)
    
    valuesA = [a * (1 - 0.05),  a * (1 - 0.025),  a * 1,  a * (1 + 0.025),  a * (1 + 0.05)]    
    result40=[]
    result41=[]
    for valuesA in valuesA:
        I_linea40 = potencia0 / V1nom
        Imp40 = 0.15 * 25000 + 1j * 0.6 * 25000
        Vtc40 = V1nom- (I_linea40 * Imp40 * valuesA)
        V40 = Vtc40 / V1nom
        result40.append(V40)
        
        I_linea41 = potencia1 / V1nom
        Imp41 = 0.15 * 25000 + 1j * 0.6 * 25000
        Vtc41 = V1nom - (I_linea41 * Imp41 * valuesA)
        V41 = Vtc41 /24.9*10**3
        result41.append(V41)
     
    valuesA = [a * (1 - 0.05),  a * (1 - 0.025),  a * 1,  a * (1 + 0.025),  a * (1 + 0.05)]   
    result50=[]
    result51=[]
    for valuesA in valuesA:
        I_linea50 = potencia0 / V1nom
        Zb20=V2nom**2/potencia0
        Ib20=V2nom/3**(1/2)*Zb20
        Imp50 = 0.15 * 25000 + 1j * 0.6 * 25000
        Vtc50 = V1nom - (I_linea50 * Imp50 * valuesA)-Ib20*Zb20
        V50 = Vtc50 / 24.9*10**3
        result50.append(V50)
        
        Zb21=V2nom**2/potencia1
        Ib21=V2nom/3**(1/2)*Zb21
        I_linea51 = potencia1 / V1nom
        Imp51 = 0.15 * 25000 + 1j * 0.6 * 25000
        Vtc51 = V1nom - (I_linea51 * Imp51 * valuesA)-Ib21*Zb21
        V51 = Vtc51 / 24.9*10**3
        result51.append(V51)
        
        
    df20=pd.DataFrame(resultV20, columns=["V20"])
    df21=pd.DataFrame(resultV21, columns=["V21"])
    df30=pd.DataFrame(results30, columns=["V30"])
    df31=pd.DataFrame(results31, columns=["V31"])
    df40=pd.DataFrame(result40, columns=["V40"])
    df41=pd.DataFrame(result41, columns=["V41"])
    df50=pd.DataFrame(result50,columns=["V50"])
    df51=pd.DataFrame(result50,columns=["V51"])
    print(df20)
    print(df21)
    print(df30)
    print(df31)
    print(df40)
    print(df41)
    print(df50)
    print(df51)
    
    
        
        
def bases1(self): #las bases necesarias para la pregunta 3 
    Ssc1=5*10**6
    Vnom1=24.9*10**3
    Zb1=Vnom1**2/Ssc1
    Ib1=Vnom1/3**(1/2)*Zb1

    Vnom2=24.9*10**3
    Zb2=Vnom2**2/Ssc1
    Ib2=Vnom2/3**(1/2)*Zb2
        
    Vnom3=7.2*10**3
    Zb3=Vnom3**2/Ssc1
    Ib3=Vnom3/3**(1/2)*Zb3

    df=pd.DataFrame({
        'Zona' : ['Zona 1', 'Zona 2', 'Zona 3'],
        'S_{base}': [Ssc1, Ssc1, Ssc1],
        'V':[Vnom1,Vnom2, Vnom3],
        'Z': [Zb1,Zb2, Zb3],
        'I':[Ib1,Ib2, Ib3]
        })


    print(df)

potencias=pregunta2(1*10**-6,5000000)
print(potencias)


