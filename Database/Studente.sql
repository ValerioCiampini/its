create table studente(
    matricola integer not null,
    nome varchar(100) not null,
    cognome varchar(100) not null,
    nascita date, --può essere null
    cf char(16) not null,

    primary key(matricola),
    unique(cf),
    unique(cognome, nome, nascita)
);

create table corso(
    codice integer primary key, 
    nome varchar not null
);

create table Esame(
    studente integer not null,
    corso integer not null,
    voto integer not null
        check(voto >= 18 and voto <= 30),
    lode boolean not null,

    check (lode = false or voto = 30),
    primary key(studente, corso),
    foreign key(studente)
        references studente(matricola),
    foreign key (corso)
        references corso(codice)
);

insert into studente(matricola, nome, cognome, nascita, cf)
    values
(1, 'Alice', 'Bianchi', '09-08-2002', 'AAABBB02G09H501L');
