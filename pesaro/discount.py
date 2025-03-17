def main() :
    lista_prezzi = [ ]
    lista_pet    = [ ]
    acquisisci_vendita(lista_prezzi, lista_pet)
    sconto = discount(lista_prezzi, lista_pet, len(lista_pet))
    print(round(sconto, 2))    
    
def discount(prices, isPet, nItems) :
    PERC_SCONTO = 0.2
#    print(prices)
#    print(isPet)
#    print(nItems)
    counter = 0
    nonAnimali = 0
    parziale = 0.0
    if len(isPet) != nItems :
        raise ValueError("Il numero di voci isPet non è coerente con nItems")
    if len(prices) != nItems :
        raise ValueError("Il numero di voci prices non è coerente con nItems")
    almeno_uno = False
    for pet in isPet :
        almeno_uno = almeno_uno or pet
        if not pet :
            nonAnimali += 1
            parziale += prices[counter]
        counter += 1           
    if almeno_uno and nonAnimali >= 5 :
        return(PERC_SCONTO * parziale)          
    return (0.0)

def acquisisci_vendita(prices, isPet) :
    riga = input()
    while riga != "-1" :
        pos = riga.find(" ")
        if pos == -1 :
            raise ValueError("Manca il separatore tra prezzo e Y/N")
        prices.append(float(riga[ : pos]))    
        if riga[pos + 1 : ] == "Y" :
            isPet.append(True)
        else :    
            isPet.append(False)
        riga = input()
    
main()