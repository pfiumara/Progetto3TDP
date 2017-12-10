from tkinter import  *
from tkinter import  ttk
from imported_xlrd import xlrd
from imported_xlrd.xlrd.xldate import *
import operator
from TdP_collections.hash_table.chain_hash_map import ChainHashMap


from Campionato import Campionato



########################### METODI  PUNTO 1-9

def Punto1(campionato,T):
    print("\n\n\n\nPunto 1 method \n")
    T.insert(INSERT,"\n CAMPIONATO :")
    T.insert(INSERT,campionato)
    T.insert(INSERT,"\n")

    squadre = set()


    for elem in campionati.__getitem__(campionato).partite:



        if(elem.giornata==1):   # OTTIMIZZAZIONE (ESEGUO L'ADD SOLO PER UNA GIORNATA E NON PER TUTTE )

            squadre.add(elem.sqcasa)
            squadre.add(elem.sqospite)
        if(squadre.__len__()==campionati.__getitem__(campionato).nsquadre):   break  # Esco dal ciclo appena raggiungo il num di squadre



    for elem in squadre:
        print(elem)
        T.insert(INSERT,elem )
        T.insert(INSERT,"\n")


def Punto2(campionato,giornata,T):
    print("\n\n\n\nPunto 2 method \n")
    T.insert( INSERT, "\n CAMPIONATO :" )
    T.insert( INSERT, campionato )
    T.insert( INSERT, "\n" )

    if (campionati.__getitem__( campionato ).ngiornate < giornata): T.insert( INSERT,"Il campionato contiene meno giornate" ); return 1;



    classifica = {}



    for elem in campionati.__getitem__(campionato).partite:

        if(elem.giornata==1): # CREO UN DICT DI SQUADRE CON PUNTEGGI A ZERO "CLASSIFICA INIZIALE"
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

        else: break  # Ottimizzazione







    print("Classifica Ordinata")
  #  items.sort( key=itemgetter( 1 ), reverse=True )
    classificaordinata = sorted( classifica.items(), key=operator.itemgetter( 1 ) ,reverse = True)

    for elem in classificaordinata.__iter__():
        print(elem[0],"Punti: ",elem[1]," Partite Giocate: ",giornata)

        T.insert(INSERT,elem[0])
        T.insert(INSERT," Punti: ")
        T.insert(INSERT,elem[1])
        T.insert(INSERT," Partite Giocate: ")
        T.insert(INSERT,giornata)
        T.insert(INSERT,"\n")


def Punto3(campionato,giornata,T):
    print("\n\n\n\nPunto 3 method \n")
    T.insert( INSERT, "\n CAMPIONATO :" )
    T.insert( INSERT, campionato )
    T.insert( INSERT, "\n" )

    if (campionati.__getitem__( campionato ).ngiornate < giornata): T.insert( INSERT,"Il campionato contiene meno giornate" ); return 1;
    classifica = {}

    for elem in campionati.__getitem__( campionato ).partite:

        if (elem.giornata == 1):  # CREO UN DICT DI SQUADRE CON PUNTEGGI A ZERO "CLASSIFICA INIZIALE"
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

        if(elem.giornata>giornata): break # ottimizzazione


    print("Classifica Ordinata")
    #  items.sort( key=itemgetter( 1 ), reverse=True )
    classificaordinata = sorted( classifica.items(), key=operator.itemgetter( 1 ), reverse=True )

    for elem in classificaordinata.__iter__():
        print(elem[0], " Punti: ", elem[1], " Partite Giocate: ", giornata)
        T.insert(INSERT,elem[0])
        T.insert(INSERT," Punti: ")
        T.insert(INSERT,elem[1])
        T.insert(INSERT," Partite Giocate",)
        T.insert(INSERT,giornata)
        T.insert(INSERT,"\n")


