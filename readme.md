## Inhoudsopgave
1. [Installatie en gebruik](#installatie-en-gebruik) 
2. [Templates](#templates)
3. [Functions](#functions)
4. [maakB4U.py](#maakb4upy)

## Installatie en gebruik
Om de code goed uit te voeren moet je de code downloaden en de benodigde pakketten installeren. Dit doe je als volgt:

1. Download en installeer Python en Git
2. Open jouw terminal en navigeer naar de gewenste opslagloctie en gebruik `git clone https://github.com/FreddyMeijer/B4U_generator.git`
3. Open de map waarin je de repository hebt opgeslagen
4. Voer het commando `pip install -r requirements.txt` uit
5. Voer het commando `python maakB4U.py` uit

## Templates
De templates hebben we nodig om straatnamen, kleuren en automerken te verkrijgen voor het B4U bestand. De inhoud van de tekstbestanden is gegenereerd door ChatGPT door simpelweg te vragen om 100 willekeurige straatnamen (in Leiden), kleuren en automerken. De templates worden gebruikt in `templateFunctions.py`.

### Automerken
Vanuit het bestand <i>automerken.txt</i> wordt een willekeurige waarde gekozen. Deze waarde wordt aangevuld met spaties totdat de lengte van de waarde gelijk is aan 20 karakters.

### Kleuren
Vanuit het bestand <i>kleuren.txt</i> wordt een willekeurige waarde gekozen. Deze waarde wordt aangevuld met spaties, of afgebroken zodat de lengte van de waarde gelijk is aan 6 karakters.

### Straatnamen
Vanuit het bestand <i>straatnamen.txt</i> wordt een willekeurige waarde gekozen. Deze waarde wordt aangevuld met spaties totdat de lengte van de waarde gelijk is aan 25 karakters.

## Functions
In de map <i>functions</i> zitten een vijftal functies die nodig zijn om data te vullen in het B4U bestand.

### Aanslagnummer
Een aanslagnummer telt 7 karakters, voorafgegaan door drie nullen. Technisch gezien is het mogelijk dat in een set van 250 aanslagnummers twee dezelfde aanslagnummers voorkomt (0,3%). 

Echter: Het kenteken moet dan ook hetzelfde zijn. De kans dat een kenteken hetzelfde is vanuit de functie `kentekens` is 0,17%. De kans dat beide variabelen hetzelfde zijn wordt hiermee zeer laag (0,00051%) en daarmee verwaarloosbaar. 

### Kentekens
Omdat we willekeurige kentekens willen krijgen is ervoor gekozen met behulp van het pakket `string` een combinatie van letters en cijfers te maken in het format AB123C. 

### Automerken
Deze functie kijkt naar het bestand met de naam <i>automerken.txt</i>. In dit bestand zijn 100 willekeurige automerken opgenomen. Het merk wordt in de functie afgekapt of verlengd tot 20 karakters.

### Kleuren
Deze functie kijkt naar het bestand met de naam <i>kleuren.txt</i>. In dit bestand zijn 100 willekeurige kleuren opgenomen. De kleur wordt in de functie afgekapt of verlengd tot 6 karakters.

### Straatnamen
Deze functie kijkt naar het bestand met de naam <i>straatnamen.txt</i>. In dit bestand zijn 100 willekeurige straten opgenomen. De straatnaam wordt in de functie afgekapt of verlengd tot 25 karakters.

## maakB4U.py
Als de code van `maakB4U.py` wordt uitgevoerd, worden allereerst een drietal variabelen gevuld die nodig zijn voor het opbouwen van de records in het B4U bestand.

`vandaag` wordt gevuld met de datumtijdstempel van het moment van uitvoeren van de code. Het format wordt gelijkgesteld aan yyyymmddhhmm. `belasting` is een array met alle mogelijke belastingbedragen. Deze zijn uit te breiden of te veranderen. Uit deze array wordt een willekeurig belastingbedrag gekozen. `aantalregels` bepaalt hoeveel naheffingen er in het bestand komen. Op dit moment wordt een willekeurig aantal regels gegenereerd in de range 100 tot 250.

Het B4U bestand krijgt een naam die bestaat uit de datum en het aantal regels (bijvoorbeeld 202406300823_testbestand_216_regels.b4u). Dit bestand wordt opgelagen in de map met de naam <i>testbestanden</i>. Bij het downloaden van de repository is deze map leeg.