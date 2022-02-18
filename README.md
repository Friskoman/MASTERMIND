# MASTERMIND
Deze repository bevat de code van de Mastermind opdracht. We laten de computer verschillende strategieën gebruiken om de geheime code te kraken. 
Aan het begin van het spel wordt er een code gegenereerd. Deze code bevat 4 integers tussen 0 en 5, elke nummer moet een andere kleur voorstellen. Vervolgens kan je beginnen met raden door een code naar keuze in te voeren wanneer hier om wordt gevraagd. Als je je gok hebt ingevoerd zal je feedback ontvangen in de vorm (goede kleur juiste plek, goede kleur onjuiste plek). Op basis van deze feedback kan je besluiten wat je volgende gok is.
Er mogen 10 pogingen gedaan worden om de code te kraken. Na 10 poging fout te hebben, heb je verloren. Je wint het spel door de juiste code te raden binnen de 10 gegeven pogingen.

# SPICE_ALGORITHM 
Spice is nieuw voorgesteld algoritme om mastermind te kraken. Het werkt als volgt:

1. De eerste drie gokken worden altijd gebruikt om te te bepalen welke kleuren (nummers) in de code voor kunnen komen. De eerste drie gokken zijn daarom altijd 1. [0,0,1,1] 2. [2,2,3,3] 3. [4,4,5,5].
2. Vervolgens worden de kleuren doorgeschoven om de juiste plek te achterhalen tot dat de code gekraakt is.