def Punto4(campionato,squadra,giornata,T):  #Inserito anche campionato poichè tra due camp diversi posso avere squadre cn nomi uguali

    print("\n\n\n\nPunto 4 method  \n")
    T.insert( INSERT, "\n CAMPIONATO :" )
    T.insert( INSERT, campionato )
    T.insert( INSERT, "\n" )
    cont=0
    if(campionati.__getitem__(campionato).ngiornate<giornata): T.insert(INSERT,"Il campionato contiene meno giornate"); return 1;
    for elem in campionati.__getitem__( campionato ).partite:

        if(giornata-5<0):
           if( elem.giornata <= giornata and (elem.sqospite == squadra or elem.sqcasa == squadra) ) :

               print(elem.sqcasa,elem.sqospite,elem.risultato,"Giornata: ",elem.giornata)
               T.insert( INSERT, elem.sqcasa )
               T.insert( INSERT, " - " )
               T.insert( INSERT, elem.sqospite )
               T.insert( INSERT, "Risultato: ", )
               T.insert( INSERT, elem.risultato )
               T.insert( INSERT, " Giornata: ", )
               T.insert( INSERT, giornata )
               T.insert( INSERT, "\n" )
               cont+=1





        elif (elem.giornata >= giornata-4 and elem.giornata<=giornata and (elem.sqospite==squadra or elem.sqcasa==squadra)):


            print(elem.sqcasa,elem.sqospite,elem.risultato,"Giornata: ",elem.giornata)
            T.insert( INSERT, elem.sqcasa )
            T.insert( INSERT, " - " )
            T.insert( INSERT, elem.sqospite )
            T.insert( INSERT, "Risultato: ", )
            T.insert( INSERT, elem.risultato )
            T.insert( INSERT, " Giornata: ", )
            T.insert( INSERT, giornata )
            T.insert( INSERT, "\n" )
            cont+=1

        elif(elem.giornata>giornata): break #ottimizzazione

    if(cont==0): T.insert( INSERT, "Squadra non esistente" )


def Punto5(data,T):

    print("\n\n\n\nPunto 5 method  \n")
    T.insert( INSERT, "\n Partite giocate in data :" )
    T.insert( INSERT,data )
    T.insert( INSERT, "\n" )

    i=0

    for elem in campionati.__iter__():

        for elem in campionati.__getitem__( elem ).partite:      ## VISITA DI TUTTE LE PARTITE DI TUTTI I CAMPIONATI
            print("QUI",data,elem.data)
            if(elem.data == data):
                i+=1

                T.insert(INSERT,elem)
                T.insert(INSERT," - ")
                T.insert(INSERT,elem.data)
                T.insert(INSERT,"\n")

    if(i==0):  T.insert(INSERT,"Non vi sono partite in questa data.")


def Punto6(giornata,k,T):
    print("\n\n\n\nPunto 6 method  \n")

    T.insert( INSERT,k)
    T.insert( INSERT, " Squadre che hanno segnato più gol fino alla giornata:" )
    T.insert( INSERT, giornata )
    T.insert( INSERT, "\n" )

    classifica={}

    for elem in campionati:
        for elem in campionati.__getitem__( elem ).partite:      ## VISITA DI TUTTE LE PARTITE DI TUTTI I CAMPIONATI
            if(elem.giornata<=giornata):


                if(not elem.sqcasa in classifica.keys()): classifica[elem.sqcasa]=elem.golcasa

                else: classifica[elem.sqcasa]+=elem.golcasa

                if (not elem.sqospite in classifica.keys()): classifica[elem.sqospite]=elem.golospite

                else: classifica[elem.sqospite]+=elem.golospite

            if(elem.giornata>giornata): break #ottimizzazione

    classificaordinata = sorted( classifica.items(), key=operator.itemgetter( 1 ), reverse=True )
    i = 0
    for elem in classificaordinata.__iter__():

        if(i<k):
            print(elem[0], "GoalFatti: ", elem[1], " Giornata: ", giornata)
            T.insert(INSERT,elem[0])
            T.insert(INSERT," Goal Fatti: ")
            T.insert(INSERT,elem[1])
            T.insert(INSERT,"\n")

        i+=1
        if(i>k): break   #ottimizza


def Punto7(giornata,k,T):
    print("\n\n\n\nPunto 7 method  \n")
    T.insert( INSERT, k )
    T.insert( INSERT, " Squadre che hanno segnato subito meno gol fino alla giornata:" )
    T.insert( INSERT, giornata )
    T.insert( INSERT, "\n" )

    classifica={}

    for elem in campionati:
        for elem in campionati.__getitem__( elem ).partite:      ## VISITA DI TUTTE LE PARTITE DI TUTTI I CAMPIONATI
            if(elem.giornata<=giornata):


                if(not elem.sqcasa in classifica.keys()): classifica[elem.sqcasa]=elem.golospite

                else: classifica[elem.sqcasa]+=elem.golospite

                if (not elem.sqospite in classifica.keys()): classifica[elem.sqospite]=elem.golcasa

                else: classifica[elem.sqospite]+=elem.golcasa

            if (elem.giornata > giornata): break  # ottimizzazione

    classificaordinata = sorted( classifica.items(), key=operator.itemgetter( 1 ), reverse=False )
    i = 0
    for elem in classificaordinata.__iter__():

        if(i<k):
            print(elem[0], "GoalSubiti: ", elem[1], " Giornata: ", giornata)
            T.insert( INSERT, elem[0] )
            T.insert( INSERT, " Goal Subiti: " )
            T.insert( INSERT, elem[1] )
            T.insert( INSERT, "\n" )

        i+=1
        if(i>k): break   #ottimizza


