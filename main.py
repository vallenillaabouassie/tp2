
import random

number = random.randint(1, 99)
counter = 0
guess = int(input("Entrez un nombre de 1 a 99: "))
while number != "guess":

    if guess < number:
        counter = counter + 1
        print("Votre nombre est trop bas")
        guess = int(input("Entrez un nombre de 1 a 99: "))
    elif guess > number:
        counter = counter + 1
        print("Votre nombre est trop grand")
        guess = int(input("Entrez un nombre de 1 a 99: "))
    else:
        counter = counter + 1
        print("Vous l'avez eu!")
        print(f"Ca vous a pris {counter} essais")
        break
