select codice, comp
from Volo
where durataMinuti > 180;

select comp
from Volo
where durataMinuti > 180;

select codice, comp
from ArrPart
where partenza = 'CIA';

select comp
from ArrPart
where arrivo = 'FCO';

select codice, comp
from ArrPart
where partenza = 'FCO' and arrivo = 'JFK';

select ArrPart.comp
from LuogoAeroporto as l1, ArrPart as ap, LuogoAeroporto as l2
where ap.partenza = l1.aeroporto and ap.arrivo = l2.aeroporto and l1.citta = 'Roma' and l2.citta = 'New York';

select Aeroporto.codice, Aeroporto.nome, LuogoAeroporto.citta
from LuogoAeroporto, Aeroporto, ArrPart
where ArrPart.comp = "MagicFly";

select Volo.codice, Volo.comp, ap.partenza, ap.arrivo
from ArrPart as ap, LuogoAeroporto as l1, LuogoAeroporto as l2, Volo as v, Aeroporto as a1, Aeroporto as a2
where l1.citta = 'Roma' and l2.citta = 'New York' and ap.partenza = a1.codice and ap.arrivo = a2.codice and a1.codice = l1.aeroporto and a2.codice = l2.aeroporto and v.codice = ap.codice and v.comp = ap.comp;

select distinct comp
from ArrPart as ap, Compagnia as c
where ap.partenza = 'FCO' and ap.arrivo = 'JFK' and c.annoFondaz <> null;
