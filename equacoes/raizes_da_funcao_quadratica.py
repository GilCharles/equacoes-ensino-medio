"""
Variáveis de função quadrática são a, b e c.
"""


# Variáveis

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

# Execução

delta = (b**2) - (4*a*c) # Equação para descobrir o delta
raiz = pow(delta, 0.5) # Equação para descobrir a raiz do delta


x1 = (-b - raiz) / (2*a) # Raiz 1 da função quadrática
x2 = (-b + raiz) / (2*a) # Raiz 2 da função quadrática

# Resultado

print(f"A função quadrática tem as seguintes raízes: {x1} e {x2}")