def Punto8(giornata,k,T):
    print("\n\n\n\nPunto 8 method  \n")
    T.insert( INSERT, k )
    T.insert( INSERT, " Squadre con miglior differenza reti fino alla giornata:" )
    T.insert( INSERT, giornata )
    T.insert( INSERT, "\n" )

    classifica={}

    for elem in campionati:
        for elem in campionati.__getitem__( elem ).partite:      ## VISITA DI TUTTE LE PARTITE DI TUTTI I CAMPIONATI
            if(elem.giornata<=giornata):


                if(not elem.sqcasa in classifica.keys()): classifica[elem.sqcasa]=elem.golcasa-elem.golospite

                else: classifica[elem.sqcasa]+=(elem.golcasa-elem.golospite)

                if (not elem.sqospite in classifica.keys()): classifica[elem.sqospite]=elem.golospite-elem.golcasa

                else: classifica[elem.sqospite]+=(elem.golospite-elem.golcasa)

            if (elem.giornata > giornata): break  # ottimizzazione

    classificaordinata = sorted( classifica.items(), key=operator.itemgetter( 1 ), reverse=True )
    i = 0
    for elem in classificaordinata.__iter__():

        if(i<k):
            print(elem[0], "Differenza Reti: ", elem[1], " Giornata: ", giornata)
            T.insert( INSERT, elem[0] )
            T.insert( INSERT, " Differenza reti: " )
            T.insert( INSERT, elem[1] )
            T.insert( INSERT, "\n" )

        i+=1
        if(i>k): break   #ottimizza


def Punto9(campionato,giornata,T):
    print("\n\n\n\nPunto 9 method  \n")

    T.insert( INSERT, "CAMPIONATO :" )
    T.insert( INSERT, campionato )
    T.insert( INSERT, " Giornata :" )
    T.insert( INSERT, giornata )
    T.insert( INSERT, "\n" )
    if (campionati.__getitem__( campionato ).ngiornate < giornata): T.insert( INSERT,"Il campionato contiene meno giornate" ); return 1;

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

        if (elem.giornata > giornata): break  # ottimizzazione



    classificaordinata = sorted( classifica.items(), key=operator.itemgetter( 1 ), reverse=True )
    classificaordinatacasa = sorted( classificacasa.items(), key=operator.itemgetter( 1 ), reverse=True )
    classificaordinatatrasf = sorted( classificatrasf.items(), key=operator.itemgetter( 1 ), reverse=True )


    print("\n\nClassifica Vittorie:")
    T.insert( INSERT, "\n Classifica Vittorie :\n" )
    for elem in classificaordinata.__iter__():


            print(elem[0], "Numero Vittorie : ", elem[1], " Giornata: ", giornata)

            T.insert( INSERT,elem[0] )
            T.insert( INSERT, " Numero Vittorie : " )
            T.insert( INSERT, elem[1] )
            T.insert( INSERT, " Giornata: " )
            T.insert(INSERT,giornata)
            T.insert( INSERT, "\n" )





    print("\n\nClassifica Vittorie Casa:")
    T.insert( INSERT, "\n Classifica Vittorie Casa:\n" )
    for elem1 in classificaordinatacasa.__iter__():

            print(elem1[0], "Numero Vittorie casa: ", elem1[1], " Giornata: ", giornata)
            T.insert( INSERT, elem1[0] )
            T.insert( INSERT, " Numero Vittorie casa : " )
            T.insert( INSERT, elem1[1] )
            T.insert( INSERT, " Giornata: " )
            T.insert( INSERT, giornata )
            T.insert( INSERT, "\n" )



    print("\n\nClassifica Vittorie Trasferta:")
    T.insert( INSERT, "\n Classifica Vittorie Trasferta:\n" )
    for elem2 in classificaordinatatrasf.__iter__():


            print(elem2[0], "Numero Vittorie trasf:", elem2[1], " Giornata: ", giornata)
            T.insert( INSERT, elem2[0] )
            T.insert( INSERT, " Numero Vittorie trasferta: " )
            T.insert( INSERT, elem2[1] )
            T.insert( INSERT, " Giornata: " )
            T.insert( INSERT, giornata )
            T.insert( INSERT, "\n" )


