###################
# Segundo parcial #
###################

# Librerias utilizadas
import math
import numpy as np
import cmath
from numpy import pi, exp, angle, conj, real, imag, sqrt
import pandas as pd
import datetime
import matplotlib.pyplot as plt

######################
# Definición de bases#
######################

# Tensión base
VS_SI = 24.9*10**3
# Tensión secundario base
VL_SI = 7.2*10**3

# Potencia base sistema
Sb_SI = 5*10**6

# Relación de transformación
a23 = (24.9/7.2)

########
# Bases#
########

# Tensión base 1
Vb_1_SI = VS_SI
# Impedancia base 1
Zb_1_SI = VS_SI**2/Sb_SI
# Corriente base 1
Ib_1_SI = Sb_SI/(3**(1/2))*Vb_1_SI  # (Sb_SI/sqrt(3)*Vb_1)

# Tensión base 2
Vb_2_SI = (1/a23)*Vb_1_SI
# Impedancia base 2
Zb_2_SI = Vb_2_SI**2/Sb_SI
# Corriente base 2
Ib_2_SI = Sb_SI/(3**(1/2))*Vb_2_SI  # (Sb_SI/sqrt(3)*Vb_1)

###############################
# Impedancia de línea 1-2, 3-4#
###############################

XL1 = 1j*0.6*25
RL1 = 0.15*25
Z1_SI = RL1+XL1
Z1_pu = Z1_SI/Zb_1_SI

##########################
# Impedancia de línea 2-3#
##########################

XL2 = 1j*0.6*(1/1000)
RL2 = 0.15*(1/1000)
Z2_SI = RL2+XL2
Z2_pu = Z2_SI/Zb_1_SI

####################
# Impedancia del tx#
####################

XTX1 = 1j*(5/100)
RTX1 = (0.2/100)
ZTX1_pu = RTX1+XTX1   # No se calcula cambio de base porque SpropiaTX1=Sbase_SYSTEM

ZTX1_SI = ZTX1_pu*Zb_1_SI

##################################
# Vectores de potencia aparente S#
##################################

fp = 0.95
S_eval_SI = S_eval_SI = np.arange(1*10**(-6), (5*10**6), (0.1*10**6))
print("Tipo S ", type(S_eval_SI))
S_eval_pu = S_eval_SI/Sb_SI

###############################
# Vectores de pontencia real P#
###############################
P_eval_SI = (S_eval_SI*fp)
print("Tipo P ", type(P_eval_SI))
# Calcular Z_load_SI fp unitario
Z_un_SI = ((VL_SI)*2)/(P_eval_SI(1+1j*sqrt(((1/1)**2)-1)))
Z_un_SI_reflex = (a23**2)*Z_un_SI

# Calcular Z_load_SI fp atraso
Z_at_SI = ((VL_SI)*2)/(P_eval_SI(1+1j*sqrt(((1/fp)**2)-1)))
Z_at_SI_reflex = (a23**2)*Z_at_SI

# Calcular Z_load_SI fp adelanto
Z_ad_SI = ((VL_SI)*2)/(P_eval_SI(1-1j*sqrt(((1/fp)**2)-1)))
Z_ad_SI_reflex = (a23**2)*Z_ad_SI

####################################
# Sumatoria de impedancias de línea#
####################################

# Z total unitaria
Z_total_SI_un = (Z1_SI+Z2_SI+Z1_SI+ZTX1_SI+Z_un_SI_reflex)

# Z total 0.95 atraso
Z_total_SI_at = (Z1_SI+Z2_SI+Z1_SI+ZTX1_SI+Z_at_SI_reflex)

# Z total 0.95 adelanto
Z_total_SI_ad = (Z1_SI+Z2_SI+Z1_SI+ZTX1_SI+Z_ad_SI_reflex)

###################################################
# Pregunta 1: Gŕafico de línea para V1,V2,V3,V4,V5#
###################################################

# Corriente de línea SI
I_un_SI_un = VS_SI/Z_total_SI_un
print("Prueba para ver magnitud: ", abs(I_un_SI_un))

# Tensiones con FP unitario #

# SI

