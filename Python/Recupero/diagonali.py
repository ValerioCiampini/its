def sum_primary_diagonal(mat:list[list]):
    somma:int = 0
    counter:int = 0
    for i in mat:
        somma += i[counter]
        counter += 1

    return somma

def sum_secondary_diagonal(mat:list[list]):
    somma:int = 0
    counter:int = 1
    for i in mat:
        somma += i[len(i) - counter]
        counter += 1

    return somma

print(sum_primary_diagonal([[1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16], [17, 18, 19, 20, 21]]))
print(sum_secondary_diagonal([[1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16], [17, 18, 19, 20, 21]]))