VotosValidos= int(input("Ingrese la cantidad de votos validos: "))
VotosPartido= int(input("Ingrese la cantidad de votos del partido: "))
Umbral= VotosValidos * 0.03

if (VotosPartido >= Umbral):
    print("El partido tendrá curules")
else:
    print("El partido no tendrá curules")