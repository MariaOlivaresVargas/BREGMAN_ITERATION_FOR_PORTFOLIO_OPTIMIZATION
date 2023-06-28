#--------------------------------Bibliotecas--------------------------
import csv
import numpy as np
from optimizacion import modifBregman
import matplotlib.pyplot as plt
from fun_axu import conteo 
from time import time

#%% 
#-----------------------------Se expotan los datos-----------------------------
with open('Rs.csv', 'r') as file:
    reader = csv.reader(file)
    x = list(reader)
    result = np.array(x).astype("float")

with open('A.csv', 'r') as file2:
    reader2 = csv.reader(file2)
    y = list(reader2)
    resulty = np.array(y).astype("float")
#------------------------------------------------------------------------------
#-------------------Particion de indices para los tau--------------------------
conj_A=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,36,38] #tau=2^{-5}

conj_B=[16,28,34,37,39,40] #tau=2^{-600}
#------------------------------------------------------------------------------

cont = []
ite=[]          #Listas para guardar número de entradas distintas de 0, iteraciones, el tiempo  y los vectores w (en ese orden).
tim=[]
w_to=[]
kaux=[]         #Guarda los k para la gráfica
#-----------------------------------------------------------------------------
#Este for corresponde a los portafolios: si se desea imprimir uno en especifico se puede
#Por ejemplo para el primero es (0,1), para el segundo (1,2). Si quiero el 1 y el 2 (0,2), etc-
for k in range(0,2): 
    #print(k)
    if k in conj_A:
        tau0=1/pow(2,5)
    elif k in conj_B:
        tau0=1/pow(2,600)
    R=np.zeros(48*60).reshape(60,48)

    for i in range(60):
        for j in range(48):
            R[i][j]=result[i+k*12][j]  #Se define R
    
    A=np.zeros(2*48).reshape(2,48)
    
    rho=0.0
  
    for i in range(48):
        rho+=resulty[k][i]
        A[0][i]=resulty[k][i]   #Se define la matriz A
        A[1][i]=1.0
    rho=rho/48.0
    
    b=np.array([rho,1.0])             #Se define el vector b
    
    
    start_time = time()
    w_aux,it=modifBregman(R,A,b,tau0)  #Se calcula w-optimo y las it-iteraciones 
    elapsed_time = time() - start_time
    print('----------------------------------------')
    print(f'--------------Portafolio {k+1}--------------')
    print('----------------------------------------')
    print(f'Aw={np.dot(A,w_aux)}') #Debe producir [p,1]  o una aproximación a 1.
    print(f'Con un tiempo de ejecución de {elapsed_time:.5f} segundos.')
    
    con=conteo(w_aux) 
    cont.insert(k,con)      #Cuenta y guarda el número de entradas distintas de 0 para cada w_i.
    
    
    ite.insert(k,it)            #Guarda las iteraciones realizadas hasta convergencia para cada w
    
    tim.insert(k,elapsed_time)     #Guarda el tiempo realizado hasta al convergencia 
    
    w_to.insert(k,w_aux)                #Guarda los w's 
    
    kaux.append(k) 

#%%
#Se dine el dominio de x para las gráficas 
n_k=len(kaux)
dif=kaux[n_k-1]-kaux[0]+1 
xdom=np.linspace(kaux[0]+1,kaux[n_k-1]+1 , num=dif)   
#%%
#Gráfica para los 40 portafolios: en cada w entradas activas
fig, ax = plt.subplots(figsize=(16,8))  # Create a figure and an axes.
ax.set_ylabel('Número de entradas activas')
ax.set_xlabel('Año')
plt.xticks(xdom)
#plt.tick_params(axis='x', colors='black', direction='out', length=13, width=3)
for i in range(len(xdom)):
  if xdom[i] in conj_A:
    plt.bar(xdom[i],cont[i],width=.8,color = 'k')
  elif xdom[i] in conj_B:
    plt.bar(xdom[i],cont[i],width=.8,color='c')
ax.set_title("Entradas activas por portafolio")  # Add a title to the axes.
#ax.grid(True)
for i in range(len(xdom)):
  plt.text(x = i+.5, y = cont[i]+.5, s = cont[i],
       size = 14, rotation = 0, color = 'k')
#ax.legend() 
#%% 
#Gráfica para los 40 portafolios: número de iteraciones.
fig, ax = plt.subplots(figsize=(16,8))  # Create a figure and an axes.
ax.set_ylabel('Número de iteraciones')
ax.set_xlabel('Año')
plt.xticks(xdom)
#plt.tick_params(axis='x', colors='black', direction='out', length=13, width=3)
for i in range(len(xdom)):
  if xdom[i] in conj_A:
    plt.bar(xdom[i],ite[i],width=.8,color = 'k')
  elif xdom[i] in conj_B:
    plt.bar(xdom[i],ite[i],width=.8,color='c')
ax.set_title("Iteraciones por portafolio")  # Add a title to the axes.
#ax.grid(True)
for i in range(len(xdom)):
  plt.text(x = i+.5, y = ite[i]+1000, s = ite[i],
       size = 14, rotation = 90, color = 'k')
#ax.legend() 
#%%
#Gráfica para los 40 portafolios: Tiempo de implementación
fig, ax = plt.subplots(figsize=(16,8))  # Create a figure and an axes.
ax.set_ylabel('Tiempo (segundos)')
ax.set_xlabel('Año')
plt.xticks(xdom)
#plt.tick_params(axis='x', colors='black', direction='out', length=13, width=3)
for i in range(len(xdom)):
  if xdom[i] in conj_A:
    plt.bar(xdom[i],tim[i],width=.8,color = 'k')
  elif xdom[i] in conj_B:
    plt.bar(xdom[i],tim[i],width=.8,color='c')
ax.set_title("Tiempo de ejecución por portafolio")  # Add a title to the axes.
#ax.grid(True)
#ax.legend() 