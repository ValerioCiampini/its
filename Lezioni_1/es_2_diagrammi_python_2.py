nord_sud:int = int(input("inserisci numero di veicoli a nord e sud: "))
est_ovest:int = int(input("inserisci numero di veicoli a est e ovest: "))
soglia:int = 70
time_ns:int = 0
time_eo:int = 0

if nord_sud > soglia and est_ovest > soglia:
    time_ns = 50
    time_eo = 50
elif nord_sud > soglia:
    time_ns = 60
    time_eo = 40
elif est_ovest > soglia:
    time_ns = 40
    time_ns = 60
else:
    time_ns = (nord_sud / (nord_sud + est_ovest)) * 100
    time_eo = (est_ovest / (nord_sud + est_ovest)) * 100

print(f"il tempo assegnato alla direzione nord sud è {(time_ns):.2f}")
print(f"il tempo assegnato alla direzione est ovest è {(time_eo):.2f}")