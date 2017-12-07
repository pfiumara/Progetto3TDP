import xlrd
import calendar
from Campionato import Campionato
book = xlrd.open_workbook("all-euro-data-2016-2017.xls")
nsheet=book.nsheets
contcamp=0
leagues=[]
while contcamp!=nsheet:
    sheet = book.sheet_by_index(contcamp)
    campionato=Campionato(sheet.cell_value(1,1))
    squadre=set()
    for j in range(1,sheet.nrows):
        for i in range (2,4):
            squadre.add(sheet.cell_value(j,i))
    n=squadre.__len__()
    cont=0

    for j in range(1,sheet.nrows):
            giornata=sheet.cell_value(j,0)
            sqcasa=sheet.cell_value(j,3)
            sqospite=sheet.cell_value(j,4)
            golcasa=sheet.cell_value(j,5)
            golospite=sheet.cell_value(j,6)
            golcasaprimo=sheet.cell_value(j,8)
            golospiteprimo=sheet.cell_value(j,9)
            risultato=sheet.cell_value(j,7)
            data=sheet.cell_value(j,2)
            y, m, d, h, i, s = xlrd.xldate_as_tuple(data, book.datemode)
            data="{0} - {1} - {2}".format(d, m, y)
            print("Data",data)
            print ("Anno",data[0])
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

print("Punto1:")
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
