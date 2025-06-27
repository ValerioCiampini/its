def tariffa_oraria(macchina:int):
    tariffa:float = 2
    ore = int(input("inserisci numero ore di presenza macchina nel parcheggio: "))
    i:int = 0
    parcheggio:list = [macchina, ore, tariffa]

    if ore <= 3:
        parcheggio[2] = tariffa
    elif ore == 24:
        tariffa = 10
        parcheggio[2] = tariffa
    else:
        while i <= ore:
            if tariffa == 10:
                break

            tariffa += 0.5
            parcheggio[2] = tariffa
            i += 1
            
    return parcheggio

mat:list[list] = []
c1 = tariffa_oraria(1)
c2 = tariffa_oraria(2)
c3 = tariffa_oraria(3)
c4 = tariffa_oraria(4)

mat.append(["Car", "Hours", "Charge"])
mat.append(c1)
mat.append(c2)
mat.append(c3)
mat.append(c4)
mat.append(["Total", c1[1] + c2[1] + c3[1] + c4[1], c1[2] + c2[2] + c3[2] + c4[2]])

for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(f"{mat[i][j]:<10}", end="")
    print("\n")








    