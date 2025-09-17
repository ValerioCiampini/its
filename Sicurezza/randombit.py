import sys
import random

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <filename>")

#1) Devo leggere tutti i file
data = None
with open(sys.argv[1], "rb") as f:
    data = f.read()

#2) Devo prendere un bit casuale di un byte
pos = random.randint(0, len(data)-1)

#3) prendo un bit casuale del byte
bit = random.randint(0, 7)

#cambio il valore del bit <bit> di data[pos] (xor)
#in sostanza devo sodtruire un byte di tutti 0 e un solo 1 nel posto giusto
byte = data[pos]
byte = byte ^ (1 << bit) #ho rovesciato il bit bit-esimo del byte

data = data[:pos] + bytes([byte]) + data[pos + 1:]
with open(sys.argv[1], "wb") as f:
    f.write(data)

print(f"modificato il bit {bit} al posto {pos} nel file {sys.argv[1]}")

