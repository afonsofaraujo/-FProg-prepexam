# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:30:09 2022

@author: Afonso Araújo
"""

def max_div(n,d):
    i=0
    while True:                   #encontrar maior potência
        if n%(d**i)==0:
            i += 1
        else:
            break
    print(int(n/(d**(i-1))))
    
max_div(75, 3)   
    
    
    
    
    