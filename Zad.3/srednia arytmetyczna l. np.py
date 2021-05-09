
a=int(input("podaj pierwszą liczbe z przedizału:"))
b=int(input("podaj ostatnia liczbe z przedizału:"))
suma=0
n=0
i=a
while i<b:
    while i%2==0:
        i=i+1
        suma=suma+i
        n=n+1
        i=i+2
        srednia=suma/n
print("srednia arytmetyczna l.np.:",srednia)
