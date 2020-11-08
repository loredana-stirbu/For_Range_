print("Utilizînd ciclul FOR elaboraţi un program care să calculeze suma numerelor de la 1 la n, care se împart la 3 şi 5 pentru oricare n întrodus de la tastatură.")

s=0
n=int(input("Dati un numar: "))
for n in range(1,n,1):
    if ((n%3==0)or(n%5==0)):
         s+=n
print(s)