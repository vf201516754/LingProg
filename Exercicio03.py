
# coding: utf-8

# 1 - Faça um Programa que peça dois números e imprima o maior deles.

# In[9]:


numero1 = input ("Insira o primeiro número?")
numero2 = input ("Insira o segundo número?")

if numero1 > numero2:
    print ("O maior número é " + numero1 + "!")
elif numero1 == numero2:
    print ("Os dois numero são iguais")
else: 
    print(numero2)


# 2 -Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# In[20]:


lt = input ("Insira uma letra ")

if lt == 'a' or lt == 'e' or lt == 'i' or lt == 'o' or lt == 'u':
    print("Vogais")
elif lt == 'q' or lt == 'w' or lt == 'r' or lt == 't' or lt == 'y' or lt == 'p' or lt == 's' or lt == 'd' or lt == 'f' or lt == 'g' or lt == 'h' or lt == 'j' or lt == 'k' or lt == 'l' or lt == 'ç' or lt == 'z' or lt == 'c' or lt == 'v' or lt == 'b' or lt == 'n' or lt == 'm':
    print("Consoantes")
else:
    print("Outros caracteres")


# 3 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa
# deve calcular a média alcançada por aluno e apresentar:
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# - A mensagem "Reprovado", se a média for menor do que sete;
# - A mensagem "Aprovado com Distinção", se a média for igual a dez.

# In[33]:


x = int(input('Digite a segunda nota: '))
y = int(input('Digite a sesgunda nota: '))

media = (x + y) / 2
if media >= 7:
    print ('aprovado')
elif media == 10:
    print ('aprovado com distinção')
else:
    print ('reprovado')


# 4 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

# In[34]:


x = int(input('Digite um número: '))
y = int(input('Digite um número: '))
z = int(input('Digite um número: '))

lista = [x, y, z]
sorted(lista, reverse=True)


# 5 - As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contrataram para desenvolver o programa que calculará os
# reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
# seguinte critério, baseado no salário atual:
# - salários até R$ 280,00 (incluindo) : aumento de 20%
# - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
# informe na tela:
# - o salário antes do reajuste;
# - o percentual de aumento aplicado;
# - o valor do aumento;
# - o novo salário, após o aumento.

# In[46]:


x = float(input('Digite o salário: '))

if x <= 280.0:
    y = x
    w = 20
    z = w * 100.0 / y
    x += 20
    print('Salário antes do reajuste:',y,
          '\nNovo salário, após o aumento:',x,
         '\nO percentual de aumento aplicado:',z,
         '\nO valo do aumento',w)
    
elif x > 280.0 and x <=700.0:
    y = x
    w = 15
    z = w * 100.0 / y
    x += 15
    print('Salário antes do reajuste:',y,
          '\nNovo salário, após o aumento:',x,
         '\nO percentual de aumento aplicado:',z,
         '\nO valo do aumento',w)
    
elif x > 700.0 and x <= 1500.0:
    y = x
    w = 10
    z = w * 100.0 / y
    x += 10
    print('Salário antes do reajuste:',y,
          '\nNovo salário, após o aumento:',x,
         '\nO percentual de aumento aplicado:',z,
         '\nO valo do aumento',w)
    
elif x > 1500:
    y = x
    porcentagem = int(5 / 100.0 * x)
    w = porcentagem
    z = 5.0
    x += porcentagem
    print('Salário antes do reajuste:',y,
          '\nNovo salário, após o aumento:',x,
         '\nO percentual de aumento aplicado:',z,
         '\nO valo do aumento',w)


# 6 - Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

# In[47]:


x = int(input('digite um número'))

if x == 1:
    print('Domingo')
elif x == 2:
    print('Segunda-feira')
elif x == 3:
    print('Terça-feira')
elif x == 4:
    print('Quarda-feira')
elif x == 5:
    print('Quinta-feira')
elif x == 6:
    print('Sexta-feira')
elif x == 7:
    print('Sabado')
else:
    print('valor inválido')


# 7 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa
# disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos
# obedece à tabela abaixo:
# Média de Aproveitamento Conceito
# Entre 9.0 e 10.0 A
# Entre 7.5 e 9.0 B
# Entre 6.0 e 7.5 C
# Entre 4.0 e 6.0 D
# Entre 4.0 e zero E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
# mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito
# for D ou E.

# In[51]:


nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 9.0 and media <= 10.0:
    print('Nota 1:', nota1,
         '\nNota 2:', nota2,
         '\nMedia:', media,
         '\nA',
         '\nAPROVADO')
    
elif media >= 7.0 and media < 9.0:
    print('Nota 1:', nota1,
         '\nNota 2:', nota2,
         '\nMedia:', media,
         '\nB',
         '\nAPROVADO')

