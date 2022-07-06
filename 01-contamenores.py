# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
