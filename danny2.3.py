import datetime
import os

listafinale=[]
listaProdotti=[]
prodotto=''
nomeprodotto=''
data=''

#PROCEDURA RICERCA DATA
today = datetime.date.today()
differenza = datetime.timedelta(days=1)
domani = today + differenza
data=str(domani.day)+'/'+str(domani.month)+'/'+str(domani.year)
#PROCEDURA RICERCA DATA
#print ('-------------')

aggiorna=0
f=open('C:\\Users\\f.altarocca\\Documents\\coding\\Python\\scripts38\\DannyKaye\\prodotti\\prodottiDanny.txt','r')
prodotti=f.readlines()
f.close()
for elemento in prodotti:
    rigaSplit=elemento.split(';')
    listaProdotti.append(rigaSplit[0])
    if '\n' in rigaSplit[1]:
        rigaSplit[1]=rigaSplit[1][:-1]
    listaProdotti.append(rigaSplit[1])   
#print (listaProdotti)
f=open('C:\\Users\\f.altarocca\\Documents\\coding\\Python\\scripts38\\DannyKaye\\dannyOrdineDaMail.csv','r')
ordine=f.readlines()
f.close()

###aggiunta a capo finale
if '\n' not in ordine[len(ordine)-1]:
    ordine[len(ordine)-1]=ordine[len(ordine)-1]+'\n'
###aggiunta a capo finale

for elemento in ordine:
    if elemento != '\n':
        #print (elemento)
        riga=elemento.split(' ')
        #print (riga)
        for pezzo in riga:
            #quantita=''
            #print (pezzo)
            if '\n' in pezzo:
                #print('IN - '+pezzo)
                #individua ultimo elemento di riga
                if 'KG' in pezzo.upper() or 'K' in pezzo.upper() or 'MZ' in pezzo.upper() or 'MAZZI' in pezzo.upper() or 'MAZZO' in pezzo.upper() or 'CS' in pezzo.upper() or 'CF' in pezzo.upper() or 'PZ' in pezzo.upper()or 'CASSE' in pezzo.upper()or 'PEZZO' in pezzo.upper()or 'PEZZI' in pezzo.upper():
                    quantita=riga[riga.index(pezzo)-1]
                    #print ('qta '+quantita)
                    isthereNumber=(any(chr.isdigit() for chr in quantita))
                    if not isthereNumber:
                        #print ('PROD --> '+nomeprodotto)
                        #quantita=riga[riga.index(pezzo)+1]
                        quantita=''
                        for char in pezzo:
                            if char.isdigit():
                                quantita=quantita+char
                    elif 'CAL.' in quantita.upper():
                        quantita=riga[riga.index(pezzo)][:-1].split('K')[0]
                    if quantita=='':
                        quantita=input(nomeprodotto.upper()+' quantita mancante, inseriscila:')
                elif 'COSTE' in pezzo or 'PALLE' in pezzo:
                    isthereNumber=(any(chr.isdigit() for chr in pezzo))
                    if isthereNumber:
                        #procedura ES: 10COSTE
                        quantita=''
                        #print (isthereNumber)
                        for lettera in pezzo:
                            if lettera.isdigit():
                                quantita=quantita+lettera
                    else:
                        posizione=riga.index(pezzo)
                        quantita=riga[posizione-1]
                #print(nomeprodotto.upper())
                elif len(riga)<=2:
                    print (nomeprodotto.upper())
                    print (riga[len(riga)-1])
                    if '\n' in riga[len(riga)-1]:
                        quantita=riga[len(riga)-1][:-1]
                    else:
                        quantita=riga[len(riga)-1]
                listafinale.append(nomeprodotto.upper())
                if ',' in quantita:
                    appQ=quantita.split(',')
                    quantita='.'.join(appQ)
                listafinale.append(quantita)
                #print (nomeprodotto+' - '+quantita)
                nomeprodotto=''
            else:
                if not pezzo.isdecimal(): 
                    nomeprodotto=nomeprodotto.upper()+pezzo

#print (listafinale)
i=0
while i<= len (listafinale)-1:
    prodotto=listafinale[i]
    if prodotto in listaProdotti:
        indice=listaProdotti.index(prodotto)
        listafinale[i]=listaProdotti[indice+1]
    else:
        #pass #procedura prodotto non trovato
        nuovoCodice=input(prodotto+' non trovato, inserisci il codice')
        prodotti.append(prodotto+';'+nuovoCodice+'\n')
        listafinale[i]=nuovoCodice.upper()
        aggiorna=1
    i=i+2
#print (listafinale)
f=open('C:\\Users\\f.altarocca\\Desktop\\ordineDanny.csv','w')
f.write('CODICE ADHOC,SEDE,CENTRO COSTO,COD.PRODOTTO,PEZZI,DATA EVASIONE,ORARIO\n')
i=0
while i<= len (listafinale)-2:
    f.write('200,00001,DISTRIBUZIONE,'+listafinale[i]+','+listafinale[i+1]+','+data+'\n')
    i=i+2
f.close()
if aggiorna==1:
    os.unlink('C:\\Users\\f.altarocca\\Documents\\coding\\Python\\scripts38\\DannyKaye\\prodotti\\prodottiDanny.txt')
    f=open('C:\\Users\\f.altarocca\\Documents\\coding\\Python\\scripts38\\DannyKaye\\prodotti\\prodottiDanny.txt','w')
    for elemento in prodotti:
        f.write(elemento)
    f.close()