def PuntoExtra(t,p,T):
    def compute_kmp_fail(p):
        m = len( p )
        fail = [0] * m  # di default, fa una sovrapposizione di 0
        j = 1
        k = 0
        while j < m:  # calcola f(j) durante questo passaggio, se non è zero
            if p[j] == p[k]:  # k + 1 caratteri corrispondono
                fail[j] = k + 1
                j += 1
                k += 1
            elif k > 0:  # k seguono un riscontro di prefissi
                k = fail[k - 1]
            else:  # nessun uguaglianza trovata a j
                j += 1
        return fail

    def KMP_Count(t, p):
        n = len( t )
        m = len( p )
        pi = compute_kmp_fail( p )
        k = 0
        cont = 0
        for i in range( n ):
            while (k > 0 and p[k] != t[i]):
                if (pi is None):
                    print( "Pattern", p + "non trovato" )
                    T.insert( INSERT, "\n Pattern non trovato \n" )
                    return cont
                k = pi[k]
            if (p[k] == t[i]):
                k = k + 1
            if (k == m):
                cont += 1
                k = 0
            else:
                if (i == n - 1):
                    return cont
        return cont
    print("Punto extra method")
    T.insert(INSERT,"Pattern da cercare: ")
    T.insert(INSERT,p)
    T.insert(INSERT," In stringa: ")
    T.insert(INSERT,t)
    T.insert(INSERT,"\n")
    T.insert( INSERT, "Conteggio= " )
    T.insert(INSERT,KMP_Count(t,p))

######################### FINE METODI PUNTO 1-9

################# INIZIO METODI GESTIONE FINESTRE
def finestra1(finestra):

    def stampa():
        lista = ['E0','E1','E2','E3','EC','SC0','SC1','SC2','SC3','D1','D2','SP1','SP2','I1','I2','F1','F2','N1','B1','P1','T1','G1']




        if(lista.__contains__(combo.get()) ):

            # QUA RICHIAMO IL METODO PT1

            T.delete( '1.0', END )
            Punto1(combo.get(),T)



    finestra.destroy()  # Distruggo la finestra principale

    finestra = Tk()
    # Assegno dimensioni e titolo
    finestra.geometry( '580x500' )
    finestra.title( "Punto1" )

    # aggiungo elmenti

    testo = Label( finestra, text="Punto1", fg="blue", font=("Helvetica", 16) ).place(x=100,y=0)

    #Combobox

    combo=ttk.Combobox(finestra)
    combo.place(x=0,y=50);testo = Label( finestra, text="<-Seleziona Campionato").place(x=150,y=50)
    combo['values']=('E0','E1','E2','E3','EC','SC0','SC1','SC2','SC3','D1','D2','SP1','SP2','I1','I2','F1','F2','N1','B1','P1','T1','G1')


    bottone= Button(finestra,text="Stampa",command=stampa).pack(side=LEFT)

    T = Text(finestra ,height=40, width=50)
    T.place(x=100,y=100)

    scroll = Scrollbar( finestra, command=T.yview )
    T.configure( yscrollcommand=scroll.set )


    scroll.place(x=500,y=100)
  #  T.insert( INSERT, "....Premi Stampa e troverai qui l' Output....." )



    finestra.mainloop()


def finestra2(finestra):
    def stampa():
        lista = ['E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'SP1', 'SP2', 'I1', 'I2', 'F1',
                 'F2', 'N1', 'B1', 'P1', 'T1', 'G1']

        if (not entry.get().isdigit()):
            T.insert( END, "\nInserire un numero !!!\n" )

        elif (lista.__contains__( combo.get() ) and (int( entry.get() ) >= 1 and int( entry.get() ) <= 46)):

            # QUA RICHIAMO IL METODO PT1

            T.delete( '1.0', END )
            Punto2( combo.get(),int(entry.get()), T )

    finestra.destroy()  # Distruggo la finestra principale

    finestra = Tk()
    # Assegno dimensioni e titolo
    finestra.geometry( '580x500' )
    finestra.title( "Punto2" )

    # aggiungo elmenti

    testo = Label( finestra, text="Punto2", fg="blue", font=("Helvetica", 16) ).place( x=100, y=0 )

    # Combobox

    combo = ttk.Combobox( finestra )
    combo.place( x=0, y=50 );
    testo = Label( finestra, text="<-Seleziona Campionato" ).place( x=150, y=50 )
    combo['values'] = (
    'E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'SP1', 'SP2', 'I1', 'I2', 'F1', 'F2', 'N1',
    'B1', 'P1', 'T1', 'G1')

    # Entry
    entry = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Giornata" ).place( x=420, y=50 )
    entry.place( x=300, y=50 )
    bottone = Button( finestra, text="Stampa", command=stampa ).pack( side=LEFT )

    T = Text( finestra, height=40, width=50 )
    T.place( x=100, y=100 )

    scroll = Scrollbar( finestra, command=T.yview )
    T.configure( yscrollcommand=scroll.set )

    scroll.place( x=500, y=100 )
    #  T.insert( INSERT, "....Premi Stampa e troverai qui l' Output....." )



    finestra.mainloop()

