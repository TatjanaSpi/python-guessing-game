import random as rand
print("Unesite bilo koji broj od nula do sto")
x = rand.randint(0, 100)

while True:
    u = int(input("Unesite broj: "))
    if u > x:
        print("Vas broj je veci od nasumicno izabranog broja")
    elif u < x:
        print("Vas broj je manji od nasumicno izabranog broja")
    else:
        print("Vas broj i nasumicno izabrani broj su jednaki")
        break

print("Bravo")