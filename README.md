# MASTERMIND
Deze repository bevat de code van de Mastermind opdracht. We laten de computer verschillende strategieën gebruiken om de geheime code te kraken. 
Aan het begin van het spel wordt er een code gegenereerd. Deze code bevat 4 integers tussen 0 en 5, elke nummer moet een andere kleur voorstellen. Vervolgens kan je beginnen met raden door een code naar keuze in te voeren wanneer hier om wordt gevraagd. Als je je gok hebt ingevoerd zal je feedback ontvangen in de vorm (goede kleur juiste plek, goede kleur onjuiste plek). Op basis van deze feedback kan je besluiten wat je volgende gok is.
Er mogen 10 pogingen gedaan worden om de code te kraken. Na 10 poging fout te hebben, heb je verloren. Je wint het spel door de juiste code te raden binnen de 10 gegeven pogingen.

# SPICE_ALGORITHM 
de eerste 3 sets worden gebruikt om te bepalen welke kleuren/nummers er in voor kunnen komen, doormiddel van 1.AABB 2.CCDD 3.EEFF. Na dat dit bepaald hoeft er alleen rond geschoven te worden om de juiste plek te vinden. In worst case isde geheime combinaties 3 van het zelfde en 1 ander element bevat dan weet het algorithme 3 van de 4 en hoeft alleen de laatste positie door te lopen voor mogelijk feedback.

