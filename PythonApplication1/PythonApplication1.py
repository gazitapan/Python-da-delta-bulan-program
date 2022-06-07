#delta bulma
print("Ondalık tabanda değerler giriniz.")
a = float(input("a katsayısını giriniz: "))
b = float(input("b katsayısını giriniz: "))
c = float(input("c katsayısını giriniz: "))

delta = (b ** 2) - (4 * a * c)

kök1=(-b + (delta) ** (1 / 2)) / (2 * a)
kök2=(-b - (delta) ** (1 / 2)) / (2 * a)

if(delta > 0):
    print("Denklemin iki farklı kök var: "+ str(kök1)+ " ve " + str(kök2))
elif(delta == 0):
    print("Denklemin çakışık iki kökü var: "+ str(kök1))
else:
    print("Denklemin kökü yok.")
