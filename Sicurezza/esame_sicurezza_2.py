#Crittografia

#Problema 1
#Sia dato il messaggio cifrato (convertito in numero intero in base 10): 
#204751668535
#Il messaggio cifrato è stato ottenuto cifrando il messaggio originale con algoritmo RSA senza padding con n=514948966453 e esponente pubblico (e) pari a 3
#Provare a decifrare il messaggio cifrato
#NB: il messaggio originale è una parola di cinque lettere maiuscole e minuscole.
#NB: Quando il problema sembra arduo, allora un approccio brutale potrebbe essere quello vincente.

C = 204751668535
n = 514948966453
e = 3

x = False

for p1 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":  #utilizzo brute force per cercare ogni corrispondenza(ci mette un pò a trovare la soluzione)
    if x == True:
        break
    for p2 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if x == True:
            break
        for p3 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if x == True:
                break
            for p4 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if x == True:
                    break
                for p5 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    if x == True:
                        break
                    messaggio = p1 + p2 + p3 + p4 + p5 #unisco ogni lettera per poter formare il messaggio
                    messaggio = int(messaggio.encode('utf-8').hex(), 16) #converto il messaggio
                    if pow(messaggio, e, n) == C:
                        print(f"il messaggio decifrato è: {messaggio}")
                        x = True
                        break

#Problema 2
#Premessa: nell'RSA, per calcolare con python l'esponente privato nota la chave pubblica e noti i due numeri primi p e q, si utilizza la sequente funzione
#d = inverse(e, phi) dove ph = (p-1)*(q-1).

#Sia dato n (pari a p*q) = 51151902024533551
#e siano
#e (esponente pubblico) = 3
#C=10002041662569686 il messaggio cifrato (l'originale è una parola di sette caratteri alfanumerici)
#Decifrare il messaggio
#NB: un attacco forza bruta su 7 caratteri ha un costo computazionale pari a 62^6 = 56.800.235.584 (infattibile in python)
#NB: ma n=p*q e quindi se riuscissi a trovare i due numeri primi che fattorizzano n, allora potrei applicare euclide inverso (la funzione inverse) per trovare la chiave privata...

'''from Crypto.Util.number import inverse 

n = 51151902024533551
e = 3
C = 10002041662569686

i = 2
while i < n: #ciclo per calcolare p e q
    p = n / i
    if i * p == n:
        q = i
        break
    i += 1

print(p, q)

phi = (p-1)*(q-1) #formula per calcolare phi

d = inverse(e, phi) #formula per calcolare l'esponente privato

messaggio = pow(C, d, n)

length = (messaggio.bit_length() + 7) // 8      #operazioni per convertire il messaggio in testo lagibile
msg_bytes = messaggio.to_bytes(length, "big")
messaggio_decriptato = msg_bytes.decode("utf-8")
print(messaggio_decriptato)
'''

