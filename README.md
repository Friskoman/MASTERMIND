# MASTERMIND
Aan het begin van het spel wordt er een code gegenereert. Daarna wordt er een vraag gesteld hier wordt een antwoord op gegeven door (goede kleur juiste plek, goede kleur onjuiste plek). Er mogen 10 pogingen gedaan worden om de code te kraken. Na 10 poging fout te hebben, heb je verloren. Je wint het spel door de juiste code te vragen binnen de 10 gegeven pogingen

SPICE_ALGORITHM 
de eerste 3 sets worden gebruikt om te bepalen welke kleuren/nummers er in voor kunnen komen, doormiddel van 1.AABB 2.CCDD 3.EEFF. Na dat dit bepaald hoeft er alleen rond geschoven te worden om de juiste plek te vinden. In worst case isde geheime combinaties 3 van het zelfde en 1 ander element bevat dan weet het algorithme 3 van de 4 en hoeft alleen de laatste positie door te lopen voor mogelijk feedback.

