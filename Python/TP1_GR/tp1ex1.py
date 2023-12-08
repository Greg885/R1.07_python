nom = "Runser"
prenom = "Grégory"
math=20
anglais=11
info=15
promotion = "2023"
moy=(math+anglais+info)/3

print(type(nom))
print(type(prenom))
print(type(math))
print(type(anglais))
print(type(info))
print(type(promotion))
print(type(moy))

print("L'étudiant", nom, prenom, "de la promotion", promotion, "a une moyenne de {:.1f}".format(moy))

