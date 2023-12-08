import time

x = int(input("Entrez votre valeur positive : "))
for i in range(0, x+1):
    if x < 0:
        print("UNE VALEUR POSITIVE EST SUPERIEUR A 0")
        break

    else:
        print(x)
        x -= 1
        time.sleep(1)

while x != 0:
    if x < 0:
        break
    else:
        print(x)
        x -= 1
        time.sleep(1)