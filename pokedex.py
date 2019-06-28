from pokemonlista import *

# pokelist är nu en lista med alla Pokémon.
# Den har statsen namn, HP och attack.
pokelist = skapa_pokemonlista()
deadpokemons = []
a = True
b = True
fight = False
d = True
while b:
    print("Välkommen till Pokedexet!\n Här kan du lära dig om Pokemons, deras egenskaper och även vilken som är den starkaste!")
    print("1. Sök efter pokemons")
    print("2. Slåss med pokemons")
    val = int(input("Skriv 1 eller 2 för att välja vad du vill göra."))
    if val == 1:
        sökning = input("Skriv namnet på pokemonen som du vill söka efter (rättstavat!)")
        for i in range(663):
            if sökning == pokelist[i].namn: # sökning
                print(pokelist[i])
                b = False # Stavat rätt på söka pokemonen
            

    elif val == 2:
        fight = True
        
        
    while fight:
        pokemon_1 = input("Skriv namnet på den första pokemonen (rättstavat). ")
        for i in range(663): # Hitta ena för fight
            if pokemon_1 == pokelist[i].namn:
                print(pokelist[i])
                pokemon_1 = pokelist[i]
                a = False # stavat rätt på första pokemonen
          
        while d:
            pokemon_2 = input("Skriv namnet på den andra pokemonen (rättstavat). ")

            for i in range(663): # Hitta andra för fight
                if pokemon_2 == pokelist[i].namn:
                    print(pokelist[i])
                    pokemon_2 = pokelist[i]
                    b = False # hittat två pokemon
                    d = False # stavat rätt på andra pokemonen
                elif 0 < len(deadpokemons) and pokemon_2 == deadpokemons[i].namn:
                    print("Denna pokemon är död, välj en annan")

        d = True
        if a == False: # fight
            pokemon_1.liv = (pokemon_1.liv + pokemon_1.defence) - pokemon_2.attack
            pokemon_2.liv = (pokemon_2.liv + pokemon_2.defence) - pokemon_1.attack

            if (pokemon_1.liv > 0) and (pokemon_2.liv > 0):
                print("Båda överlevde")
                if pokemon_1.liv > pokemon_2.liv:
                    print(pokemon_1.namn, "vann!")
                    slut = input("Vill du fortsätta slåss med pokemons? ")
                elif pokemon_1.liv < pokemon_2.liv:
                    print(pokemon_2.namn, "vann!")
                    slut = input("Vill du fortsätta slåss med pokemons? ")
            elif (pokemon_1.liv > 0) and (pokemon_2.liv < 0):
                print(pokemon_2.namn, "dog,", pokemon_1.namn, "vann!")
                slut = input("Vill du fortsätta slåss med pokemons? ")
                
            elif (pokemon_1.liv < 0) and (pokemon_2.liv > 0):
                print(pokemon_1.namn, "dog,", pokemon_2.namn, "vann!")
                slut = input("Vill du fortsätta slåss med pokemons? ")
            if pokemon_1.liv < 0:
                pokelist.remove(pokemon_1)
                deadpokemons.append(pokemon_1)
            elif pokemon_2.liv < 0:
                pokelist.remove(pokemon_2)
                deadpokemons.append(pokemon_2)

            if (slut == "nej")or(slut == "Nej"):
            
                fight =  False
              
                    
                        
            if fight == False:
                print("Du har nu stängt pokedex")
                        
        
    if b == True or a == True:
        print("Försök igen, du stavade fel.")
        b = True
        a = True
        d = True
