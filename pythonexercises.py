#PRIMEIRA LISTA: EXERCÍCIOS SOBRE VARIÁVEIS E TIPOS DE DADOS.
#Exercício 1: Faça um programa que que leia um número inteiro de 4 dígitos e imprima 1 dígito por linha. [FÁCIL]
numero = input('Digite um número inteiro de 4 dígitos,ou seja,entre 1000 e 9999:')
if len(numero) == 4:
    print(f'{numero[0]} \n{numero[1]} \n{numero[2]} \n{numero[3]}')
else:
    print('Esse valor não é válido.')
#Exercício 2: Faça um programa para ler as dimensões de um terreno,bem como o preço do metro de tela. Imprima o custo para cerca este mesmo terreno com tela.  [MÉDIO]
comprimento = float(input('Digite o comprimento do terreno,em metros:'))
largura = float(input('Agora,digite a largura do terreno,em metros:'))
preço = float(input('Digite o preço do metro de tela,em reais:'))
perimetro = 2*(c+l) 
total = perimetro*preço
print(f'O custo para cercar o terreno de {perimetro} metros de perímetro ficará em {total} reais.')

#Exercício 3: Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem(0, 0). [DIFÍCIL]
x = float(input('Digite a coordenada x do ponto:'))
y = float(input('Digite a coordenada y do ponto:'))
formula = ((x*x)+(y*y))**0.5 #A formula da distância entre dois pontos é a raíz da diferença entre x1 e x2 elevado ao quadrado somado à diferença entre y1 e y2 elevado ao quadrado.
print(f'A distância das coordenadas ({x},{y}) da origem (0,0) é {formula} unidades de distância.')



#SEGUNDA LISTA: EXERCÍCIOS SOBRE ESTRUTURAS CONDICIONAIS.
#Exercício 1: Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação. [FÁCIL]
peso = float(input('Digite seu peso,em kilograma:'))
altura = float(input('Digite sua altura,em metros:'))
imc = peso/(altura*altura)
if imc < 18.5:
    print(f'Seu IMC,{imc},é classificado como abaixo do peso.')
elif imc >= 18.6 and imc <= 24.9:
    print(f'Seu IMC,{imc},é classificado como peso normal.')
elif imc >= 25 and imc <= 29.9:
    print(f'Seu IMC,{imc},é classificado como peso em execesso.')
elif imc >= 30 and imc <= 34.9:
    print(f'Seu IMC,{imc},é classificado como obesidade grau I.')
elif imc >= 35 and imc <= 39.9:
    print(f'Seu IMC,{imc},é classificado como obesidade grau II(severa).')
else:
    print(f'Seu IMC,{imc},é classificado como obesidade grau III(mórbida).')

#Exercício 2: Faça um programa que receba três números e mostre-os em ordem crescente ou decrescente,dependendo da escolha do usuário. [MÉDIO]
numero1 = float(input('Digite o primeiro número:'))
numero2 = float(input('Digite o segundo número:'))
numero3 = float(input('Digite o terceiro número:'))
decisão = int(input('Digite 1 para ordem crescente ou 2 para ordem decrescente:'))
if decisão == 1:
    if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
        print(f'A ordem crescente dos números é:{numero3},{numero2},{numero1}.')
    if numero1 > numero2 and numero1 > numero3 and numero3 > numero2:
        print(f'A ordem crescente dos números é:{numero2},{numero3},{numero1}.')
    if numero2 > numero1 and numero2 > numero3 and numero1> numero3:
        print(f'A ordem crescente dos números é:{numero3},{numero1},{numero2}.')
    if numero2 > numero1 and numero2 > numero3 and numero3 > numero1:
        print(f'A ordem crescente dos números é:{numero1},{numero3},{numero2}.')
    if numero3 > numero1 and numero3 > numero2 and numero1 > numero2:
        print(f'A ordem crescente dos números é:{numero2},{numero1},{numero3}.')
    if numero3 > numero1 and numero3 > numero2 and numero2 > numero1:
        print(f'A ordem crescente dos números é:{numero1},{numero2},{numero3}.')
elif decisão == 2:
     if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
        print(f'A ordem decrescente dos números é:{numero1},{numero2},{numero3}.')
     if numero1 > numero2 and numero1 > numero3 and numero3 > numero2:
        print(f'A ordem decrescente dos números é:{numero1},{numero3},{numero2}.')
     if numero2 > numero1 and numero2 > numero3 and numero1> numero3:
        print(f'A ordem decrescente dos números é:{numero2},{numero1},{numero3}.')
     if numero2 > numero1 and numero2 > numero3 and numero3 > numero1:
        print(f'A ordem decrescente dos números é:{numero2},{numero3},{numero1}.')
     if numero3 > numero1 and numero3 > numero2 and numero1 > numero2:
        print(f'A ordem decrescente dos números é:{numero3},{numero1},{numero2}.')
     if numero3 > numero1 and numero3 > numero2 and numero2 > numero1:
        print(f'A ordem decrescente dos números é:{numero3},{numero2},{numero1}.')
else:
    print('A escolha não é válida.')

#Exercício 3: Informe o número de raízes de uma equação de 2o grau e as calcule. [DIFÍCIL]
a = int(input('Nos informe o valor do coeficiente a,seguindo o modelo ax²+bx+c=0:'))
b = int(input('Nos informe o valor do coeficiente b,seguindo o modelo ax²+bx+c=0:'))
c = int(input('Nos informe o valor do coeficiente c,seguindo o modelo ax²+bx+c=0:'))
discriminante = (b**2)-4*a*c
if discriminante < 0:
    print('Não existem raízes no domínio dos reais.')
elif discriminante == 0:
    raiz = -b/(2*a) 
    print(f'Essa equação apresenta a raíz única {raiz}.')
else:
  raizdiscriminante= discriminante**0.5
  raiz1= (-b+raizdiscriminante)/(2*a)
  raiz2= (-b-raizdiscriminante)/(2*a)
  print(f'Essa equação apresenta as raízes {raiz1} e {raiz2}.')

#TERCEIRA LISTA: EXERCÍCIO SOBRES ESTRUTURAS DE REPETIÇÃO.
#Exercício 1: Faça um programa que determine e mostre os cinco primeiros múltiplos de 3,considerando o domínio dos numeros naturais. [FÁCIL]
x = 0
while x < 15:
    x = x+3
    print(x)

#Exercício 2: Faça um programa que calcule a área de um triângulo,cuja base e altura são fornecidas pelo usuário. Esse programa não pode permitir a entrada de dados inválidos. [MÉDIO]
altura = float(input('Digite a altura do triângulo:'))
base = float(input('Digite a largura do triângulo:'))
area = (base*altura) / 2
if altura > 0 and base > 0:
    print(f'A área do triângulo é {area}.')
while area < 0:
    print('Dados informados inválidos.')
    altura = float(input('Digite a altura do triângulo:'))
    base = float(input('Digite a largura do triângulo:'))
    area = (base*altura) / 2
    if area > 0:
        print(f'A área do triângulo é {area}.')

#Exercício 3: Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado Triangulo de Floyd.
n = int(input('Digite o número de linhas do triângulo de floyd.'))
x = 1 
y = 1
while x <= n:
    z = 1 
    while z <= x:
        print(y,end=' ')
        y += 1 
        z += 1 
    print()
    x+=1 
