#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Capoluoghi.py
#  
#  Copyright 2016 marta
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import random


# Definisco la lista delle regioni e dei capoluoghi corrispondenti
db_regioni = {"Valle d'Aosta" : "Aosta" ,
    "Piemonte" : "Torino" ,
    "Liguria" : "Genova" ,
    "Lombardia" : "Milano" ,
    "Trentino-Alto Adige" : "Trento" ,
    "Veneto" : "Venezia" ,
    "Friuli-Venezia Giulia" : "Trieste" ,
    "Emilia-Romagna" : "Bologna" ,
    "Toscana" : "Firenze" ,
    "Marche" : "Ancona" ,
    "Umbria" : "Perugia" ,
    "Lazio" : "Roma" ,
    "Abruzzo" : "L'Aquila" ,
    "Molise" : "Campobasso" ,
    "Campania" : "Napoli" ,
    "Basilicata" : "Potenza" ,
    "Puglia" : "Bari" ,
    "Calabria" : "Catanzaro" ,
    "Sicilia" : "Palermo" ,
    "Sardegna" : "Cagliari"}


regioni = list(db_regioni.keys()) # lista delle regioni

# Quiz. Indovina il capoluogo
# Estraggo una regione a caso

print("Indovina il capoluogo")
print('scrivi "fine" per finire\n')

for i in range(0, 21):
    region = random.choice(regioni)
    print("Qual'è il capoluogo di %s?" % (region))
    capoluogo = input(">>> ")
    if capoluogo == "fine":
        print("Il gioco è finito")
        break
    if capoluogo == db_regioni[region]:
        print("Bravissimo!")
    else:
        print("Hai sbagliato!")
        print("Era " + db_regioni[region])
        





def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
