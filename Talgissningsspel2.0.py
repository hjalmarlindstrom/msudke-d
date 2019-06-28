import random
import random
tal = random.randint(1, 100)

def gissning():
    gissning1 = int(input("Skriv din gissning. \n"))
    if gissning1 < tal:
        print("Talet jag tänker på är större. ")
    elif gissning1 > tal:
        print("Talet jag tänker på är mindre. ")
    elif gissning1 == tal:
        print("Du gissade rätt!")
        b = False

def sista_gissningen():
    gissning7 = int(input("Skriv din sista gissning. \n"))
    if gissning7 < tal:
        print("Du hade fel och dina gissningar är slut. :( ")
    elif gissning7 > tal:
        print("Du hade fel och dina gissningar är slut. :(")
    elif gissning7 == tal:
        print("Du gissade rätt!")
        b = False 


b = True
while b:

    print("I det här spelet kommer datorn att tänka på ett tal och spelaren få gissa. ")
    print("Du har 7 gissningar.")

    gissning()

    gissning()

    gissning()

    gissning()

    gissning()

    gissning()

    sista_gissningen()

    print("---------------------")
