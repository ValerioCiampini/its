utente:dict = {"nome":str(input("inserisci il nome: ")), "ruolo":str(input("inserisci il suo ruolo: ")), "età":int(input("inserisci la sua età: "))}

match utente:
    case utente if utente["ruolo"] == "admin":
        print("Accesso completo a tutte le funzionalità.")
    case utente if utente["ruolo"] == "moderatore":
        print("Può gestire i contenuti ma non modificare le impostazioni.")
    case utente if utente["età"] >= 18 and utente["ruolo"] == "utente":
        print("Accesso standard a tutti i servizi.")
    case utente if utente["età"] <= 18 and utente["ruolo"] == "utente":
        print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case utente if utente["ruolo"] == "ospite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")