def finestra3(finestra):
    def stampa():
        lista = ['E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'SP1', 'SP2', 'I1', 'I2', 'F1',
                 'F2', 'N1', 'B1', 'P1', 'T1', 'G1']

        if (not entry.get().isdigit()):
            T.insert( END, "\nInserire un numero !!!\n" )

        elif (lista.__contains__( combo.get() ) and (int( entry.get() ) >= 1 and int( entry.get() ) <= 46)):

            # QUA RICHIAMO IL METODO PT1

            T.delete( '1.0', END )
            Punto3( combo.get(),int(entry.get()), T )

    finestra.destroy()  # Distruggo la finestra principale

    finestra = Tk()
    # Assegno dimensioni e titolo
    finestra.geometry( '580x500' )
    finestra.title( "Punto3" )

    # aggiungo elmenti

    testo = Label( finestra, text="Punto3", fg="blue", font=("Helvetica", 16) ).place( x=100, y=0 )

    # Combobox

    combo = ttk.Combobox( finestra )
    combo.place( x=0, y=50 );
    testo = Label( finestra, text="<-Seleziona Campionato" ).place( x=150, y=50 )
    combo['values'] = (
    'E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'SP1', 'SP2', 'I1', 'I2', 'F1', 'F2', 'N1',
    'B1', 'P1', 'T1', 'G1')

    # Entry
    entry = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Giornata" ).place( x=420, y=50 )
    entry.place( x=300, y=50 )
    bottone = Button( finestra, text="Stampa", command=stampa ).pack( side=LEFT )

    T = Text( finestra, height=40, width=50 )
    T.place( x=100, y=100 )

    scroll = Scrollbar( finestra, command=T.yview )
    T.configure( yscrollcommand=scroll.set )

    scroll.place( x=500, y=100 )
    #  T.insert( INSERT, "....Premi Stampa e troverai qui l' Output....." )



    finestra.mainloop()
def finestra4(finestra):
    def stampa():
        lista = ['E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'SP1', 'SP2', 'I1', 'I2', 'F1',
                 'F2', 'N1', 'B1', 'P1', 'T1', 'G1']

        T.delete( '1.0', END )
        if (not entry.get().isdigit() or entry2.get().isdigit()):
            T.insert( INSERT, "\nInserimento errato !!!\n" )



        elif (lista.__contains__( combo.get() ) and (int( entry.get() ) >= 1 and int( entry.get() ) <= 46)):

            # QUA RICHIAMO IL METODO PT1


            Punto4( combo.get(),entry2.get(),int(entry.get()), T )

    finestra.destroy()  # Distruggo la finestra principale

    finestra = Tk()
    # Assegno dimensioni e titolo
    finestra.geometry( '800x500' )
    finestra.title( "Punto4" )

    # aggiungo elmenti

    testo = Label( finestra, text="Punto4", fg="blue", font=("Helvetica", 16) ).place( x=100, y=0 )

    # Combobox

    combo = ttk.Combobox( finestra )
    combo.place( x=0, y=50 );
    testo = Label( finestra, text="<-Seleziona Campionato" ).place( x=150, y=50 )
    combo['values'] = (
    'E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'SP1', 'SP2', 'I1', 'I2', 'F1', 'F2', 'N1',
    'B1', 'P1', 'T1', 'G1')

    # Entry
    entry = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Giornata" ).place( x=420, y=50 )
    entry.place( x=300, y=50 )

    entry2 = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Squadra" ).place( x=660, y=50 )
    entry2.place( x=540, y=50 )
    bottone = Button( finestra, text="Stampa", command=stampa ).pack( side=LEFT )

    T = Text( finestra, height=40, width=50 )
    T.place( x=100, y=100 )

    scroll = Scrollbar( finestra, command=T.yview )
    T.configure( yscrollcommand=scroll.set )

    scroll.place( x=500, y=100 )
    #  T.insert( INSERT, "....Premi Stampa e troverai qui l' Output....." )



    finestra.mainloop()
def finestra5(finestra):
    def stampa():


        T.delete( '1.0', END )
        if (entry.get().isdigit()):
            T.insert( INSERT, "\nInserimento errato !!!\n" )



        else :

            Punto5((entry.get()), T )

    finestra.destroy()  # Distruggo la finestra principale

    finestra = Tk()
    # Assegno dimensioni e titolo
    finestra.geometry( '800x500' )
    finestra.title( "Punto5" )

    # aggiungo elmenti

    testo = Label( finestra, text="Punto5", fg="blue", font=("Helvetica", 16) ).place( x=100, y=0 )





    # Entry
    entry = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui data" ).place( x=420, y=50 )
    entry.place( x=300, y=50 )


    bottone = Button( finestra, text="Stampa", command=stampa ).pack( side=LEFT )

    T = Text( finestra, height=40, width=50 )
    T.place( x=100, y=100 )

    scroll = Scrollbar( finestra, command=T.yview )
    T.configure( yscrollcommand=scroll.set )

    scroll.place( x=500, y=100 )
    #  T.insert( INSERT, "....Premi Stampa e troverai qui l' Output....." )



    finestra.mainloop()

