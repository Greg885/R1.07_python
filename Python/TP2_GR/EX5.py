x= int(input("Entrez un nombre entier: "))
if x==0:
    print("Le nombre est zéro (et il est pair)")

if (x > 0) & (x % 2 == 0) :
    print("Le nombre est positif et pair")

if (x > 0) & (x % 2 == 1):
    print("Le nombre est positif et impair")

if (x < 0) & (x % 2 == 0) :
    print("Le nombre est negatif et pair")

if (x < 0) & (x % 2 == 1):
    print("Le nombre est negatif et impair")
