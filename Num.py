# put your python code here
import random

num_r = random.randint(1, 101)
print('Добро пожаловать в числовую угадайку! Как тебя зовут?')
name = input()
print(f'Привествую, {name}')

def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False


while True:
    count = 0
    print('Введите число от 1 до 100')
    count += 1
    num_in = int(input())
    if is_valid(num_in) == False:
        print('Вводи корректное число, тварына')
        continue
    else:
        if num_in > num_r:
            print(f'{name} число слишком большое, давай еще раз')
            continue
        if num_in < num_r:
            print(f'{name} число слишком маленькое, давай еще раз')
            continue
        if num_in == num_r:
            print(f'{name} Красавг4ег, угадал!')
            break
print(f'Спасибо, что попользовался этой прогой, {name}')