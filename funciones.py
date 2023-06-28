# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:23:24 2021

@author: jorge
"""
import numpy as np

#%%
##############################################################################
#                          FUNCIONES ANALITICAS                           #
#############################################################################
#%%

# Definimos la clase que contendrá a las funciones f y g que se necesitarán 
# para el algoritmo de FISTA, esto simplicará estarlas llamando cuando sea 
# necesario. Una vez dadas las matrices R,A; el vector b, y los escalares 
# rho, tau, lam, las funciones f y g quedan definidas. 
class TestFunction(object):
    """
    Se recomienda ampliamente que _todo se trabaje de forma vectorizada.
    Trate de evitar lo más que se pueda los búcles cuando se trata de
    evaluar función objetivo, gradiente o hessinano.
    """
    def __init__(self,R: np.ndarray, A: np.ndarray, b: np.ndarray, rho: float,tau:float,lam:float):
        #Los argumentos relacionados a 
        
        self.R = R
        self.A=A
        self.b=b
        self.rho=rho
        self.tau=tau
        self.lam=lam

    def f(self, x: np.ndarray):
        raise NotImplementedError
    
    def g(self, x: np.ndarray):
        raise NotImplementedError

    def fgradient(self, x: np.ndarray):
        raise NotImplementedError
        
    def ggradient(self, x: np.ndarray):
        raise NotImplementedError

#%%
# Creamos la función de la clase TestFunction que utilizaremos. 
# En esta parte definimos la expresión analítica de f y g, 
# además del gradiente de f.    
# Recibe los parámetros: las matrices R,A; el vector b, y los escalares 
# rho, tau, lam.        
class fobjetivo(TestFunction):

    def __init__(self,R: np.ndarray, A: np.ndarray, b: np.ndarray, rho: float,tau:float,lam:float):
        super().__init__(R,A,b,rho,tau,lam)
        
   #definimos f, recibe un vector w
    def f(self, w: np.ndarray, keep_record=True):
        R=self.R
        A=self.A
        b=self.b
        rho=self.rho
        lam=self.lam
        
        aux1=np.linalg.norm(rho-np.dot(R,w))**2
        aux2=np.linalg.norm(np.dot(A,w)-b)**2
        
        return aux1+(lam/2)*aux2
    
    #definimos g, recibe un vector w
    def g(self, w:np.array, keep_record=True):
        tau=self.tau
        aux=np.sum(np.abs(w))
        return tau*aux
    
    #definimos gradiente de f, recibe un vector w
    def fgradient(self, w:np.array, keep_record=True):
        R=self.R
        A=self.A
        b=self.b
        rho=self.rho
        lam=self.lam
        aux1=-2*np.dot(np.transpose(R),rho-np.dot(R,w))
        aux2=lam*np.dot(np.transpose(A),np.dot(A,w)-b)
        
        return aux1+aux2
    

        
    
        
        