def finestra6(finestra):
    def stampa():
        lista = ['E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'SP1', 'SP2', 'I1', 'I2', 'F1',
                 'F2', 'N1', 'B1', 'P1', 'T1', 'G1']

        T.delete( '1.0', END )
        if (not entry.get().isdigit() or (not entry2.get().isdigit())):
            T.insert( INSERT, "\nInserimento errato !!!\n" )



        elif ( (int( entry.get() ) >= 1 and int( entry.get() ) <= 46)):

            # QUA RICHIAMO IL METODO PT1


            Punto6( int(entry.get()),int(entry2.get()), T )

    finestra.destroy()  # Distruggo la finestra principale

    finestra = Tk()
    # Assegno dimensioni e titolo
    finestra.geometry( '1000x500' )
    finestra.title( "Punto6" )

    # aggiungo elmenti

    testo = Label( finestra, text="Punto6", fg="blue", font=("Helvetica", 16) ).place( x=100, y=0 )

    # Combobox




    # Entry
    entry = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Giornata" ).place( x=420, y=50 )
    entry.place( x=300, y=50 )

    entry2 = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Intero k" ).place( x=660, y=50 )
    entry2.place( x=540, y=50 )
    bottone = Button( finestra, text="Stampa", command=stampa ).pack( side=LEFT )

    T = Text( finestra, height=40, width=100 )
    T.place( x=100, y=100 )

    scroll = Scrollbar( finestra, command=T.yview )
    T.configure( yscrollcommand=scroll.set )

    scroll.place( x=900, y=100 )
    #  T.insert( INSERT, "....Premi Stampa e troverai qui l' Output....." )



    finestra.mainloop()
def finestra7(finestra):
    def stampa():
        lista = ['E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'SP1', 'SP2', 'I1', 'I2', 'F1',
                 'F2', 'N1', 'B1', 'P1', 'T1', 'G1']

        T.delete( '1.0', END )
        if (not entry.get().isdigit() or (not entry2.get().isdigit())):
            T.insert( INSERT, "\nInserimento errato !!!\n" )



        elif ( (int( entry.get() ) >= 1 and int( entry.get() ) <= 46)):

            # QUA RICHIAMO IL METODO PT1


            Punto7( int(entry.get()),int(entry2.get()), T )

    finestra.destroy()  # Distruggo la finestra principale

    finestra = Tk()
    # Assegno dimensioni e titolo
    finestra.geometry( '1000x500' )
    finestra.title( "Punto7" )

    # aggiungo elmenti

    testo = Label( finestra, text="Punto7", fg="blue", font=("Helvetica", 16) ).place( x=100, y=0 )

    # Combobox




    # Entry
    entry = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Giornata" ).place( x=420, y=50 )
    entry.place( x=300, y=50 )

    entry2 = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Intero k" ).place( x=660, y=50 )
    entry2.place( x=540, y=50 )
    bottone = Button( finestra, text="Stampa", command=stampa ).pack( side=LEFT )

    T = Text( finestra, height=40, width=100 )
    T.place( x=100, y=100 )

    scroll = Scrollbar( finestra, command=T.yview )
    T.configure( yscrollcommand=scroll.set )

    scroll.place( x=900, y=100 )
    #  T.insert( INSERT, "....Premi Stampa e troverai qui l' Output....." )



    finestra.mainloop()
def finestra8(finestra):
    def stampa():
        lista = ['E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'SP1', 'SP2', 'I1', 'I2', 'F1',
                 'F2', 'N1', 'B1', 'P1', 'T1', 'G1']

        T.delete( '1.0', END )
        if (not entry.get().isdigit() or (not entry2.get().isdigit())):
            T.insert( INSERT, "\nInserimento errato !!!\n" )



        elif ( (int( entry.get() ) >= 1 and int( entry.get() ) <= 46)):

            # QUA RICHIAMO IL METODO PT1


            Punto8( int(entry.get()),int(entry2.get()), T )

    finestra.destroy()  # Distruggo la finestra principale

    finestra = Tk()
    # Assegno dimensioni e titolo
    finestra.geometry( '1000x500' )
    finestra.title( "Punto8" )

    # aggiungo elmenti

    testo = Label( finestra, text="Punto8", fg="blue", font=("Helvetica", 16) ).place( x=100, y=0 )

    # Combobox




    # Entry
    entry = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Giornata" ).place( x=420, y=50 )
    entry.place( x=300, y=50 )

    entry2 = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Intero k" ).place( x=660, y=50 )
    entry2.place( x=540, y=50 )
    bottone = Button( finestra, text="Stampa", command=stampa ).pack( side=LEFT )

    T = Text( finestra, height=40, width=100 )
    T.place( x=100, y=100 )

    scroll = Scrollbar( finestra, command=T.yview )
    T.configure( yscrollcommand=scroll.set )

    scroll.place( x=900, y=100 )
    #  T.insert( INSERT, "....Premi Stampa e troverai qui l' Output....." )



    finestra.mainloop()

