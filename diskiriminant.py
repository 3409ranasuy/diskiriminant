# a*x**2 + b*x + c
a = float(input('x**2 ifade : '))
b = float(input('x ifade : '))
c = float(input('sabit : '))
kökTop = float(-b/a)
kökÇarp = float(c/a)
Δ = float(b**2-4*a*c)
x1 = float((-b+(Δ**1/2))//(2*a)) 
x2 = float((-b-(Δ**1/2))//(2*a))
if ( Δ==0) :
    print(-b/2*a) 
elif (Δ>0):
    print(f'x1: {x1}, x2: {x2}')
elif (Δ<0):
    print('Denklemin reel kökü yoktur.')

print(f'Denklemin kök toplamlamı: {kökTop}')
print(f'Denklemin kök çarpımı: {kökÇarp}')
result = (x1*x2)==(kökÇarp)
result1= (x1+x2)==(kökTop)
print(f'Denklemin kök çarpımları eşit mi: {result}')
print(f'denklemin kök toplamı eşit mi: {result1}')
print(f'Denkleminin diskiriminantı: {Δ}')

