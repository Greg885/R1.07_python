BASE=4
fromage=800.0
Eau=2
ail=2
pain=400

nbConvives = int(input("Combien y'a t'il de convives ? : "))
print("il y aura, ", nbConvives, " convives" )

nouvelleQuantiteFromage= fromage * nbConvives / BASE
nouvelleQuantiteEau= Eau * nbConvives / BASE
nouvelleQuantiteAil= ail * nbConvives / BASE
nouvelleQuantitePain= pain * nbConvives / BASE


print("Pour faire une fondue fribourgeoise pour ",nbConvives, "personnes, il vous faut : \n"
"-" ,nouvelleQuantiteFromage, "gr de fromage \n"
"-" ,nouvelleQuantiteEau, "dl d'eau \n"
"-" ,nouvelleQuantiteAil, "gousse(s) d'ail \n"
"-" ,nouvelleQuantitePain, "gr de pain \n" )