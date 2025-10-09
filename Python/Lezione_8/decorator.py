'''def cronometro(fun):
    def wrapper():
        import time
        start = time.time()
        fun()
        print(time.time() - start)
    
    return wrapper 

@cronometro
def prova():
    return "ciao"

def i():
    for j in [1, 3, 4, 5,6 ,7 ,8]:
        print(7)
prova = cronometro(prova)
prova()
ciclo = cronometro(i)
ciclo()'''

def saluti(fun):
    def wrapper():
        fun()
        print("Bene")

    return wrapper

@saluti
def ciao():
    print("Ciao, come stai?")

prova = saluti(ciao)
prova()

d:dict = {[1, 3]:[4, 5]}

if 1 not in d:
    pass