import random

tal = random.randint(1,100)



b = True
while b:
    print("I det här spelet kommer datorn att tänka på ett tal och spelaren få gissa ")
    print("Du har 7 gissningar")

    gissing1 = int(input("Skriv din första gissning \n"))
    if gissning1 < tal:
        print("Talet jag tänker på är större")
    elif gissning1 > tal:
        print("Talet jag tänker på är mindre")
    elif gissning1 == tal:
        print("Du gissade rätt!")
        b = False

    gissning2 = int(input("Skriv din andra gissning \n"))
    if gissning2 < tal:
        print("Talet jag tänker på är större")
    elif gissning2 > tal:
        print("Talet jag tänker på är mindre")
    elif gissning2 == tal:
        print("Du gissade rätt!")
        b = False

    gissning3 = int(input("Skriv din tredje gissning \n"))
    if gissning3 < tal:
        print("Talet jag tänker på är större")
    elif gissning3 > tal:
        print("Talet jag tänker på är mindre")
    elif gissning3 == tal:
        print("Du gissade rätt!")
        b = False

    gissning4 = int(input("Skriv din fjärde gissning \n"))
    if gissning4 < tal:
        print("Talet jag tänker på är större")
    elif gissning4 > tal:
        print("Talet jag tänker på är mindre")
    elif gissning4 == tal:
        print("Du gissade rätt!")
        b = False

    gissning5 = int(input("Skriv din femte gissning \n"))
    if gissning5 < tal:
        print("Talet jag tänker på är större")
    elif gissning5 > tal:
        print("Talet jag tänker på är mindre")
    elif gissning5 == tal:
        print("Du gissade rätt!")
        b = False

    gissning6 = int(input("Skriv din sjätte gissning \n"))
    if gissning6 < tal:
        print("Talet jag tänker på är större")
    elif gissning6 > tal:
        print("Talet jag tänker på är mindre")
    elif gissning6 == tal:
        print("Du gissade rätt!")
        b = False

    gissning7 = int(input("Skriv din sista gissning \n"))
    if gissning7 < tal:
        print("Du hade fel och dina gissningar är slut :( ")
    elif gissning5 > tal:
        print("Du hade fel och dina gissningar är slut :(")
    elif gissning5 == tal:
        print("Du gissade rätt!")
        b = False
    print("---------------------")

    
