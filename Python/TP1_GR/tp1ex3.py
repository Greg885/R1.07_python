print("quel jour somme nous (entre 1 et 31)")
jour=int(input())
print("donner le nombre de l'heure (entre 0 et 23)")
heure=int(input())
print("donner le nombre des minutes (entre 0 et 59)")
minute=int(input())


time=(jour*1440+heure*60+minute)

print("il y a exactement depuis le début du mois", time, "minutes qui se sont écoulé")

