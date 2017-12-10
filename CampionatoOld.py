from TdP_collections.hash_table.chain_hash_map import ChainHashMap
import bisect
class Campionato():

    class Partita():
        def __init__(self,sqcasa,sqospite,golcasa,golospite,golcasaprimo,golospiteprimo,risultato,data,giornata):

            self.sqcasa=sqcasa
            self.sqospite=sqospite
            self.golcasa=golcasa
            self.golospite=golospite
            self.golcasaprimo=golcasaprimo
            self.golospiteprimo=golospiteprimo
            self.risultato=risultato
            self.data = data # Stringa in formato data g/m/a
            self.giornata = giornata # n° giornata

        def __str__(self):
            return (self.sqcasa + " - " + self.sqospite + " RIS = "+str(self.golcasa)+"-"+str(self.golospite)+" Giornata="+str(self.giornata))

        def __lt__(self,partita):
            return self.giornata < partita.giornata



    def __init__(self, nome): # Inizializzo Campionato

        self.nome = nome
        self.partite = list()
        self.ngiornate=0
        self.nsquadre=0



    def get_nome(self):
        if(self.nome is not None):
            return self.nome

    def set_partita(self,partita): # Serve Per allocare la partita

        self.partite.append(partita)

    def set_partita_inorder(self,partita):

            bisect.insort(self.partite,partita)

    def __contains__(self, item):
        if isinstance(item,self.Partita):
            return self.partite.__contains__(item)
        raise TypeError()

    def __getitem__(self, item):
        if (self.partite.__contains__(item)):
            return self.partite.__getitem__(item)
        raise IndexError()



    def print_partite(self):

        for elem in self.partite.__iter__():

            print(elem)


    def print_campionato(self):

        print("Campionato: ",self.nome)
        print("Partite:")
        self.print_partite()


