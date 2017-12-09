from imported_xlrd import xlrd

from imported_xlrd.xlrd.xldate import *
import operator

from TdP_collections.hash_table.chain_hash_map import ChainHashMap
from TdP_collections.hash_table.probe_hash_map import ProbeHashMap

import calendar

from Campionato import Campionato
book = xlrd.open_workbook( "all-euro-data-2016-2017.xls" )
nsheet=book.nsheets
contcamp=0
leagues=[]
campionati = ChainHashMap()  # Hashmap contenente i campionati


while contcamp!=nsheet:
    sheet = book.sheet_by_index(contcamp)
    k=1 # contatore campionati
    campionato=Campionato(sheet.cell_value(k,1))
    campionati.__setitem__(campionato.get_nome(),campionato)

    k+=1
    squadre=set()
    for j in range(1,sheet.nrows):
        for i in range (2,4):
            squadre.add(sheet.cell_value(j,i))
    n=squadre.__len__()
    cont=0
    giornata=1
    for j in range(1,sheet.nrows):
            giornata = sheet.cell_value( j, 0 )
            data = sheet.cell_value( j, 2 )
            sqcasa=sheet.cell_value(j,3)
            sqospite=sheet.cell_value(j,4)
            golcasa=int(sheet.cell_value(j,5))
            golospite=int(sheet.cell_value(j,6))
            golcasaprimo=(sheet.cell_value(j,8))   # va fattto il cast a intero ma prima va aggiustato il file

            golospiteprimo=sheet.cell_value(j,9)
            risultato=sheet.cell_value(j,7)

            y, m, d, h, i, s = xldate_as_tuple(data, book.datemode)

            data="{0}/{1}/{2}".format(d, m, y)
        #    print("Data",data)

            campionato.set_partita(campionato.Partita(sqcasa,sqospite,golcasa,golospite,golcasaprimo,golospiteprimo,risultato,data,giornata))
    leagues.insert(contcamp,campionato)
    contcamp+=1
ind=0
print("Campionati")
while (ind!=nsheet):
    print("Campionato",ind)
    camp=leagues.__getitem__(ind)
    camp.print_campionato()
    ind+=1

print("Punto1:\n\n\n")
squadre=set()
for item in campionato.partite:
    squadre.add(item.sqcasa)
print("Squadre Campionato")
while (squadre.__len__()!=0):
    print(squadre.pop())

print("Punto2:")
for item in campionato.partite:
    if (item.giornata==1):
        print(item)




print("\n\n################## PRESI TUTTI I VALORI ################### \n\n")

def Punto1(campionato):
    print("\n\n\n\nPunto 1 method \n")
    squadre = set()
    for elem in campionati.__getitem__(campionato).partite:

        if(elem.giornata==1):   # OTTIMIZZAZIONE (ESEGUO L'ADD SOLO PER UNA GIORNATA E NON PER TUTTE )
            squadre.add(elem.sqcasa)
            squadre.add(elem.sqospite)

    for elem in squadre:
        print(elem)

def Punto2(campionato,giornata):
    print("\n\n\n\nPunto 2 method \n")
    classifica = {}

    for elem in campionati.__getitem__(campionato).partite:

        if(elem.giornata==giornata): # CREO UN DICT DI SQUADRE CON PUNTEGGI A ZERO "CLASSIFICA INIZIALE"
            classifica[elem.sqcasa]=0
            classifica[elem.sqospite]=0


    for elem in campionati.__getitem__( campionato ).partite:
        if (elem.giornata <= giornata):
            if(elem.risultato=="H"):
                classifica[elem.sqcasa]+=3




            if (elem.risultato == "D"):

                classifica[elem.sqcasa]+=1
                classifica[elem.sqospite]+=1





            if(elem.risultato=="A"):

                classifica[elem.sqospite]+=3



    print("Classifica Ordinata")
  #  items.sort( key=itemgetter( 1 ), reverse=True )
    classificaordinata = sorted( classifica.items(), key=operator.itemgetter( 1 ) ,reverse = True)

    for elem in classificaordinata.__iter__():
        print(elem[0],"Punti: ",elem[1]," Partite Giocate: ",giornata)