def finestra9(finestra):
    def stampa():
        lista = ['E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'SP1', 'SP2', 'I1', 'I2', 'F1',
                 'F2', 'N1', 'B1', 'P1', 'T1', 'G1']

        if (not entry.get().isdigit()):
            T.insert( END, "\nInserire un numero !!!\n" )

        elif (lista.__contains__( combo.get() ) and (int( entry.get() ) >= 1 and int( entry.get() ) <= 46)):

            # QUA RICHIAMO IL METODO PT1

            T.delete( '1.0', END )
            Punto9( combo.get(),int(entry.get()), T )

    finestra.destroy()  # Distruggo la finestra principale

    finestra = Tk()
    # Assegno dimensioni e titolo
    finestra.geometry( '1000x500' )
    finestra.title( "Punto9" )

    # aggiungo elmenti

    testo = Label( finestra, text="Punto9", fg="blue", font=("Helvetica", 16) ).place( x=100, y=0 )

    # Combobox

    combo = ttk.Combobox( finestra )
    combo.place( x=0, y=50 );
    testo = Label( finestra, text="<-Seleziona Campionato" ).place( x=150, y=50 )
    combo['values'] = (
    'E0', 'E1', 'E2', 'E3', 'EC', 'SC0', 'SC1', 'SC2', 'SC3', 'D1', 'D2', 'SP1', 'SP2', 'I1', 'I2', 'F1', 'F2', 'N1',
    'B1', 'P1', 'T1', 'G1')

    # Entry
    entry = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Giornata" ).place( x=420, y=50 )
    entry.place( x=300, y=50 )
    bottone = Button( finestra, text="Stampa", command=stampa ).pack( side=LEFT )

    T = Text( finestra, height=40, width=100 )
    T.place( x=100, y=100 )

    scroll = Scrollbar( finestra, command=T.yview )
    T.configure( yscrollcommand=scroll.set )

    scroll.place( x=900, y=100 )
    #  T.insert( INSERT, "....Premi Stampa e troverai qui l' Output....." )



    finestra.mainloop()

def finestraextra(finestra):
    def stampa():

        T.delete( '1.0', END )

        PuntoExtra( entry2.get(),entry.get(),T)



    finestra.destroy()  # Distruggo la finestra principale

    finestra = Tk()
    # Assegno dimensioni e titolo
    finestra.geometry( '580x500' )
    finestra.title( "Punto Extra" )

    # aggiungo elmenti

    testo = Label( finestra, text="Punto Extra", fg="blue", font=("Helvetica", 16) ).place( x=100, y=0 )

    # Entry
    entry = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Pattern" ).place( x=120, y=50 )
    entry.place( x=0, y=50 )

    entry2 = Entry( finestra );
    testo = Label( finestra, text="<-Scrivi qui Stringa" ).place( x=400, y=50 )
    entry2.place( x=250, y=50 )
    bottone = Button( finestra, text="Stampa", command=stampa ).pack( side=LEFT )

    T = Text( finestra, height=40, width=50 )
    T.place( x=100, y=100 )

    scroll = Scrollbar( finestra, command=T.yview )
    T.configure( yscrollcommand=scroll.set )

    scroll.place( x=500, y=100 )

    finestra.mainloop()

#Creo la finestra principale ###################################

def finestraprincipale():
    finestra = Tk()

#Assegno dimensioni e titolo
    finestra.geometry('320x300')
    finestra.title("Home")



#aggiungo elmenti

    testo = Label(finestra,text="PROGETTO 3 GRUPPO 7",fg="blue",font=("Helvetica",16)).grid(row=0,column=1)

    testo = Label(finestra,text="").grid(row=1,column=1) # Crea spazio vuoto
