n=int(input("n="))
if (n<10000) and (n>=0):
 print("ultima cifra a acestui numar este=",n%10) #primul punct
 print("Penultima cifră a acestui număr este=",(n//10)%10) #al doilea punct
 print("Restul=",n%9,"câtul=",n//9) #al treilea punct

n=str(n) #punctul patru
if len(n) == 1:
     print("suma cifrelor=",n)
n=str(n)
if len(n) == 2:
     n=int(n)
     a=n%10
     b=(n//10)%10
     c=a+b
     print("suma cifrelor=",c)
n=str(n)
if len(n) == 3:
     n=int(n)
     a=n%10
     b=(n//10)%10
     c=(n//100)%10
     print("suma cifrelor=",a+b+c)
if len(n) == 4:
     n=int(n)
     a=n%10
     b=(n//10)%10
     c=(n//100)%10
     d=(n//1000)%10
     print("suma cifrelor=",a+b+c+d)
n=str(n)
print(n[::-1]) #punctul cinci