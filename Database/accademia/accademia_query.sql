-- 1
select WP.nome, WP.inizio, WP.fine
from WP, Progetto
where Progetto.nome = 'Pegasus' and Progetto.id = WP.progetto;

-- 2
select distinct p.nome, p.cognome, p.posizione
from Persona as p, Progetto as pr, AttivitaProgetto as a
where a.persona = p.id and a.progetto = pr.id and pr.nome = 'Pegasus'
order by cognome desc;

-- 3
select distinct p.nome, p.cognome, p.posizione
from Persona as p, Progetto as pr, AttivitaProgetto as a1, AttivitaProgetto as a2
where pr.id = a2.progetto and a1.persona = p.id and a2.persona = p.id and a1.progetto = pr.id and a1.id <> a2.id;

-- 4
select distinct p.nome, p.cognome 
from Persona as p, Assenza as a
where p.posizione = 'Professore Ordinario' and p.id = a.persona and a.tipo = 'Malattia';

-- 5
select distinct p.nome, p.cognome 
from Persona as p, Assenza as a
where p.posizione = 'Professore Ordinario' and p.id = a.persona and a.tipo = 'Malattia';

-- 6
select distinct p.nome, p.cognome
from Persona as p, LavoroNonProgettuale as l
where p.posizione = 'Ricercatore' and p.id = l.persona and l.tipo = 'Didattica';

-- 7


-- 8
select distinct p.nome, p.cognome
from Persona as p, AttivitaProgetto as a, AttivitaNonProgettuale as an
where p.id = a.persona and p.id = an.persona and a.giorno = an.giorno;

