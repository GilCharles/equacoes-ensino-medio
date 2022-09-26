"""
# Função Quadrática:

f(x) = ax^2 + bx + c, sendo "a" diferente de 0


"""


a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
c = int(input("Qual o valor de c? "))

print(f"""
Sua equação ficou assim:

f(x) = {a}x^2 +{b}*x + {c}
""")

x = int(input("Qual é o valor de x? "))

resultado = (a * (x**2)) + (b*x) + c

