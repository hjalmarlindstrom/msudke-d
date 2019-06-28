
# Här skapas en klass. Den hanterar alla objekten, alltså alla Pokémon.
class Pokemon:
    def __init__(self, namn, liv, attack, defence):
        self.namn=namn
        self.liv=liv
        self.attack=attack
        self.defence=defence
        # Vill du lägga till flera stats så kan du göra det senare.

    def __str__(self):
        return (self.namn + ', liv: ' + str(self.liv) + ', attack: ' + str(self.attack))
        # Här läggs alla atribut ihop så att de kan printas


''' Det här är en funktion. Fråga ledare om du är nyfiken på vad det är.
Först skapas en lista där alla Pokémon ska läggas till.
Sedan öppnas filen där alla Pokémon ligger'''
def skapa_pokemonlista():
    pokelist=list()
    f=open("pokemonexcel.csv", "r")
    aPokemon = f.readline().strip().split(",") # Vi vill inte ha första raden
    '''
    Vidare vill vi ta bort onödiga tecken med strip(). Sedan vill vi dela upp den i rätt delar med split().
    Sen skapar vi alla objekt med klassen ovan.
    Sedan läggs objetet till i listan.
    Till slut spottar funktionen ut listan.
    '''
    for p in f:
        enPokemon = p.strip().split(",")
        pokeobjekt=Pokemon(enPokemon[2], int(enPokemon[3]), int(enPokemon[4]), int(enPokemon[5]) =)
        pokelist.append(pokeobjekt)
    return (pokelist)