#Bottoni


    bottone1= Button(finestra,text="1", font=("HELVETICA",16),command= lambda: finestra1(finestra),bg="red").grid(row=2,column=0)
    bottone2= Button(finestra,text="2",font=("HELVETICA",16), command=lambda: finestra2(finestra),bg="red").grid(row=2,column=1)
    bottone3= Button(finestra,text="3",font=("HELVETICA",16), command=lambda: finestra3(finestra),bg="red").grid(row=2,column=2)
    bottone4= Button(finestra,text="4", font=("HELVETICA",16),command=lambda: finestra4(finestra),bg="red").grid(row=3,column=0)
    bottone5= Button(finestra,text="5",font=("HELVETICA",16), command=lambda: finestra5(finestra),bg="red").grid(row=3,column=1)
    bottone6= Button(finestra,text="6",font=("HELVETICA",16), command=lambda: finestra6(finestra),bg="red").grid(row=3,column=2)
    bottone7= Button(finestra,text="7", font=("HELVETICA",16),command=lambda: finestra7(finestra),bg="red").grid(row=4,column=0)
    bottone8= Button(finestra,text="8",font=("HELVETICA",16), command=lambda: finestra8(finestra),bg="red").grid(row=4,column=1)
    bottone9= Button(finestra,text="9",font=("HELVETICA",16), command=lambda: finestra9(finestra),bg="red").grid(row=4,column=2)



    testo = Label(finestra,text="").grid(row=5,column=1) # Crea spazio vuoto

    testo = Label(finestra,text="Cliccare su un pulsante per svolgere il relativo punto",fg="blue",font=("Helvetica",8)).grid(row=6,column=1)
    bottone10 = Button( finestra, text="EXTRA", font=("HELVETICA", 14), command=lambda: finestraextra( finestra ),bg="blue" ).grid( row=7, column=1 )

#Avvio la finestra

    finestra.mainloop()


########################################FINE METODI GESTIONE FINESTRE

########################################   M A I N

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

    dict = {} # dizionario di appoggio utile alla riorganizzazione delle partite  [giornata,count]

    giorn = 0 # variabile di appoggio utile per gestire il dict

    k+=1
    squadre=set()
    for j in range(1,sheet.nrows):

         for i in range (3,4):
            squadre.add(sheet.cell_value(j,i))


         for i in range(1):
             if (int( sheet.cell_value( j, i ) ) > giorn):
                 giorn = int( sheet.cell_value( j, i ) );  # alla fine dei due for giorn è il numero di giornate


    for j in range(1,giorn):
        dict[j]=0;






    n=squadre.__len__()
    campionati.__getitem__( campionato.get_nome() ).nsquadre=n  #Conto le squadre
    cont=0
    giornata=1





    for j in range(1,sheet.nrows):
            giornata = sheet.cell_value( j, 0 )
            data = sheet.cell_value( j, 2 )
            sqcasa=sheet.cell_value(j,3)
            sqospite=sheet.cell_value(j,4)
            golcasa=int(sheet.cell_value(j,5))
            golospite=int(sheet.cell_value(j,6))
            golcasaprimo=(sheet.cell_value(j,8))   # va fattto il cast a intero ma prima va aggiustato il file (elem vuoti)

            golospiteprimo=sheet.cell_value(j,9)
            risultato=sheet.cell_value(j,7)
            count=j


            y, m, d, h, i, s = xldate_as_tuple(data, book.datemode)

            data="{0}/{1}/{2}".format(d, m, y)
        #    print("Data",data)
            if(giornata>campionato.ngiornate): campionato.ngiornate=giornata

            if(j>1):
              if(giornata <int(sheet.cell_value( count, 0 ))):  # se la giornata è minore della precedente la partita è rinviata (IDENTIFICO LA PARTITA RINVIATA)

                  print("quaaa",giornata,(sheet.cell_value( count, 0 )))
                  campionato.set_partita_inorder(campionato.Partita( sqcasa, sqospite, golcasa, golospite, golcasaprimo, golospiteprimo,risultato, data, giornata ) )
              else : campionato.set_partita(campionato.Partita(sqcasa,sqospite,golcasa,golospite,golcasaprimo,golospiteprimo,risultato,data,giornata))


            else : campionato.set_partita(campionato.Partita(sqcasa,sqospite,golcasa,golospite,golcasaprimo,golospiteprimo,risultato,data,giornata))

    leagues.insert(contcamp,campionato)
    contcamp+=1

   # campionati.__getitem__( campionato.get_nome() ).partite.sort()


#for elem in campionati:  # ORDINO I CAMPIONATI PER RIORGANIZZARE GIORNATE RINVIATE
 #   campionati[elem].partite.sort()

for elem in campionati:
    print(campionati[elem].print_partite())


print("\n\n################## PRESI TUTTI I VALORI ################### \n\n")


finestraprincipale()   # INIZIA TUTTO DALLA CREAZIONE DI FINESTRA PRINCIPALE