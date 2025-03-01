def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."
    
print("Bem-vindo à calculadora modularizada!")
print("Escolha uma operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
    
opcao = int(input("Digite o número da operação: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:
        resultado = soma(num1, num2)
elif opcao == 2:
        resultado = subtrai(num1, num2)
elif opcao == 3:
        resultado = multiplica(num1, num2)
elif opcao == 4:
        resultado = divide(num1, num2)
else:
        resultado = "Operação inválida."

print("Resultado:", resultado)