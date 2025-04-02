x:int = int(input("inserisci una coordinata x: "))
y:int = int(input("inserisci una coordinata y: "))
coordinate:tuple = (x, y)

match coordinate:
    case (0, 0):
        print(f"Il punto {coordinate} si trova nell'origine.")
    case (x, 0):
        print(f"Il punto {coordinate} si trova sull'asse X.")
    case (0, y):
        print(f"Il punto {coordinate} si trova sull'asse Y.")
    case coordinate if x > 0 and y > 0:
        print(f"Il punto {coordinate} si trova nel primo quadrante")
    case coordinate if x < 0 and y > 0:
        print(f"Il punto {coordinate} si trova nel secondo quadrante")
    case coordinate if x < 0 and y < 0:
        print(f"Il punto {coordinate} si trova nel terzo quadrante")
    case coordinate if x > 0 and y < 0:
        print(f"Il punto {coordinate} si trova nel quarto quadrante.")