print("s1=1+2+3+…+n, s2=1*2+2*3+3*4+…+(n-1)*n, s3=1+1*2+1*2*3+…+1*2*3*…*n, s4=12+22+32+…+n2, s5=1/2+2/3+3/4+…+n/(n+1), s6=1+2+22+23+24+…+2n, Notă: Pentru fiecare sumă n – se va citi de la tastatură.")

n=int(input("dati un numar: "))
s1 = 0
s2 = 0
s5 = 0
s6 = 3
for i in range(1, n):
    s1 += i
    s2 += ((i - 1) * i)
    s5 += (i / (i + 1))
    s6 += (20 + i)

s3 = 1
pr=1
for i in range(2,n,1):
    pr*=i
    s3+=pr
   
s4 = 0
x=(n * 10) + 1
for i in range(1,x):
    if (i % 10 == 0):
        s4 += (i + 2)

print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
print("s4 =", s4)
print("s5 =", s5)
print("s6 =", s6)