elif media >= 6.0 and media <= 7.5:
    print('Nota 1:', nota1,
         '\nNota 2:', nota2,
         '\nMedia:', media,
         '\nC',
         '\nAPROVADO')
    
elif media >= 4.0 and media < 6.0:
    print('Nota 1:', nota1,
         '\nNota 2:', nota2,
         '\nMedia:', media,
         '\nD',
         '\nreprovado')
    
elif media >= 0.0 and media < 4.0:
    print('Nota 1:', nota1,
         '\nNota 2:', nota2,
         '\nMedia:', media,
         '\nE',
         '\nREPROVADO')


# 8 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
# informar se os valores podem ser um triângulo. Indique, caso os lados formem um
# triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
# que o terceiro;
# - Triângulo Equilátero: três lados iguais;
# - Triângulo Isósceles: quaisquer dois lados iguais;
# - Triângulo Escaleno: três lados diferentes;

# In[ ]:


a = float(input('lado 1: '))
b = float(input('lado 2: '))
c = float(input('lado 3: '))

if not (a + b) > c and (a + c) > b and (b + c) > a:
    print ('Os lados fornecidos não formam um triângulo')
    
elif a==b and a==c:
    print('O triângulo é equilátero')
    
elif a!=b and a!=c and b!=c:
    print('O triângulo é escaleno')
    
else:
    print('O triângulo é isósceles')


# 9 - Faça um programa que calcule as raízes de uma equação do segundo grau, na
# forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
# consistências, informando ao usuário nas seguintes situações:
# - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
# o programa não deve fazer pedir os demais valores, sendo encerrado;
# - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao
# usuário e encerre o programa;
# - Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
# informe-a ao usuário;
# - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

# In[4]:


import math
 
a = float(input('Digite o valor para A: '))
if a != 0:  
    b = float(input('Digite o valor para B: '))
    c = float(input('Digite o valor para C: '))
    
    delta = b * b - 4 * a * c
    
    if delta < 0:
        print('A equação não possui raizes reais')

    elif delta == 0:
        raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
        print('A raiz da equação é: ',raiz)

    else:
        raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)   
        print ('As raizes são',raiz1,' e ',raiz2)
else:
    print('A equação não é do segundo grau')


# 10 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
# usuário a valor do saque e depois informar quantas notas de cada valor serão
# fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é
# de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a
# quantidade de notas existentes na máquina.
# - Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de
# 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# - Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de
# 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

# In[11]:


from math import *
from string import *

saque = int(input('Digite o valor do saque: '))

if saque < 10.0:
    print('Valor incorreto, saque minimo permitido 10.0')

elif saque > 600:
    print('Valor incorreto, saque maximo permitido 600.0')
    
else:
    n100 = int(saque / 100)
    resto = saque % 100

    n50 = int(resto / 50)
    resto = resto % 50

    n20 = int(resto / 20)
    resto = resto % 20

    n10 = int(resto / 10)
    resto = resto % 10

    n5 = int(resto / 5)
    resto = resto % 5

    n2 = int(resto / 2)
    resto = resto % 2

    n1 = int(resto / 1)
    resto = resto % 1

    print ('Ao sacar', saque, 'reais, voce receberá:')
    print (n100, 'notas de 100')
    print (n50, 'notas de 50')
    print (n20, 'notas de 20')
    print (n10, 'notas de 10')
    print (n5, 'notas de 5')
    print (n2, 'notas de 2')
    print (n1, 'notas de 1')





# 11 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
# perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário,
# ele será classificado como "Inocente".

# In[12]:


p1 = input('Telefonou para a vítima? - responda sim ou não: ')
p2 = input('Esteve no local do crime? - responda sim ou não: ')
p3 = input('Mora perto da vítima? - responda sim ou não: ')
p4 = input('Devia para a vítima? - responda sim ou não: ')
p5 = input('Já trabalhou com a vítima? - responda sim ou não: ')

if p1 == 'sim':
    p1 = 1
elif p1 == 'não':
    p1 = 0
else:
    print('valor incorreto')
    
if p2 == 'sim':
    p2 = 1
elif p2 == 'não':
    p2 = 0
else:
    print('valor incorreto')

if p3 == 'sim':
    p3 = 1
elif p3 == 'não':
    p3 = 0
else:
    print('valor incorreto')
    
if p4 == 'sim':
    p4 = 1
elif p4 == 'não':
    p4 = 0
else:
    print('valor incorreto') 
    
if p5 == 'sim':
    p5 = 1
elif p5 == 'não':
    p5 = 0
else:
    print('valor incorreto')  
    
resultado = p1 + p2 + p3 + p4 + p5   
if resultado == 2:
    print('Suspeita')
elif resultado == 3 or resultado == 4:
    print('Cumplice')
