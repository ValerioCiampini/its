create domain PosInteger as integer
    check(value >= 0);

create domain Stringa as varchar;

create domain StringaM as varchar(100);

create domain CAP as char(5);
    check(value ~ '[0-9]{5}')

create type Indirizzo as (
    via Stringa, 
    civico Stringa,
    cap CAP 
);

create domain RealGEZ as real
    check(value >= 0);

create domain RealBZO as real
    check(value >= 0 and value <= 1);

create domain CodiceFiscale as char(16);

create domain Telefono as char(20)
 check(value '[0-9]*10');

create domain Email as char(100)
    check(value ~ '%^[A-Za-z0-9._%\-+!#$&/=?^|~]+@[A-Za-z0-9.-]+[.][A-Za-z]+$%');

create domain Partita_iva as char(11)
    check(value ~ '^[0-9]{11}');

create type StatoOrdine as 
    enum('in preparazione', 'inviato', 'da saldare', 'saldato');

create table Direttore(
    nome Stringa not null,
    cognome Stringa not null,
    cf CodiceFiscale not null,
    anni_servizio PosInteger not null,
    data_nascita date not null,

    primary key(cf),
    unique(cf)
);

create table dipartimento (
	nome stringa primary key,
	indirizzo indirizzo not null
	citta integer not null,
    direttore Codice
    
	foreign key (citta) references citta(id),
    
);

create table Ordine(
    data_stipula date not null,
    imponibile RealGEZ not null,
    aliquota RealBZO not null,
    descrizione StringaM not null,
    id integer not null,

    primary key(id)
);

create table StatoOrdine(
    nome Stringa not null,

    primary key(nome)
);

create table Fornitore(
    ragione_sociale Stringa not null,
    partita_iva Partita_iva not null,
    indirizzo Indirizzo not null,
    telefono Telefono not null,
    email Email not null,

    primary key(partita_iva),
    unique(partita_iva)
);

create table nazione (
	nome stringa primary key
);

create table regione (
	nome stringa not null,
	nazione stringa not null,
	primary key (nome, nazione),
	foreign key (nazione) references nazione(nome)
);

create table citta (
	id integer primary key, 
	nome stringa not null,
	regione stringa not null,
	nazione stringa not null,
	unique (nome, regione, nazione),
	foreign key (regione, nazione)
		references regione(nome, nazione)
);

