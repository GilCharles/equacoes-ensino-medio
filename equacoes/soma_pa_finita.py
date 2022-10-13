""" 

"""


class somapafinita:

    def __init__(self, a1, enesimo, ntermos, sn = None):
        self.sn = sn # Soma dos n termos
        self.a1 = a1 # Primeiro termo
        self.enesimo = enesimo # Enésimo termo 
        self.ntermos = ntermos # Número de termos

    def somatermos(self):

        return ((self.a1 + self.enesimo) * self.ntermos) / 2



#res = somapafinita(0, 5500, 12)
#print(res.somatermos())


