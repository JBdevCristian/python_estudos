"""a = 6
b = 3
a /= 2 * b
print(a)


 #Ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
# Escolha o número maior
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprimir o resultado
print("O maior número é:", larger_number) 

#Ler dois números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
# Escolha o número maior
if number1 > number2: larger_number = number1
else: larger_number = number2
 
# Imprimir o resultado
print("O maior número é:", larger_number)


# Leia três números
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
 
# Assumimos temporariamente que o primeiro número
# é o maior deles.
# Em breve verificaremos isso.
largest_number = number1
 
# Nós verificamos se o segundo número é maior que o maior_número atual
# e atualize o maior_número, se necessário.
if number2 > largest_number:
    largest_number = number2
 
# Nós verificamos se o terceiro número é maior que o maior_número atual
# e atualize o maior_número, se necessário.
if number3 > largest_number:
    largest_number = number3
 
# Imprimir o resultado
print("O maior número é:", largest_number)
 
 
largest_number = -999999999
number = int(input())

if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Ir para a linha 02

# Leia três números.
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

# Verifique qual dos números é o maior
# e passe-o para a variável de número_maior.
 
largest_number = max(number1, number2, number3)
 
# Imprimir o resultado.
print("O maior número é:", largest_number)
 
 
 # Porgrama que verifica letra
palavra = input("Digite a palavra: ");

if palavra == "Spathiphyllum":
    print("Sim a", palavra, "é a melhor");
elif palavra == "spathiphyllum":
    print("Não, eu quero um grande Spathiphyllum!");
else:
    print("Spathiphyllum! Not pelargonium!");

ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")"""


    
 


 

 


