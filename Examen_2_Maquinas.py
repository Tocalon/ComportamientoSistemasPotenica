import math
import os
import pandas as pd
import matplotlib.pyplot as plt
from numpy import conj, abs, sqrt
import numpy as np 

class Examen:

    def  __init__(self):
        ##### tensiones bases #########
        self.Potencia=5*10**6
        self.Rin=0.002
        self.Xin=0.05
        self.V1_pu=1
        self.V1nom=24.9*10**3
        self.V2nom=7.2*10**3
        self.a=self.V1nom/self.V2nom
        self.Xtx=1j*(5/100)
        self.Rtx=0.2/100
        
    def bases(self):
        
        self.Ssc1=5*10**6
        self.Vnom1=24.9*10**3
        self.Zb1=self.Vnom1**2/self.Ssc1
        self.Ib1=self.Ssc1/(3**(1/2))*self.V1nom

        self.V2nom=7.2*10**3
        self.Zb2=self.V2nom**2/self.Ssc1
        self.Ib2=self.Ssc1/(3**(1/2))*self.V2nom
        
        df=pd.DataFrame({
            'Zona' : ['Zona 1', 'Zona 2'],
            'S_{base}': [self.Ssc1, self.Ssc1],
            'V':[self.Vnom1,self.V2nom],
            'Z': [self.Zb1,self.Zb2],
            'I':[self.Ib1,self.Ib2]
        })


        print(df)
        
    def tensiones(self):
        
        Z12=0.15*25000+1j*0.6*25000
        Z34=0.15*25000+1j*0.6*25000
        Z3=0.15*0.001+1j*0.6*0.001
        fp=0.95
        self.Ztx_pu=self.Rtx+self.Xtx
        self.Ztx_si=self.Ztx_pu*self.Zb1
        self.S_eval=S_eval= np.arange((1*10**-6) , (5*10**6) , (0.1*10**6))
        self.S_eval_pu= self.S_eval/self.Ssc1
        
        #### Vectores de potencia real 
        self.P_vel_SI=self.S_eval*fp
        
        ####Vectores Z_load_ fp unitario 
        self.Z_un=((self.V1nom)**2)/(self.P_vel_SI)*(1+1j*(sqrt(1/1)**2)-1)
        self.Z_un_reflex=(self.a**2)*self.Z_un
        
        
        #### vectores de fp en atraso 
        self.Z_AT=((self.V1nom)**2)/(self.P_vel_SI)*(1+1j*(sqrt(1/fp)**2)-1)
        self.Z_at_reflex=(self.a**2)*self.Z_AT
        
        ###vectores de fp en adelanto
        self.Z_Ad=((self.V1nom)**2)/(self.P_vel_SI)*(1-1j*(sqrt(1/fp)**2)-1)
        self.Z_ad_reflex=(self.a**2)*self.Z_Ad
        
        
        #### sumatoria de impedancia de linea 
        self.Z_total_SI_un=Z12+Z34+self.Ztx_si+Z3+self.Z_un_reflex
        self.Z_total_SI_at=Z12+Z34+self.Ztx_si+Z3+self.Z_at_reflex
        self.Z_total_SI_ad=Z12+Z34+self.Ztx_si+Z3+self.Z_ad_reflex
        
        ####corriente 
        self.I_un_SI= self.V1nom/self.Z_total_SI_un
        v1=self.V1nom-self.I_un_SI*0
        v1_pu=abs(v1/self.V1nom)
        
        V2=v1-abs(self.I_un_SI)*Z12
        V2_pu=abs(V2/self.V1nom)
            
        V3=V2-abs(self.I_un_SI)*Z3
        V3_pu=abs(V3/self.V1nom)
        
        V4=V3-abs(self.I_un_SI)*Z34
        self.V4_pu=abs(V4/self.V1nom)
            
        V5=V4-abs(self.I_un_SI)*self.Z_total_SI_un
        self.V5pu=abs(V5/self.V1nom)
            
        plt.plot( self.S_eval_pu, v1_pu, "r",label="V1_pu")
        plt.plot( self.S_eval_pu, V2_pu, "g",label="V2_pu")
        plt.plot( self.S_eval_pu, V3_pu, "b", label="V3_pu")
        plt.plot(self.S_eval_pu, self.V4_pu, "c",label="V4_pu")
        plt.plot( self.S_eval_pu, self.V5pu, "k", label="V5pu")
        plt.xlabel("Demanda de carga (MVA)")
        plt.ylabel("Magnitud de las impedancias (pu)")
        plt.title("Gráfico de la tension (pu) en funcion de la potencia")
        plt.legend()
        plt.grid(True)
        plt.box(True)
        plt.show()
        
        
    def pregunta1B(self):
        Z12=0.15*25000+1j*0.6*25000
        Z34=0.15*25000+1j*0.6*25000
        Z3=0.15*0.001+1j*0.6*0.001
        #en atraso 
        I_at_si=self.V1nom/self.Z_total_SI_at
        #en adelanto
        I_ad_SI=self.V1nom/self.Z_total_SI_ad
        
        V1_SI_at = self.V1nom-I_at_si*0
        V2_SI_at = V1_SI_at-I_at_si*(Z12)
        V3_SI_at = V2_SI_at-I_at_si*(Z3)
        V4_SI_at = V3_SI_at-I_at_si*(Z34)
        V5_SI_at = V4_SI_at-I_at_si*(self.Ztx_si)
        
        V1_SI_ad = self.V1nom-I_ad_SI*0
        V2_SI_ad = V1_SI_ad-I_ad_SI*(Z12)
        V3_SI_ad = V2_SI_ad-I_ad_SI*(Z3)
        V4_SI_ad = V3_SI_ad-I_ad_SI*(Z34)
        V5_SI_ad = V4_SI_ad-I_ad_SI*(self.Ztx_si)
        
        V4_pu_at = abs(V4_SI_at/self.V1nom)
        V4_pu_ad = abs(V4_SI_ad/self.V1nom)

        V5_pu_at = abs(V5_SI_at/self.V1nom)
        V5_pu_ad = abs(V5_SI_ad/self.V1nom)
            
        plt.plot(self.S_eval_pu, V4_pu_at, 'b', label='V4_0.95_atraso')
        plt.plot(self.S_eval_pu, self.V4_pu, 'r', label='V4_unitario')
        plt.plot(self.S_eval_pu, V4_pu_ad, 'g', label='V4_0.95_adelanto')
        plt.title('Tensiones V4 según fp')
        plt.xlabel('Sload (pu)')
        plt.ylabel('Tensión (pu)')
        plt.legend()
        plt.grid(True)
        plt.box(True)
        plt.show()

        plt.plot(self.S_eval_pu, V5_pu_at, 'b', label='V5_0.95_atraso')
        plt.plot(self.S_eval_pu, self.V5pu, 'r', label='V5_unitario')
        plt.plot(self.S_eval_pu, V5_pu_ad, 'g', label='V5_0.95_adelanto')
        plt.title('Tensiones V5 según fp')
        plt.xlabel('Sload (pu)')
        plt.ylabel('Tensión (pu)')
        plt.legend()
        plt.grid(True)
        plt.box(True)
        plt.show()
        

listo=Examen()
listo.bases()
listo.tensiones()
listo.pregunta1B()