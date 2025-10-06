--Quanti sono gli strutturati di ogni fascia?

select posizione, count(posizione)
from Persona
group by posizione;

--Quanti sono gli strutturati con stipendio ≥ 40000?
select count(posizione)
from Persona
where stipendio >= 40000;

--Quanti sono i progetti già finiti che superano il budget di 50000?
select count(*)
from Progetto
where budget > 50000 and fine < current_date;

--Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’ ?
select avg(oreDurata), max(oreDurata), min(oreDurata)
from Progetto as pr, AttivitaProgetto as ap
where pr.id = ap.progetto and pr.nome = 'Pegasus';

--Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto ‘Pegasus’ da ogni singolo docente?
select avg(oreDurata), max(oreDurata), min(oreDurata)
from Progetto as pr, AttivitaProgetto as ap, Persona as p
where pr.id = ap.progetto and pr.nome = 'Pegasus' and p.id = ap.persona and (p.posizione = 'Professore Ordinario' or p.posizione = 'Professore Associato');

--Qual è il numero totale di ore dedicate alla didattica da ogni docente?
select sum(oreDurata)
from 