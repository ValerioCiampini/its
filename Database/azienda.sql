create domain RealGEZ as real
    check(value >= 0);

create domain Stringa as varchar;

create type Indirizzo as (
    via Stringa, 
    civico Stringa
);

create table Impiegato(
    nome Stringa not null,
    cognome Stringa not null,
    nascita date not null,
    stipendio RealGEZ not null,
    id integer not null,

    primary key(id),
    unique(id)
);

create table dipartimento(
    nome Stringa not null,
    indirizzo Indirizzo,
    id integer not null,

    primary key(id),
    unique(id)
);

create table progetto(
    nome Stringa not null,
    budget RealGEZ not null,
    id integer not null,

    primary key(id),
    unique(id)
);

create table numerotelefono(

);