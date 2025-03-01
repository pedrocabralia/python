import  operacoes

def mostrarMenu():
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
        resultado = operacoes.soma(num1, num2)
    elif opcao == 2:
            resultado =operacoes.subtrai(num1, num2)
    elif opcao == 3:
            resultado = operacoes.multiplica(num1, num2)
    elif opcao == 4:
            resultado = operacoes.divide(num1, num2)
    else:
            resultado = "Operação inválida."
            
    print("Resultado", resultado)
