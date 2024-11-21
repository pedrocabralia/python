valores = [25, 40, 35, 10, 50]

menor = valores[0]
for i in range(len(valores)):
    
    if(valores[i] < menor):
        menor = valores[i]
    else:
        print("é maior")
print("o menor número é:",menor)
    