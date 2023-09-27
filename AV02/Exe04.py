from operations import calcular

print("Calculadora de dois valores")

numero1= float(input("Digite o primeiro numero: "))
numero2=float(input("Digite o segundo numero: "))
print("Operaçôes disponiveis")
print("soma, sub, divisão, multiplicação")

operador = input("Digite a operação que deseja: ")

print(f"Resultado:  {calcular(numero1, numero2, operador)}")