# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:01:09 2022

@author: Afonso Araújo
"""
def conta_menores(lista ,inteiro):
    n = 0
    for i in lista:
        if i< inteiro:
            n += 1
    return n 
def main():
    print(conta_menores((3, 4, 5, 6, 7), 5))
main()
