def soma(a, b):
    return a + b 
def subtracao(a, b):
    return a - b 
def multiplicacao (a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "Não é possivel dividir por zero"
    else: 
        return a / b
print("Escolha a operação")
print("1. Soma")
print("2. Multiplicação")
print("3. Subtração")
print("4. Divisão")

escolha = input("Digite 1, 2, 3 ou 4 para selecionar a operação: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    print("Resultado:", soma(num1, num2))
elif escolha == '2':
    print("Resultado:", subtracao(num1, num2))
elif escolha == '3':
    print("Resultado:", multiplicacao(num1, num2))
elif escolha == '4':
    print("Resultado:", divisao(num1, num2))
else:
    print("Operação inválida")

