from pylab import *

# Informasjon om konstanter, krefter og gjenstanden
m = 4.8e6   # massen av gjenstanden, kg
g = 9.81  # tyngdeakselerasjon, m/s^2
F_motor = 75.9e6    # Kraft til rakettmotorene

sum_F = F_motor - m*g  # kraftsum, N
a = sum_F/m  # akselerasjon, m/s^2

# Startverdier for bevegelsen
s = 0  # startposisjon, m
v = 0  # startfart, m/s
t = 0  # starttid, s

# Simuleringsteknisk
t_slutt = 10     # sluttid for simulering, s
dt = 0.01        # lengde på tidssteg, s
s_verdier = [s]  # liste for lagring av posisjon
v_verdier = [v]  # liste for lagring av fart
t_verdier = [t]  # liste for lagring av tid

# Løkke som beregner ny fart, posisjon og tid
while v <= 1000/3.6:  # så lenge farten er mindre enn 500 km/h.
    v = v + a*dt      # regner ut ny v og overskriver gammel
    s = s + v*dt      # regner ut ny s og overskriver gammel
    t = t + dt        # regner ut ny t og overskriver gammel

    t_verdier.append(t)  # legger til ny t-verdi i listen for t
    v_verdier.append(v)  # legger til ny v-verdi i listen for v
    s_verdier.append(s)  # legger til ny s-verdi i listen for s


print(f"tiden opp til {s:.2f} m er {t:.2f} sekunder. Farten er da {v:.2f} m/s, eller {v*3.6:.2f} km/h.")

# Tegning av graf
plot(t_verdier, s_verdier)              # lager grafen
title("Strekning som funksjon av tid")  # tittel på grafen
xlabel("$t$ / s")                       # x-akse-tittel
ylabel("$s$ / m")                       # y-akse-tittel
grid()                                  # viser rutenett
#show()                                  # viser grafen