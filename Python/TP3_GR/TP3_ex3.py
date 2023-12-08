import random

x=int(input("Entrez une valeur: "))
n=random.randint(0,100)

while n!=x:
    if x > n:
        print("C'EST MOINS")
        x = int(input("Entrez une nouvelle valeur: "))
    if x < n:
        print("C'EST PLUS")
        x = int(input("Entrez une nouvelle valeur: "))
print("OUI OUI OUI C'EST LA BONNE VALEUR")

        