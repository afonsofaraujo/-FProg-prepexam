# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 17:39:03 2022

@author: Afonso Araújo
"""

def inverte_dic(dic):
    invdic={}
    for i in dic:
        for v in dic[i]:
            if v in invdic:
                invdic[v] = invdic[v] + [i]
            else:
                invdic[v] = [i]
    print(invdic)
        
inverte_dic({'a': [1, 2], 'b': [1, 5], 'c': [9], 'd': [4]})      