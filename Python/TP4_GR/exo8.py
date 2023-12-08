name = str(input('quel est votre nom ? '))
firstname = str(input('quel est votre prénom ? '))
promo = int(input('quelle est votre promo ? '))
group = input('quelle est votre groupe ? ')

dico = {"name":name,"firstname":firstname,"promo":promo,"group":group}

print("Votre nom est",dico["name"],", prénom est ", dico["firstname"],",vous faites partie de la promo", dico["promo"], " et votre groupe est", dico["group"])

