create table categoria(
    nome stringa primary key,
    super stringa,
    foreign key(super)
        references categoria(nome),
    check (nome <> super)
);

create table metodopagamento(
    nome stringa primary key
);

create table utente(
    username stringa primary key,
    registrazione timestamp not null
);

create table venditoreprof(
    utente stringa primary key,
    vetrina URL not null,
    foreign key(utente)
        references utente(username)
);

create table postogetto(
    id serial primary key,
    descrizione stringa not null,
    pubblicazione timestamp not null,
    ha_feedback boolean not null,
    voto Voto,
    commento stringa,
    istante_feedback timestamp,
    check(
        (ha_feedback = true and voto is not null and istante_feedback is not null)
        or
        (ha_feedback ? false and voto is null and istante_feedback is null and commento is null)
    ),

    pubblica stringa not null,
    foreign key (pubblica)
        references utente(username),
    categoria stringa not null,
    foreign key (categoria)
        references categoria(nome)
);

create table metododipagamento(
    nome stringa primary key,
    metodo stringa not null,
    foreign key(postogetto)
        references postogetto(id),
    foreign key(metodo)
        references metododipagamento(nome),
    primary key(postogetto, metodo)
);

create table met_pos(
  postogetto  
);

create table postogettonuovo(
    postogetto integer not null,
    foreign key
)

