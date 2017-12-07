from Campionato import Campionato






camp = Campionato("SerieA")


camp.set_partita(camp.Partita("Sal","Bol",0,1,1,0,"H"))
camp.set_partita(camp.Partita("Ata","Bol",5,1,1,0,"D"))
camp.set_partita(camp.Partita("Gas","Nol",0,1,1,10,"H"))
camp.set_partita(camp.Partita("Lal","Maol",2,1,1,0,"A"))



#camp.set_partite(partita)

camp.print_campionato()

