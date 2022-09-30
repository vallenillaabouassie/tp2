
import random
#Prends un nombre au hasard entre 1 et 99
number = random.randint(1, 99)
#Demande a l'utilisateur son choix
guess = int(input("Entrez un nombre de 1 a 99: "))
while number != "guess":

    if guess < number:
        #si le nombre est plus petit que le nombre "number"
        print("Votre nombre est trop bas")
        #redemande une valeur
        guess = int(input("Entrez un nombre de 1 a 99: "))
    elif guess > number:
        #si le nombre est plus grand que le nombre dans "Number"
        print("Votre nombre est trop haut")
        #redemande une valeur
        guess = int(input("Entrez un nombre de 1 a 99: "))
    else:
        #si le nombre est correct
        print("Vous l'avez eu!")
        break
