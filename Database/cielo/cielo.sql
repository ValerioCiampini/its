create domain PosInteger as integer
    check(value >= 0);

create domain StringaM as varchar(100);

create domain CodIATA as char(3);

create table Compagnia(
    nome StringaM not null, 
    annoFondaz PosInteger,
    
    primary key(nome)
    );

create table Volo(
    codice PosInteger not null, 
    comp StringaM not null, 
    durataMinuti PosInteger not null,
    
    primary key(codice, comp),
    foreign key(comp) 
        references Compagnia(nome)
    );

create table Aeroporto(
    codice CodIATA not null, 
    nome StringaM not null,
    
    primary key(codice),
    );

create table LuogoAeroporto(
    aeroporto CodIATA not null, 
    citta StringaM not null, 
    nazione StringaM not null,
    
    primary key(aeroporto),
    foreign key(aeroporto) 
        references Aeroporto(codice) on delete cascade deferrable
    );

create table ArrPart(
    codice PosInteger not null, 
    comp StringaM not null, 
    arrivo CodIATA not null, 
    partenza CodIATA not null,
    
    primary key(codice, comp),
    foreign key(codice, comp) 
        references Volo(codice, comp) deferrable,
    foreign key(arrivo) 
        references Aeroporto(codice),
    foreign key(partenza) 
        references Aeroporto(codice)
    );

alter table Volo
    add constraint volo_arrpart_fk
    foreign key(codice, comp) 
        references ArrPart(codice, comp) deferrable;

alter table Aeroporto
    add constraint aeroporto_luogoaeroporto_fk
    foreign key(codice) 
        references LuogoAeroporto(aeroporto) on delete cascade deferrable;

begin transaction;
set costrains all deferred;

insert into Aeroporto(codice, nome) 
values 
('FCO', 'Aeroporto Leonardo Da Vinci'),
('MXP', 'Aeroporto di Milano Malpensa');

insert into LuogoAeroporto(aeroporto, citta, nazione) 
values 
('FCO', 'Roma', 'Italia'),
('MXP', 'Milano', 'Italia');

insert into Compagnia(nome, annoFondaz)
values
('WizardAir', 2006),
('Apitalia', 1987);

insert into Volo(codice, comp, durataMinuti)
values
(101, 'WizardAir', 55),
(102, 'Apitalia', 45);

insert into ArrPart(codice, comp, partenza, arrivo)
values
(101, 'WizardAir', 'FCO', 'MXP'),
(102, 'Apitalia', 'MXP', 'FCO');

commit;