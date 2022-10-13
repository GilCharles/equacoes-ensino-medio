"""
Termo geral para descobrir o termo que queremos
"""


class progaritmetica:
    
    def __init__ (self ,a ,n ,r ,an = None):
        self.an = an # Termo geral
        self.a = a # Primeiro termo
        self.n = n # Número de termos
        self.r = r # Razão da PA

    
    def pa(self):
        print(self.a + (self.n-1) * self.r)


#q1 = progaritmetica(0, 12, 500)
#q1.pa()
