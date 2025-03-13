import pickle
FILE_APPUNTAMENTI = 'appuntamenti'
from os.path import exists
listaAppuntamenti = {}

class Appuntamento :
    def __init__(self, text, aaaa, mm, gg) :
        self._desc   = text
        self._anno   = aaaa
        self._mese   = mm
        self._giorno = gg    
    def occursOn(self, aaaa, mm, gg) :  
        pass           # il metodo deve essere sovrascritto dalla classe derivata
    def __repr__(self) :
        pass           # il metodo deve essere sovrascritto dalla classe derivata

class Occasionale(Appuntamento) :
    def __init__(self, text, aaaa, mm, gg) :
        super().__init__(text, aaaa, mm, gg)
    def occursOn(self, aaaa, mm, gg) :  
        occurs = (self._anno == aaaa) and (self._mese == mm) and (self._giorno == gg)
        return occurs
    def __repr__(self) :
        return f"Occasionale {self._giorno}/{self._mese}/{self._anno}: '{self._desc}'\n"

class Annuale(Appuntamento) :
    def __init__(self, text, mm, gg) :
        super().__init__(text, None, mm, gg)
    def occursOn(self, mm, gg) :  
        occurs = (self._mese == mm) and (self._giorno == gg)
        return occurs
    def __repr__(self) :
        return f"Annuale mese {self._mese} giorno {self._giorno}: '{self._desc}'\n"
    
class Mensile(Appuntamento) :
    def __init__(self, text, gg) :
        super().__init__(text, None, None, gg)
    def occursOn(self, aaaa, mm, gg) :  
        occurs = (self._giorno == gg)
        return occurs
    def __repr__(self) :
        return f"Mensile giorno {self._giorno}: '{self._desc}'\n"
    
def main() :
    print("""
        Progamma Gestione Appuntamenti

          Indicare una lettera per scegliere la funzione:

            s = ricerca appuntamenti in data indicata
            i = inserimento nuovo appuntamento (occasionale)
            a = inserimento nuovo appuntamento (annuale)
            m = inserimento nuovo appuntamento (mensile)
            l = lista gli appuntamenti
            q = uscita
            
        """)
    funzione = input().upper()
    caricaDati(listaAppuntamenti)
    while funzione != "Q" :
        if funzione == "L" :
            print(listaAppuntamenti['root'])
        if funzione == "I" :
            listaAppuntamenti['root'].append(Occasionale(
                  input("Descrivi appuntamento: ")
            , int(input("Indica anno: "))
            , int(input("Indica mese: "))
            , int(input("Indica giorno: "))))
        if funzione == "A" :
            listaAppuntamenti['root'].append(Annuale(
                  input("Descrivi appuntamento: ")
            , int(input("Indica mese: "))
            , int(input("Indica giorno: "))))
        if funzione == "M" :
            listaAppuntamenti['root'].append(Mensile(
                  input("Descrivi appuntamento: ")
            , int(input("Indica giorno: "))))
        if funzione == "S" :
            aaaa = int(input("Indica anno: "))
            mm   = int(input("Indica mese: "))
            gg   = int(input("Indica giorno: "))
            for e in listaAppuntamenti['root'] :
                if (e.occursOn(aaaa, mm, gg)) : 
                    print(e)
        funzione = input().upper()
    salvaDati(listaAppuntamenti)    
    
    
def caricaDati(lista) :
    if exists(FILE_APPUNTAMENTI) :
        dbfile = open(FILE_APPUNTAMENTI, 'rb')  
        l = pickle.load(dbfile)
        lista['root']=l
        dbfile.close()
    else :    
        lista['root']=[]

def salvaDati(lista) :
    dbfile = open(FILE_APPUNTAMENTI, 'wb')  
    pickle.dump(lista['root'], dbfile)
    dbfile.close()    
    
main()    