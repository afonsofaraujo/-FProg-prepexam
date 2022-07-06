# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:20:50 2022

@author: Afonso Araújo
"""

def parte(lst,n):
    def parte_aux(lst,n,menores,maiores):
        if lst == []:
            print([menores, maiores])
        elif lst[0]<n:
            menores.append(lst[0])
            return parte_aux(lst[1:], n, menores, maiores)
        else:
            maiores.append(lst[0])
            return parte_aux(lst[1:], n, menores, maiores)
    return parte_aux(lst, n, [], [])

parte([3, 5, 1, 4, 5, 8, 9], 4)