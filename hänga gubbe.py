
import random
ordlista = ["hund", "mus", "dator", "stol", "bord", "skor", "ben"]
gissade_bokstäver = []
gissade_bokstäver_2 = []
gissningar = 0
ordet = ordlista[random.randrange(0, len(ordlista)-1)]

def gissning():
    global gissade_bokstäver 
    global gissade_bokstäver_2
    global gissningar 
    global ordet 
    gissning2 = input("Skriv en bokstav")
    if gissning2 in ordet:
        print("Rätt!")
        gissningar = gissningar + 1
        gissade_bokstäver_2.append(gissning2)
    else:
        gissade_bokstäver.append(gissning2)
        print(gissade_bokstäver)
        print("Du hade tyvärr fel!")
        gissningar = gissningar + 1
    




print("Välkommen till hänga gubbe!")
print("Du kommer att ha 10 gissningar att gissa ordet!")
print("Lycka till!")

a = True
while a:

    if len(ordet) < len(gissade_bokstäver_2):
        gissning()
    
    elif len(ordet) == len(gissade_bokstäver_2):
        print("Du vann!")
        a = False
        print(gissade_bokstäver_2)
    elif gissningar < 10:
        gissning()

    elif gissningar == 10 or gissningar > 10:
        print("Du har tyvärr slut på gissningar")
        a = False
        
    




