import random

print("*********************Nombre Secret**********************")
secret=random.randint(1,101)
print(secret)
print("********************************************************")
flag=False
compteur=0

while flag==False:
    choix=int(input("Entrez un nombre entre 0 et 100\n"))
    compteur+=1
    if choix==secret:
        flag=True
    elif choix<secret:
        print("Trop petit!!")
    elif choix>secret:
        print("Trop grand!!")
print("Bravo le nombre etait "+str(secret)+"\n coups pour trouver:",compteur)