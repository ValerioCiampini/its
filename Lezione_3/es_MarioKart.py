n:int = int(input("inserisci la posizione: "))

'''if n == 1:
    print("1st")
elif n == 2:
    print("2nd")
elif n == 3:
    print("3rd")
else:
    print(f"{n}th")'''

match n:
    case 1:
        print(f"{n}st")
    case 2:
        print(f"{n}nd")
    case 3: 
        print(f"{n}rd")
    case _:
        print(f"{n}th")
