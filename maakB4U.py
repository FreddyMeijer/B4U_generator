import functions.templateFunctions as tf
from datetime import datetime
import random

vandaag = datetime.now().strftime('%Y%m%d%H%M')
belasting = ['2800','0310','0020']
aantalregels = random.randint(100, 250)

with open('testbestanden/' + vandaag + '_testbestand_' + str(aantalregels) + '_regels.b4u', 'w') as file:
    file.write('01 TRDLC PHS4U 0000000000        20230522074439'+ (' ' * 453) + '\n')
    for i in range(aantalregels):
        recordidentifier = '15'
        datumuitschrijven = vandaag
        controleursnummer = '75712' + (' ' * 10)
        soortVoertuigLand = 'PANL '
        kenteken = tf.kentekens()
        kenteken += ' ' * 6
        merk = tf.automerken()
        kleur = tf.kleuren()
        catBFeit = '1F409A' + (' ' * 3)
        kosten = ('0' * 12) + '7000'
        belastingbedrag = ('0' * 12) + random.choice(belasting)
        klemkostenwww = ('0' * 16) + 'NNN'
        omschrijving = ' ' * 240
        geseponeerd = 'N' + ('0' * 12) + (' ' *16)
        aanslagnummer = tf.aanslagnummer()
        straatnaam = tf.straatnamen()
        runnummer = '00289' + (' ' * 57)
        regel = recordidentifier + datumuitschrijven + controleursnummer + soortVoertuigLand + kenteken + merk + kleur + catBFeit + kosten + belastingbedrag + klemkostenwww + omschrijving + geseponeerd + aanslagnummer + straatnaam + runnummer + '\n'
        file.write(regel)
    file.write('99EINDE' + (' ' * 493))