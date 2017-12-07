from TdP_collections.hash_table.chain_hash_map import ChainHashMap
from Campionato import Campionato
from imported_xlrd import xlrd

camp = Campionato("SerieA")


camp.set_partita(camp.Partita("Sal","Bol",0,1,1,0,"H",0,0))
camp.set_partita(camp.Partita("Ata","Bol",5,1,1,0,"D",0,0))
camp.set_partita(camp.Partita("Gas","Nol",0,1,1,10,"H",0,0))
camp.set_partita(camp.Partita("Lal","Maol",2,1,1,0,"A",0,0))

partita = camp.Partita("ATA","GA",2,1,1,0,"A",0,0)

camp.set_partita(partita)


print("stampa singola",camp.__getitem__(partita),"\n")


camp.print_campionato()
# USARE COME CHIAAVE LA PARTITA STESSA
