create type Strutturato as 
    enum('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type LavoroProgetto as 
    enum('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');

create type LavoroNonProgettuale as
    enum('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');

create type CausaAssenza as 
    enum('Chiusura Universitaria', 'Maternita', 'Malattia');

create domain PosInteger as integer
    check(value >= 0);

create domain StringaM as varchar(100);

create domain NumeroOre as integer
    check(value >= 0 and value <= 8)

create domain Denaro as real
    check(value >= 0);

create table Persona(
    id PosInteger not null,
    nome StringaM not null, 
    cognome StringaM not null,
    posizione Strutturatonot null,
    stipendio Denaronot null,

    primary key(id)
);

create table Progetto(
    id PosInteger not null, 
    nome StringaM not null, 
    inizio date not null, 
    fine date not null,
    budget Denaro not null,

    primary key(id)
);

create table WP(
    progetto PosInteger not null,
    id PosInteger not null, 
    nome StringaM not null, 
    inizio date not null,
    fine date not null,

    primary key(progetto, id),
    check(inizio < fine),
    unique(progetto, nome),
    foreign key(progetto)
        references Progetto(id)
);

create table AttivitaProgetto (
    id PosInteger not null, 
    persona PosInteger not null, 
    progetto PosInteger not null,
    wp PosInteger not null, 
    giorno date not null, 
    tipo LavoroProgetto not null, 
    oreDurata NumeroOre not null,

    primary key(id),
    foreign key(persona)
        references Persona(id),
    foreign key(progetto, wp)
        references WP(progetto, id)
    );

create table AttivitaNonProgettuale (
    id PosInteger not null, 
    persona PosInteger not null, 
    tipo LavoroNonProgettuale not null, 
    giorno date not null, 
    oreDurata NumeroOre not null,
    
    primary key(id),
    foreign key(persona)
        references Persona(id)
    );

create table Assenza (
    id PosInteger not null, 
    persona PosInteger not null, 
    tipo CausaAssenza not null, 
    giorno date not null,
    
    primary key(id),
    unique(persona, giorno),
    foreign key(persona)
        references Persona(id)
    );

insert into Persona(id, nome, cognome, posizione, stipendio)
    values
(1, 'Marco', 'Bianchi', 'Ricercatore', 1500);


insert into Persona(id, nome, cognome, posizione, stipendio)
    values
(2, 'Alice', 'Rossi', 'Professore Ordinario', 2000);
