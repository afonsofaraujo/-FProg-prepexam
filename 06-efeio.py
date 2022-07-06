# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:46:48 2022

@author: Afonso Araújo
"""

def max_div(n,d):
    i=0
    while True:                   #encontrar maior potência
        if n%(d**i)==0:
            i += 1
        else:
            break
    return int(n/(d**(i-1)))

def e_feio(n):
    for d in (2,3,5):
        n = max_div(n,d)
    return n==1
        
print(e_feio(300))