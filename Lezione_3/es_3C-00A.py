n:int = int(input("Quanti neonati sono nati? "))    #input per inserire il numero dei neonati

match n:                                            #match per vedere quanti neonati sono nati
    case 1:
        print("Congratulazioni")
    case 2: 
        print("Wow! Gemelli!")
    case 3:
        print("Wow! Tre!")
    case 4:
        print("Mamma mia Quattro! Wow!")
    case 5:
        print("Incredibile! Cinque!")
    case _:
        print(f"Non ci credo! {n} bambini!")