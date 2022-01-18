import random

digits = ['23456789']
lowercase_letters = ['abcdefghjkmnpqrstuvwxyz']
uppercase_letters = ["ABCDEFGHIJKMNPQRSTUVWXYZ'"]
punctuation = ['!# $%&*+-=?@^_.']
punctuation_2 = ['il1LoO0']

chars = []

pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
pwd_len = int(input('Какой длины должен быть пароль? '))

pwd_digits = input('Включать ли в пароль цифры от 0 до 9 д/н ? ')
if pwd_digits.lower() == 'д':
    chars.append(digits)
pwd_uppercase = input('Включать ли в пароль прописные буквы д/н ? ')
if pwd_uppercase.lower() == 'д':
    chars.append(uppercase_letters)
pwd_lowercase = input('Включать ли в пароль строчные буквы д/н ? ')
if pwd_lowercase.lower() == 'д':
    chars.append(lowercase_letters)
pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_" д/н ? ')
if pwd_punctuation.lower() == 'д':
    chars.append(punctuation)
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O" д/н ? ')
if pwd_exceptions.lower() == 'н':
    chars.append(punctuation_2)

def generate_password(length, chars):
    password = []
    for j in range(length):
        password += random.shuffle(chars)
    return password


print(generate_password(pwd_len, chars))