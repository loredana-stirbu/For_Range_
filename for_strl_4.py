print("Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele impare, pentru intervalul de la a la b (a și b se citesc de la tastatură).")

a=int(input("Dati un numar: "))
b=int(input("Dati un numar: "))
for a in range(a,b,1):
    if a%2!=0 :
        print(a)
    