# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 18:26:11 2022

@author: Afonso Araújo
"""

class mem_f:
    
    def __init__(self):
        self.f = {0: 0, 1: 1, 2: 2, 3: 7, 4: 17, 5: 52, 6: 137, 7: 397, 8: 1082}
    def val(self, n):
        def val_aux(n):
            if n in self.f:
                return self.f[n]
            else:
                f_n_1 = val_aux(n-1)
                f_n_2 = val_aux(n-2)
                f_n_3 = val_aux(n-3)
                self.f[n] = f_n_1 + 2 * f_n_2 + 3 * f_n_3
                return self.f[n]
        if n<0 or not isinstance(n,int):
            raise ValueError("o argumento deve ser um inteiro não negativo")
        else:
            return val_aux(n)
    def mem(self):
        return self.f

def f(n):
    
    def f_aux(n):
        if n>=3:
            return f_aux(n-1)+2*f_aux(n-2)+3*f_aux(n-3)
        elif n>=0 and n<3:
            return n
    if n<0 or not isinstance(n,int):
        raise ValueError("o argumento deve ser um inteiro não negativo")
    else:
        return f_aux(n)
    
#print(f(20))
f = mem_f()
print(f.val(9))        #não está a dar igual
print(f.mem())
#print(f.val(9))