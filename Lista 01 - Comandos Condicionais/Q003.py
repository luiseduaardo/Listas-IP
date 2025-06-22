n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

soma = n1 + n2 + n3 + n4 + n5
resto = soma % 5

if resto == 0:
    print("Arthur", end = ' ')
elif resto == 1:
    print("Bruna", end = ' ')
elif resto == 2:
    print("César", end = ' ')
elif resto == 3:
    print("Daniel", end = ' ')
else:
    print("Eduarda", end = ' ')

print("vai ter a honra de passear com Byte hoje!")