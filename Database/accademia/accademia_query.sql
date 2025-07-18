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
from Persona as p, Assenza as a1, Assenza as a2
where p.posizione = 'Professore Ordinario' and p.id = a1.persona and a.tipo = 'Malattia';

-- 5
select distinct p.nome, p.cognome 
from Persona as p, Assenza as a
where p.posizione = 'Professore Ordinario' and p.id = a1.persona and a1.tipo = 'Malattia' and a2.tipo = 'Malattia' and p.id = a2.persona;

-- 6
select distinct p.nome, p.cognome
from Persona as p, LavoroNonProgettuale as l
where p.posizione = 'Ricercatore' and p.id = l.persona and l.tipo = 'Didattica';

-- 7
select distinct p.nome, p.cognome
from Persona as p, AttivitaNonProgettuale as a1, AttivitaNonProgettuale as a2
where p.posizione = 'Ricercatore' and p.id = a1.persona and a1.tipo = 'Didattica' and p.id = a2.persona and a2.tipo = 'Didattica';

-- 8
select distinct p.nome, p.cognome
from Persona as p, AttivitaProgetto as a, AttivitaNonProgettuale as an
where p.id = a.persona and p.id = an.persona and a.giorno = an.giorno;

-- 9
select distinct p.nome, p.cognome, a.giorno, pr.nome, an.tipo, a.oreDurata, an.oreDurata
from Persona as p, AttivitaProgetto as a, AttivitaNonProgettuale as an, Progetto as pr
where p.id = a.persona and p.id = an.persona and a.giorno = an.giorno and pr.id = a.progetto;

-- 10
select distinct p.nome, p.cognome
from Persona as p, AttivitaProgetto as ap, Assenza as a
where p.id = a.persona and p.id = ap.persona and a.giorno = ap.giorno;

-- 11
select distinct p.nome, p.cognome, a.giorno, pr.nome, a.tipo, ap.oreDurata
from Persona as p, AttivitaProgetto as ap, Assenza as a, Progetto as pr
where p.id = a.persona and p.id = ap.persona and a.giorno = ap.giorno and pr.id = a.progetto;

-- 12
select distinct wp1.nome
from WP as wp1, Progetto as pr1, WP as wp2, Progetto as pr2
where wp1.nome = wp2.nome and pr1.id <> pr2.id and pr1.id = wp1.progetto and pr2.id = wp2.progetto;


