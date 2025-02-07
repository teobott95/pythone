from random import randint
def main() :
    game = False
    punti_1 = 0
    punti_2 = 0
    while not game:
        punto = randint(1, 2)
        if punto == 1 :
            punti_1 += 1
        else :
            punti_2 += 1
        if ((punti_1 == 4 and punti_2 < 3) or
            (punti_1 > 4 and punti_2 < punti_1 - 1)) :
            print("Game player 1")
            game = True
        if ((punti_2 == 4 and punti_1 < 3) or
            (punti_2 > 4 and punti_1 < punti_2 - 1)) :
            print("Game player 2")
            game = True
        if not game :    
            decodifica(punti_1, punti_2)    
        
def decodifica(p1, p2) :
    if p1 == 1 and p2 == 0 :
        print("15-Love")
    elif p1 == 0 and p2 == 1 :
        print("Love-15")
    elif p1 == 1 and p2 == 1 :
        print("15-all")
    elif p1 == 2 and p2 == 0 :
        print("30-Love")
    elif p1 == 0 and p2 == 2 :
        print("Love-30")
    elif p1 == 2 and p2 == 1 :
        print("30-15")
    elif p1 == 1 and p2 == 2 :
        print("15-30")
    elif p1 == 2 and p2 == 2 :
        print("30-all")
    elif p1 == 3 and p2 == 0 :
        print("40-Love")
    elif p1 == 0 and p2 == 3 :
        print("Love-40")
    elif p1 == 3 and p2 == 1 :
        print("40-15")
    elif p1 == 1 and p2 == 3 :
        print("15-40")
    elif p1 == 3 and p2 == 2 :
        print("40-30")
    elif p1 == 2 and p2 == 3 :
        print("30-40")
    elif p1 == p2 :
        print("deuce")
    elif p1 > p2 :
        print("Advantage player 1")
    elif p2 > p1 :
        print("Advantage player 2")        
        
main()  