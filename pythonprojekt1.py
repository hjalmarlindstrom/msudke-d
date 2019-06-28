import random
lista_1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
lista_2 = ["Hjärter", "Klöver", "Ruter", "Spader"]

print("Hej vad heter ni? ")
namn1 = input("Spelare 1:")
namn2 = input("Spelare 2:")

print("Hej", namn1,"och", namn2, "!")
print("Korten har sina vanliga namn förutom:")
print("1 = Ess")
print("11 = Knekt")
print("12 = Dam")
print("13 = Kung")

siffra1 = random.randint(0, len(lista_1)-1)
siffra2 = random.randint(0, len(lista_1)-1)

spelare1 = lista_1[siffra1] + " " + lista_2[random.randint(0, len(lista_2)-1)]
spelare2 = lista_1[siffra2] + " " + lista_2[random.randint(0, len(lista_2)-1)]                                                        
                                                                 
print(namn1, "fick", spelare1)
print(namn2, "fick", spelare2)

if siffra1 < siffra2:
    print(namn2, "vann!")
elif siffra1 > siffra2:
    print(namn1, "vann!")
elif siffra1 == siffra2:
    print("Det blev oavgjort!")
                                    
