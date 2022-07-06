# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:12:44 2022

@author: Afonso Araújo
"""

def cria_lista_multiplos(n):
    if n<=0 or type(n) != int:
        print("numero inválido")
    else:
        res=[]
        for i in range(0,10):
            res.append(i*n)
    print(res)
           
            
        
    