def Punto3(campionato,giornata):
    print("\n\n\n\nPunto 3 method \n")
    classifica = {}

    for elem in campionati.__getitem__( campionato ).partite:

        if (elem.giornata == giornata):  # CREO UN DICT DI SQUADRE CON PUNTEGGI A ZERO "CLASSIFICA INIZIALE"
            classifica[elem.sqcasa] = 0
            classifica[elem.sqospite] = 0

    for elem in campionati.__getitem__( campionato ).partite:
        if (elem.giornata < giornata):
            if (elem.risultato == "H"):
                classifica[elem.sqcasa] += 3

            if (elem.risultato == "D"):
                classifica[elem.sqcasa] += 1
                classifica[elem.sqospite] += 1

            if (elem.risultato == "A"):
                classifica[elem.sqospite] += 3

        if (elem.giornata == giornata):
            if (elem.golcasaprimo>elem.golospiteprimo):
                classifica[elem.sqcasa] += 3

            if (elem.golcasaprimo==elem.golospiteprimo):
                classifica[elem.sqcasa] += 1
                classifica[elem.sqospite] += 1

            if (elem.golospiteprimo>elem.golcasaprimo):
                classifica[elem.sqospite] += 3


    print("Classifica Ordinata")
    #  items.sort( key=itemgetter( 1 ), reverse=True )
    classificaordinata = sorted( classifica.items(), key=operator.itemgetter( 1 ), reverse=True )

    for elem in classificaordinata.__iter__():
        print(elem[0], "Punti: ", elem[1], " Partite Giocate: ", giornata)



def Punto4(campionato,squadra,giornata):  #Inserito anche campionato poichè tra due camp diversi posso avere squadre cn nomi uguali

    print("\n\n\n\nPunto 4 method  \n")
    risultati = []
    for elem in campionati.__getitem__( campionato ).partite:

        if(giornata-5<0):
           if( elem.giornata <= giornata and (elem.sqospite == squadra or elem.sqcasa == squadra) ) :

               print(elem.sqcasa,elem.sqospite,elem.risultato,"Giornata: ",elem.giornata)





        elif (elem.giornata >= giornata-5 and elem.giornata<=giornata and (elem.sqospite==squadra or elem.sqcasa==squadra)):


            print(elem.sqcasa,elem.sqospite,elem.risultato,"Giornata: ",elem.giornata)



def Punto5(data):

    print("\n\n\n\nPunto 5 method  \n")

    for elem in campionati.__iter__():

        for elem in campionati.__getitem__( elem ).partite:      ## VISITA DI TUTTE LE PARTITE DI TUTTI I CAMPIONATI
            if(data==elem.data): print(elem,elem.data)
            print(elem, elem.data)



def Punto6(giornata,k):
    print("\n\n\n\nPunto 6 method  \n")

    classifica={}

    for elem in campionati:
        for elem in campionati.__getitem__( elem ).partite:      ## VISITA DI TUTTE LE PARTITE DI TUTTI I CAMPIONATI
            if(elem.giornata<=giornata):


                if(not elem.sqcasa in classifica.keys()): classifica[elem.sqcasa]=elem.golcasa

                else: classifica[elem.sqcasa]+=elem.golcasa

                if (not elem.sqospite in classifica.keys()): classifica[elem.sqospite]=elem.golospite

                else: classifica[elem.sqospite]+=elem.golospite

    classificaordinata = sorted( classifica.items(), key=operator.itemgetter( 1 ), reverse=True )
    i = 0
    for elem in classificaordinata.__iter__():

        if(i<=k):
            print(elem[0], "GoalFatti: ", elem[1], " Giornata: ", giornata)

        i+=1
        if(i>k): break   #ottimizza



