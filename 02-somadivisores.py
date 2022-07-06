# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:01:09 2022

@author: Afonso Araújo
"""
def soma_divisores(n):
    sum=0
    if n==0:
        return 0
    elif n<0:
        print("invalid number")
    else:
        for i in range(1,n+1):
            if n%i ==0:
                sum += n/i
    print(int(sum))
        
soma_divisores(20)