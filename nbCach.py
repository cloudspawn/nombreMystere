import random

print("*********************Nombre Secret**********************")

#generation du nombre aleatoire
secret=random.randint(1,101)

flag=False
compteur=0

#tant que le nombre n'a pas ete trouvé, boucle flag False
while flag==False:
    choix=int(input("Entrez un nombre entre 0 et 100\n"))
    compteur+=1
    if choix==secret:
        flag=True
    elif choix<secret:
        print("Trop petit!!")
    elif choix>secret:
        print("Trop grand!!")

#le nombre a été trouvé, le flag est True on sort de la boucle
print("Bravo le nombre etait "+str(secret)+"\n coups pour trouver:",compteur)
