nb = int(input('Vous cherchez la table de multiplication de quel nombre ? '))
nb2 = int(input('Vous cherchez la table de multiplication de quel nombre ? ( entrez à nouveau ) : '))

resultat = []

for i in range(0,11):
    nb2 = nb * i
    resultat.append(nb)
    print(nb,'*', i,'=', nb2)