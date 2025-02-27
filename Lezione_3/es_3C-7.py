lancio_moneta = 1
croce = 0
testa = 0

while lancio_moneta <= 8:
    print(f'lancio mumero {lancio_moneta}')
    risultato_lancio = input('Inserire risultato lancio moneta con T o C (t / c utlizziabili): ')
    lancio_moneta += 1
    match risultato_lancio:
        case 'T' | 't':
            testa += 1
        case 'C' | 'c':
            croce += 1

print(f'In otto lanci croce è uscito {croce} volte, con una percentuale di {((croce/8) * 100):.2f}%')
print(f'In otto lanci croce è uscito {testa} volte, con una percentuale di {((testa/8) * 100):.2f}%')