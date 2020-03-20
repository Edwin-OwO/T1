horas = float(input("Decime cuantas horas trabajas: "))
coste = float(input("Decime cuanto cobras por hora: "))
paga = round(horas * coste, 3)
print("Tu paga es " + str(paga))