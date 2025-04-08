def discount(prices, isPet, nItems):
    SCONTO_APPLICATO = 0.2
    print(prices, isPet, nItems, sep="\n")
    if (nItems == 0 or
        nItems < 6 or
        len(set(isPet)) == 1):
        return 0.00;
    i = 0
    cnt = 0
    somma = 0.0
    while i < nItems:
        if not isPet[i]: # siccome isPet[i] e True se l'i-esimo
                         # elemento è un animale, not è il contrario
            somma += prices[i]
            cnt += 1
        i += 1
    if cnt >= 5:
        return somma * SCONTO_APPLICATO
    else:
        return 0.00;

prezzi = []
animale = []
counter = 0
riga = input("Passami prezzo e Y/N: ")
while riga != "-1":
    prezzi.append(float(riga[0:riga.find(" ")]))
    animale.append(riga[-1] == "Y")
    counter += 1
    riga = input("Passami prezzo e Y/N: ")
print(discount(prezzi, animale, counter))    