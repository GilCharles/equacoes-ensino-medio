"""
Termo geral para descobrir o termo que queremos
"""


class progaritmetica:
    
    def __init__ (self ,a ,n ,r ,an = None):
        self.an = an
        self.a = a
        self.n = n
        self.r = r

    
    def pa(self):
        print(self.a + (self.n-1) * self.r)


q1 = progaritmetica(26, 10 ,5)
q1.pa()
