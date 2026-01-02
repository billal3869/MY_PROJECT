numerateur=input("Entrez le numerateur:")
denominateur=input("Entrez le denominateur:")

try:
	resultat=int(numerateur)/int(denominateur)
	print(f"le resultat est :{resultat}")
except ZeroDivisionError:
	print("Erreur : Division par Zero!")
except ValueError:
	print("Erreur : Conversiion de type incorrecte")
	
