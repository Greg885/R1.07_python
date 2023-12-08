nbr = float(input("Vous chercher la table de multiplication de quel nombre ? "))
L = []
for i in range(11):
    L.append(nbr*float(i))
    print(f"{nbr} * {i} = {L[i]}")