# V1_SI_UN
V1_SI_un = VS_SI-I_un_SI_un*0
# V2_SI_UN
V2_SI_un = V1_SI_un-I_un_SI_un*(Z1_SI)
# V3_SI_UN
V3_SI_un = V2_SI_un-I_un_SI_un*(Z2_SI)
# V4_SI_UN
V4_SI_un = V3_SI_un-I_un_SI_un*(Z1_SI)
# V5_SI_UN
V5_SI_un = V4_SI_un-I_un_SI_un*(ZTX1_SI)

# PU

# V1_pu_UN
V1_pu_un = abs(V1_SI_un/Vb_1_SI)
# V2_pu_UN
V2_pu_un = abs(V2_SI_un/Vb_1_SI)
# V3_pu_UN
V3_pu_un = abs(V3_SI_un/Vb_1_SI)
# V4_pu_UN
V4_pu_un = abs(V4_SI_un/Vb_1_SI)
# V5_pu_UN
V5_pu_un = abs(V5_SI_un/Vb_1_SI)

plt.plot(S_eval_pu, V1_pu_un, 'r', label='V1_pu')
plt.plot(S_eval_pu, V2_pu_un, 'g', label='V2_pu')
plt.plot(S_eval_pu, V3_pu_un, 'b', label='V3_pu')
plt.plot(S_eval_pu, V4_pu_un, 'c', label='V4_pu')
plt.plot(S_eval_pu, V5_pu_un, 'k', label='V5_pu')
plt.title('Tensiones V1, V2, V3, V4, V5')
plt.xlabel('Sload (pu)')
plt.ylabel('Tensión (pu)')
plt.legend()
plt.grid(True)
plt.box(True)
plt.show()


###################################################
# Pregunta 2: Gŕafico de línea para V4 y V5 at,ad #
###################################################

# Atraso
I_at_SI = VS_SI/Z_total_SI_at

# Adelanto
I_ad_SI = VS_SI/Z_total_SI_ad

# Tensiones unitarias SI (at,ad)

# Atraso
V1_SI_at = VS_SI-I_at_SI*0
V2_SI_at = V1_SI_at-I_at_SI*(Z1_SI)
V3_SI_at = V2_SI_at-I_at_SI*(Z2_SI)
V4_SI_at = V3_SI_at-I_at_SI*(Z1_SI)
V5_SI_at = V4_SI_at-I_at_SI*(ZTX1_SI)

# Adelanto
V1_SI_ad = VS_SI-I_ad_SI*0
V2_SI_ad = V1_SI_ad-I_ad_SI*(Z1_SI)
V3_SI_ad = V2_SI_ad-I_ad_SI*(Z2_SI)
V4_SI_ad = V3_SI_ad-I_ad_SI*(Z1_SI)
V5_SI_ad = V4_SI_ad-I_ad_SI*(ZTX1_SI)

# Tensiones unitarias PU (ad, at)
V4_pu_at = abs(V4_SI_at/Vb_1_SI)
V4_pu_ad = abs(V4_SI_ad/Vb_1_SI)

V5_pu_at = abs(V5_SI_at/Vb_1_SI)
V5_pu_ad = abs(V5_SI_ad/Vb_1_SI)


plt.plot(S_eval_pu, V4_pu_at, 'b', label='V4_0.95_atraso')
plt.plot(S_eval_pu, V4_pu_un, 'r', label='V4_unitario')
plt.plot(S_eval_pu, V4_pu_ad, 'g', label='V4_0.95_adelanto')
plt.title('Tensiones V4 según fp')
plt.xlabel('Sload (pu)')
plt.ylabel('Tensión (pu)')
plt.legend()
plt.grid(True)
plt.box(True)
plt.show()

plt.plot(S_eval_pu, V5_pu_at, 'b', label='V5_0.95_atraso')
plt.plot(S_eval_pu, V5_pu_un, 'r', label='V5_unitario')
plt.plot(S_eval_pu, V5_pu_ad, 'g', label='V5_0.95_adelanto')
plt.title('Tensiones V5 según fp')
plt.xlabel('Sload (pu)')
plt.ylabel('Tensión (pu)')
plt.legend()
plt.grid(True)
plt.box(True)
plt.show()