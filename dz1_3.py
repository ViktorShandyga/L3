print("Вгадай число")
import random
number = random.randint(1,10)
guess = 0
while guess !=0:
 guess = input("Виберіть число від 1 до 10:")
guess = int(guess)
if guess == number:
    print("Правильно")
if guess > number:
    print("Більше!")
if guess < number:
    print("Менше!")