#Aritmeticos
x = 15
y = 4
formatacao = x / y
print(x + y)
print(x - y)
print(x * y)
print(f"{formatacao:.1f}")
print(x % y)
print(x ** y)
print(x // y) # Resto da divisao

print("\n")

#Comparacao
x = 5
y = 3
print(x == y) #Igualdade
print(x != y) #Diferenca
print(x > y) #Maior que
print(x < y) #Menor que
print(x >= y) #Maior ou igual
print(x <= y) #Menor ou igual

print("\n")

#Logicos
# e
x = 5
print(x > 0 and x < 10)

# ou
x = 5
print(x < 5 or x > 10)

# not
x = 5
print(not(x > 3 and x < 10))