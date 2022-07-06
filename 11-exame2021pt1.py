# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 23:33:42 2022

@author: Afonso Araújo
"""
from math import *

'''P1'''
soma=0
n=1
while n<=102685:
    soma += n
    n += 1
#print(soma)
###############
v=0
n=102685
while n>=1:
    n=n//2
    v += 1
#print(v)
###############
n=102685
a=0
for i in range(2,int(sqrt(n))):
    if n%i == 0:
        print('não é primo')
        print (n,'é divisível por',i)
        a=1
        break
if a==0:
    print('é primo')
###############
'''P2'''










