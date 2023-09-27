# soma
def soma(value1, value2):
    
    return value1 + value2
# multiplicação
def multi(value1, value2):
    
    return value1 * value2
# divisão
def div(value1, value2): 
    
    return value1 / value2
# subtração
def sub(value1, value2):
    
    return value1 - value2
# expoente
def elevar(value1, value2=2):
    return value1 ** value2

# Contador positivo e negativo
def contagem(numero):
    if numero >0: 
        return "Positivo"
    else :
        return "Negativo"

# contagem de digitos
def quantidade(numero): 
    digitos = len(str(numero))
    return(digitos)


#calcular
def calcular(numero1, numero2, operador):
   if operador == "soma":
       return numero1 + numero2
   
   elif operador == "sub":
       return numero1 - numero2
   