elif resultado == 5:
    print('Assassino')
else:
    print('Inocente')


# 12 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# Até 5 Kg Acima de 5 Kg
# Morango R$ 2,50 por Kg R$ 2,20 por Kg
# Maçã R$ 1,80 por Kg R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
# R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um
# algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de
# maças adquiridas e escreva o valor a ser pago pelo cliente.

# 13 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor
# válido.

# In[ ]:


lista = [0,1,2,3,4,5,6,7,8,9,10]
x = int(input('digite uma nota entre zero e dez: '))
for num in lista:
    if num == x:
        print('valor entrado na lista')
    x = int(input('digite uma nota entre zero e dez: '))
        


# In[ ]:


lista = [1,2,3,4,5]
for item in lista:
    print(item)
    


# 14 - Faça um programa que leia 5 números e informe o maior número.

# In[2]:


n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
n3 = int(input('numero 3: '))
n4 = int(input('numero 4: '))
n5 = int(input('numero 5: '))

lista = [n1,n2,n3,n4,n5]

maior = max(lista)
print(maior)


# 15 - Faça um programa que leia 5 números e informe a soma e a média dos números.

# In[4]:


n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
n3 = int(input('numero 3: '))
n4 = int(input('numero 4: '))
n5 = int(input('numero 5: '))

soma = n1 + n2 + n3 + n4 + n5
media = soma / 5

print('Soma: ',soma,
     '\nMedia: ',media)


# 16 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

# In[1]:


for num in range(50):
    if num%2 != 0:
        print(num)


# 18 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um
# programa capaz de gerar a série até o n−ésimo termo.

# In[30]:


valor = int(input("Digite o valor: "))
a = 0
b = 1
while b < valor:
    print (b)
    a = b
    b = a+b


# 19 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
# usuário. Ex.: 5!=5.4.3.2.1=120

# In[33]:


def fatorial(n):
    if n <=1: 
        return 1
    else:
        return n*fatorial(n-1) 
    
n = float(input("Insira um numero natural"))
fatorial(n)
print ('O fatorial de n eh:', fatorial(n))


# 20 - O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca
# de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele
# desenvolveu um tabela que contém o número de itens que o cliente comprou e ao
# lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar
# quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado
# para desenvolver o programa que monta esta tabela de preços, que conterá os
# preços de 1 até 50 produtos, conforme o exemplo abaixo:
# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50

# 21- O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar
# a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
# contratado para desenvolver o programa que monta a tabela de preços de pães, de
# 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo
# abaixo:
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00

# 22 - O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
# agora possui uma loja de conveniências. Faça um programa que implemente uma
# caixa registradora rudimentar. O programa deverá receber um número
# desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve
# ser informado pelo operador para indicar o final da compra. O programa deve então
# mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
# para então calcular e mostrar o valor do troco. Após esta operação, o programa
# deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser
# conforme o exemplo abaixo:
# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00

# 23 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre
# acidentes de trânsito. Foram obtidos os seguintes dados:
# - Código da cidade;
# - Número de veículos de passeio (em 1999);
# - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# - Qual a média de veículos nas cinco cidades juntas;
# - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de
# passeio.

# In[17]:


codCidade1 = '001'
codCidade2 = '002'
codCidade3 = '003'
codCidade4 = '004'
codCidade5 = '005'

nVeiculos1 = 10000.0
nVeiculos2 = 20000.0
nVeiculos3 = 30000.0
nVeiculos4 = 40000.0
nVeiculos5 = 50000.0

nAcidente1 = 1000.0
nAcidente2 = 2000.0
nAcidente3 = 3000.0
nAcidente4 = 4000.0
nAcidente5 = 5000.0

lista = [nAcidente1,nAcidente2,nAcidente3,nAcidente4,nAcidente5]

maior = max(lista)
print('maior índice de acidentes de transito e a que cidade pertence',maior ,'na cidade 005')

menor = min(lista)
print('menor índice de acidentes de transito e a que cidade pertence',menor ,'na cidade 001')

mediaVeiculos = (nVeiculos1 + nVeiculos2 + nVeiculos3 + nVeiculos4 + nVeiculos5) / 5
print('média de veículos nas cinco cidades juntas é: ', mediaVeiculos)

mediaAciTra = (nAcidente1 + nAcidente2 + nAcidente3 + nAcidente4 + nAcidente5) / 5
print('média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é:', mediaAciTra)


# 24 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com
# os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor
# da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
# 1 0
# 3 10
# 6 15
# 9 20
# 12 25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
# R$ 1.000,00 0 1 R$ 1.000,00
# R$ 1.100,00 100 3 R$ 366,00
# R$ 1.150,00 150 6 R$ 191,67

# 25 - Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.