def Punto7(giornata,k):
    print("\n\n\n\nPunto 7 method  \n")

    classifica={}

    for elem in campionati:
        for elem in campionati.__getitem__( elem ).partite:      ## VISITA DI TUTTE LE PARTITE DI TUTTI I CAMPIONATI
            if(elem.giornata<=giornata):


                if(not elem.sqcasa in classifica.keys()): classifica[elem.sqcasa]=elem.golospite

                else: classifica[elem.sqcasa]+=elem.golospite

                if (not elem.sqospite in classifica.keys()): classifica[elem.sqospite]=elem.golcasa

                else: classifica[elem.sqospite]+=elem.golcasa

    classificaordinata = sorted( classifica.items(), key=operator.itemgetter( 1 ), reverse=False )
    i = 0
    for elem in classificaordinata.__iter__():

        if(i<=k):
            print(elem[0], "GoalSubiti: ", elem[1], " Giornata: ", giornata)

        i+=1
        if(i>k): break   #ottimizza



def Punto8(giornata,k):
    print("\n\n\n\nPunto 8 method  \n")

    classifica={}

    for elem in campionati:
        for elem in campionati.__getitem__( elem ).partite:      ## VISITA DI TUTTE LE PARTITE DI TUTTI I CAMPIONATI
            if(elem.giornata<=giornata):


                if(not elem.sqcasa in classifica.keys()): classifica[elem.sqcasa]=elem.golcasa-elem.golospite

                else: classifica[elem.sqcasa]+=(elem.golcasa-elem.golospite)

                if (not elem.sqospite in classifica.keys()): classifica[elem.sqospite]=elem.golospite-elem.golcasa

                else: classifica[elem.sqospite]+=(elem.golospite-elem.golcasa)

    classificaordinata = sorted( classifica.items(), key=operator.itemgetter( 1 ), reverse=True )
    i = 0
    for elem in classificaordinata.__iter__():

        if(i<=k):
            print(elem[0], "Differenza Reti: ", elem[1], " Giornata: ", giornata)

        i+=1
        if(i>k): break   #ottimizza


def Punto9(giornata,campionato):
    print("\n\n\n\nPunto 9 method  \n")

    classifica={}
    classificacasa = {}
    classificatrasf = {}

    for elem in campionati.__getitem__( campionato ).partite:

        if (elem.giornata == 1):  # CREO UN DICT DI SQUADRE CON PUNTEGGI A ZERO "CLASSIFICA INIZIALE"
            classifica[elem.sqcasa] = 0
            classifica[elem.sqospite] = 0
            classificacasa[elem.sqcasa] = 0
            classificacasa[elem.sqospite] = 0
            classificatrasf[elem.sqcasa] = 0
            classificatrasf[elem.sqospite] = 0

    for elem in campionati.__getitem__( campionato ).partite:

        if(elem.giornata<=giornata):

            if (elem.risultato=="H"):


                classifica[elem.sqcasa] += 1
                classificacasa[elem.sqcasa] +=1

            if (elem.risultato == "A"):

                classifica[elem.sqospite] += 1
                classificatrasf[elem.sqospite] += 1

    classificaordinata = sorted( classifica.items(), key=operator.itemgetter( 1 ), reverse=True )
    classificaordinatacasa = sorted( classificacasa.items(), key=operator.itemgetter( 1 ), reverse=True )
    classificaordinatatrasf = sorted( classificatrasf.items(), key=operator.itemgetter( 1 ), reverse=True )


    print("\n\nClassifica Vittorie:")
    for elem in classificaordinata.__iter__():


            print(elem[0], "Numero Vittorie : ", elem[1], " Giornata: ", giornata)




    print("\n\nClassifica Vittorie Casa:")
    for elem1 in classificaordinatacasa.__iter__():

            print(elem1[0], "Numero Vittorie casa: ", elem1[1], " Giornata: ", giornata)



    print("\n\nClassifica Vittorie Trasferta:")
    for elem2 in classificaordinatatrasf.__iter__():


            print(elem2[0], "Numero Vittorie trasf:", elem2[1], " Giornata: ", giornata)









Punto1("E0")
Punto2("E0",9)
Punto3("E0",9)
Punto4("E0","Arsenal",10)
Punto5("22/10/2016")
Punto6(5,4)
Punto7(5,4)
Punto8(5,4)
Punto9(9,"E0")








