x = int(input("Entre 1 pour que le programme s'execute avec une boucle While ou 0 pour qu'il s'execute avec une boucle for : "))
n = int(input("Entrer un nombre dont vous souhaitez determiner la factorielle : "))
a = 1

if x==1:
    print("Vous avez choisi la bocule while")
    while n!=1:
        a = a*n
        n -=1
    print("voici votre nombre",a)
if x==2:
    print("Vous avez choisi la bocule for")
    for i in range(1, n+1):
        a=a*i
    print("voici votre nombre",a)

