import random
in1 = int(input('введите 1-ое число \n'))
in2 = int(input('введите 2-ое число \n'))
in3 = input('введите знак /, +, *, ** \n')
a = random.randint(0,1)
def plus():
    return print(f"{in1} + {in2} = {in1 + in2}")

def minus():
    return print(f"{in1} - {in2} = {in1 - in2}")

def umnogenie():
    return print(f"{in1} * {in2} = {in1 * in2}")

def delenie():
    if in2 == 0:
        print('ошибка, на 0 делить нельзя>:(')
    else:
        return print(f"{in1} / {in2} = {in1 / in2}")

def stepen1():
    return print(f"{in1} в степени {in2} = {in1 ** in2}")
def stepen2():
    return print(f"{in1} ** {in2} = {in1 ** in2}")
if in3 == '+':
    plus()
elif in3 == '-':
    minus()
elif in3 == '*':
    umnogenie()
elif in3 =='/':
    delenie()
elif in3 == '**':
    if a == 0:
        stepen1()
    else:
        stepen2()
