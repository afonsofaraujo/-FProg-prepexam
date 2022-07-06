# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 17:01:29 2022

@author: Afonso Araújo
"""

def max_div(n,d):
    i=0
    while True:        # encontrar maior potência
        if n%(d**i)==0:
            i += 1
        else:
            break
    return int(n/(d**(i-1)))

def e_feio(n):
    for d in (2,3,5):
        n = max_div(n,d)
    return n==1
        
def n_esimo_feio(n):
    i=1
    c=1
    while True:         # o while também podia selecionar a entrada no ciclo
        i+=1
        if e_feio(i)==True:
            c+=1
        if c==n:
            break
    print(i)

n_esimo_feio(10)