print("digite um número")
numero = int(input())

for i in range(numero):
    if(i % 3 ==0 and i % 5 ==0):
        print("FizzBuzz")
    elif(i % 5 ==0):
        print("Buzz")
    elif(i % 3 ==0):
        print("Fizz")
    else:
        print(i)
        

