#Exercício 1: Faça um programa para ler as dimensões de um terreno,bem como o preço do metro de tela. Imprima o custo para cerca este mesmo terreno com tela.
c = float(input('Digite o comprimento do terreno,em metros:'))
l = float(input('Agora,digite a largura do terreno,em metros:'))
p = float(input('Digite o preço do metro de tela,em reais:'))
per = 2*(c+l) #perímetro = 2 vezes a soma das dimensões.
calc = per*p #total = perímetro vezes o preço do metro de tela.
print(f'O custo para cercar o terreno de {per} metros de perímetro ficará em {calc} reais.')

#Exercício 2: Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem(0, 0).
x = float(input('Digite a coordenada x do ponto:'))
y = float(input('Digite a coordenada y do ponto:'))
formula = (x*x)+(y*y)
formula1 = formula**0.5
print(f'A distância das coordenadas ({x},{y}) da origem (0,0) é {formula1} unidades de distância.')
A fórmula da distância entre dois pontos é a raíz da diferença entre x1 e x2 elevado ao quadrado somado à diferença entre y1 e y2 elevado ao quadrado.

#Exercício 3: Faça um programa que que leia um número inteiro de 4 dígitos e imprima 1 dígito por linha.
a = input('Digite um número inteiro de 4 dígitos,ou seja,entre 1000 e 9999:')
if len(a) == 4:
    print(f'{a[0]} \n{a[1]} \n{a[2]} \n{a[3]}')
else:
    print('Esse valor não é válido.')