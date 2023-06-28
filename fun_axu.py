#Bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#%%
##############################################################################
#                          FUNCIONES AUXILIARES                              #
#############################################################################
#%%
#IDENTIFICACIÓN DE PORTAFOLIO CON ENTRADAS NEGATIVAS 
#Argumentos: w- vector 
def c_n(w):
  w=np.array(w)
  por=[]
  for i in range(len(w)):
    for j in range(len(w[0])):
      if w[i,j]<0:                  #Si es negativo, se guarda el indice 
        por.append(i)
        break
  return por

#%%
#CONTEO DE ENTRADAS DISTINTAS DE 0
#Argumentos: w- vector 
def conteo(w):
    aux=0
    n=len(w)
    for i in range(n):
        if w[i]!=0: #Cuenta el número de entradas distintasd de 0. 
            aux+=1
    return aux

#%%
