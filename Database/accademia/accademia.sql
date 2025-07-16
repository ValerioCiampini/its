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
    check(value >= 0 and value <= 8);

create domain Denaro as real
    check(value >= 0);

create table Persona(
    id PosInteger not null,
    nome StringaM not null, 
    cognome StringaM not null,
    posizione Strutturato not null,
    stipendio Denaro not null,

    primary key(id)
);

create table Progetto(
    id PosInteger not null, 
    nome StringaM not null, 
    inizio date not null, 
    fine date not null,
    budget Denaro not null,

    primary key(id),
    check(inizio < fine)
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

insert into Progetto(id, nome, inizio, fine, budget)
    values
(3, 'Progetto 1', '2020/06/21', '2021/02/12');

insert into Progetto(id, nome, inizio, fine, budget)
    values
(4, 'Progetto 2', '2023/11/10', '2023/12/20');

insert into WP(progetto, id, nome, inizio, fine)
    values
(4, 5, 'WP 1', '2019/02/21', '2020/01/30');

insert into WP(progetto, id, nome, inizio, fine)
    values
(3, 6, 'WP 2', '2015/04/13', '2022/06/01');

insert into AttivitaProgetto(id, persona, progetto, wp, giorno, tipo, oreDurata)
    values
(7, 2, 4, 6, '2023/12/21', 'Altro', 5);

insert into AttivitaProgetto(id, persona, progetto, wp, giorno, tipo, oreDurata)
    values
(8, 1, 3, 5, '2020/10/30', 'Ricerca e Sviluppo', 3);

insert into AttivitaNonProgettuale(id, progetto, tipo, giorno, oreDurata)
    values
(9, 3, 'Missione', '2020/09/18', 3);

insert into AttivitaNonProgettuale(id, progetto, tipo, giorno, oreDurata)
    values
(10, 4, 'Altro', '2023/11/15', 6);

insert into Assenza(id, persona, tipo, giorno)
    values
(11, 1, 'Malattia', '2025/09/24');

insert into Assenza(id, persona, tipo, giorno)
    values
(12, 2, 'Maternita', '2025/08/11');