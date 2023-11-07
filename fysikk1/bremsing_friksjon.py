from pylab import *

# Informasjon om konstanter, krefter og gjenstanden
m = 0.250  # massen av gjenstanden, kg
g = 9.81   # tyngdeakselerasjon, m/s^2
mu = 0.3   # friksjonstall
G = m*g    # gravitasjonskraft, N
N = G      # normalkraft, N
R = mu*N   # friksjonskraft, N

sum_F = -R   # kraftsum, N
a = sum_F/m  # akselerasjon, m/s^2

# Startverdier for bevegelsen
s = 0    # startposisjon, m
v = 2.3  # startfart, m/s
t = 0    # starttid, s

# Simuleringsteknisk
v_slutt = 0      # sluttfart for simulering, m/s
dt = 0.01        # lengde på tidssteg, s
s_verdier = [s]  # liste for lagring av posisjon
v_verdier = [v]  # liste for lagring av fart
t_verdier = [t]  # liste for lagring av tid

# Løkke som beregner ny fart, posisjon og tid
while v > v_slutt:  # så lenge farten er større v_slutt
  v = v + a*dt      # regner ut ny v og overskriver gammel
  s = s + v*dt      # regner ut ny s og overskriver gammel
  t = t + dt        # regner ut ny t og overskriver gammel

  t_verdier.append(t)  # legger til ny t-verdi i listen for t
  v_verdier.append(v)  # legger til ny v-verdi i listen for v
  s_verdier.append(s)  # legger til ny s-verdi i listen for s

# Tegning av graf
plot(t_verdier, s_verdier)              # lager grafen
title("Strekning som funksjon av tid")  # tittel på grafen
xlabel("$t$ / s")                       # x-akse-tittel
ylabel("$s$ / m")                       # y-akse-tittel
grid()                                  # viser rutenett
show()                                  # viser grafen