select WP.nome, WP.inizio, WP.fine
from WP, Progetto
where Progetto.nome = 'Pegasus' and Progetto.id = WP.progetto;

select distinct p.nome, p.cognome, p.posizione
from Persona as p, Progetto as pr, AttivitaProgetto as a
where a.persona = p.id and a.progetto = pr.id and pr.nome = 'Pegasus'
order by cognome desc;

select distinct p.nome, p.cognome, p.posizione
from Persona as p, Progetto as pr, AttivitaProgetto as a
where a.persona = p.id and a.progetto = pr.id and pr.nome = 'Pegasus' and a.giorno;

select distinct p.nome, p.cognome 
from Persona as p, Assenza as a
where p.posizione = 'Professore Ordinario' and p.id = a.persona and a.tipo = 'Malattia';

select distinct p.nome, p.cognome 
from Persona as p, Assenza as a
where p.posizione = 'Professore Ordinario' and p.id = a.persona and a.tipo = 'Malattia';

select distinct p.nome, p.cognome
from Persona as p, LavoroNonProgettuale as l
where p.posizione = 'Ricercatore' and p.id = l.persona and l.tipo = 'Didattica';


