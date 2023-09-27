import time
from operations import *

print("Bem vindo a calculadora")

value1=float(input("Digite seu primeiro valor: "))
value2=float(input("Digite seu segundo valor: "))

print("Operaçôes disponíveis")
time.sleep(0.8)
print("1 - Soma")
time.sleep(0.8)
print("2 - Subtração")
time.sleep(0.8)
print("3 - Multipliação")
time.sleep(0.8)
print("4 - Divisão")
time.sleep(0.8)

decision = input("Digite a operação desejada: ")
if decision == "1":
    print(f"resultado: {soma(value1, value2)}")
elif decision == "2":
    print(f"resultado: {sub(value1, value2)}")
elif decision == "3":
    print(f"resultado: {multi(value1, value2)}")
elif decision == "4":
    print(f"resultado: {div(value1, value2)}")    
else:
    print("Inválido")