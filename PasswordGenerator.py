import random

characters_count = input("Napiš kolik znaků má mít tvoje nové heslo: ")

lowercase_letters = "qwertyuiopasdfghjklzxcvbnm"
uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "123456789"

letters = lowercase_letters + uppercase_letters + numbers
l_letters = list(letters)

password = ""

for i in range(int(characters_count)):
    random_letter = random.choice(l_letters)
    password += random_letter

print(password)