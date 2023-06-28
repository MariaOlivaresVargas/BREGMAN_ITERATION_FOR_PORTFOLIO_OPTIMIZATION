#------------------------------Bibliotecas-----------------------------------
import numpy as np
from scipy.optimize import line_search
from funciones import fobjetivo

#%%
##############################################################################
#          MÉTODOS: FISTA Y ALGORITMO MODIFICADO DE BREGMAN                  #
##############################################################################

#%%
#Función que cuenta el numero de entradas negativas

#Argumentos: w- vector

def numShort(w):

    n=len(w); aux=0

    for i in range(n):

        if w[i]<0:

            aux+=1

    return aux
#%%
#Función para regularizar tau

#Argumentos: m-escalar (número de entradas negativas <numshort>)

def phi(m):

    if m==0:

        return 1

    elif m>0:

        return 2
#%%
#Función que define la aproximacion cuadrática de la funcipon F=f+g ya regularizada 
#de manera simplificada.

#Argumentos: x-vector x, L>0 escalar ('tamaño de paso), f-función, y-vector

def h(x,L,f,y):
   
    aux1=f.g(x)     # Función convexa no continua que actua de regularizador
    
    aux2=np.linalg.norm(x-(y-(1/L)*f.fgradient(y)))**2  # función convexa
    
    return aux1+(L/2)*aux2
#%%
#Función gradiente de la aproximación cuadrática regularizada.

#Argumentos: x-vector x, L>0 escalar ('tamaño de paso), f-función, y-vector

def gradh(x,L,f,y):

    aux1=f.ggradient(x)+(x-(y-(1/L)*f.fgradient(y)))*L

    return aux1

#%% 
#Funcion objetivo a minimizar 

#Argumentos: x-vector; f-funcion

def F(x,f):
    return f.f(x)+f.g(x)
#%%
#Función que define la aproximacion cuadrática de la funcipon F=f+g ya regularizada sin simplificar
#Argumentos: x,y-vectores; L>0 escalar (tamaño de paso); f-función

def Q(x,y,L,f):

    aux1=f.f(y) #función 

    aux2=np.dot(x-y,f.fgradient(y)) # producto punto de la diferencia de los vectores y el gradi

    aux3=(L/2.0)*(np.linalg.norm(x-y)**2) # 

    aux4=f.g(x) # Función convexa no continua que actua de regularizador 
    return aux1+aux2+aux3+aux4

#%%
#Función que mínimiza la función cuadrática regularizada simplificada
#Operador proximal de g, de la norma l1

#Argumentos: w-vector, tau-real positivo.
#Proxg(x)(wi)=sgn(wi)(|wi|-min(|wi|,tau))
def pL(w,tau):
    aux=np.copy(w)
    n=len(w)
    
    for i in range(n):
        absw=abs(w[i])
        
        if absw>=tau:           #Se escoge al mínimo de |wi| y tau
            mina=tau
        else:
            mina=absw       
        if w[i]>=0:
            aux[i]=absw-mina           #Funcion signo 
        elif w[i]<0:
            aux[i]=mina-absw
    return aux

#%%
#Implementación de FISTA
#Argumentos:  x0- punto inicial (vector); R-Matriz de datos; A=(mu,1)-Matriz en R^(2xn)
# rho>0-escalar, bk-vector inicial bk=(rho,1), tau-escalar (parametro de regularizacion)

def FistaBacktracking(x0,R,A,rho,bk,tau):
    L=1.0
    eta=2
    t=1.0
    lam=10.0
    k=0
    tol=1/pow(10,6)
    y=np.copy(x0)
    x=np.copy(x0)
    n=len(x)
    
    Lbar=L   
    f=fobjetivo(R,A,bk,rho,tau,lam) #Funcion inicial
     
    while True:
        while True:         #Se encuentra el entero más pequeño no negativo tal que Lbar=eta^{i}L_k
            z=y-(1/Lbar)*f.fgradient(y)
            pl=pL(z,tau)

            if F(pl,f) <= Q(pl,y,L,f):   #El entero más pequeño debe cumplir está condición
                break
            Lbar=Lbar*eta
            L=Lbar
        x_new=np.copy(pl)               
        t_new=0.5*(1+np.sqrt(1+4*t**2))             #Actualizaciones: x,t y
        y_new=x_new+(t-1)/t_new*(x_new-x)            
        
        k+=1
         #Criterio de paro
        if np.linalg.norm(x-x_new)/n<tol:
            break
        x=np.copy(x_new)    
        t=np.copy(t_new)                #Se reescriben x,t,y
        y=np.copy(y_new)
    return x

#%%
#Bregman modificado para seleccion de cartera (portfolio)
#Argumentos: R-Matriz de datos; A=(mu,1)-Matriz en R^(2xn), b=(rho,1), vector 
def modifBregman(R,A,b,tau0):
    tol=1/pow(10,3)
    n=48
    rho=b[0]
    k=0
    tauk=tau0
    
    w=np.zeros(n)
    bk=np.zeros(2)
    
    normb=np.linalg.norm(b)
    
    
    while True: 
        w_n=FistaBacktracking(w,R,A,rho,bk,tauk)   #Se minimiza Ek(w)+(lam/2)||Aw-bk||_2^2
        
        i=numShort(w_n)     #Cuenta el número de entradas donde w<0
    
        tau_n=phi(i)*tauk  
                                                        #Actualización de tau y b
        bk_n=bk+(tau_n/tauk)*(b-np.dot(A,w_n))
        
        
        #print(tau_n)
        #print(w_n)
        #print("norma:",np.linalg.norm(bk-bk_n)/normb)
        #print(np.dot(A,w))
        if (np.linalg.norm(bk-bk_n)/normb)<tol:
            break 
        k+=1
        tauk=tau_n      
        bk=np.copy(bk_n)
        w=np.copy(w_n)
    return w,k

