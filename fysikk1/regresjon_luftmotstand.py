import matplotlib.pyplot as plt 
import scipy.optimize as opt 
import numpy as np

"""
   Regresjon av data.

   I dette eksempelet brukes Newtons avkjølingslov som har denne modellen for temperatur:
   F = 0.5 * rho * v^2 * C_d * A
   der rho er tettheten til luften,
   v er terminal velocity,
   C_d er lutmotstandskoeffisienten,
   A er frontarealet til muffinsformen.

   Ved terminal velocity er summen av krefter lik null:
   F (luftmotstanden) og G (tyngden) er lik hverandre.
   mg = 0.5 * rho * v^2 * C_d * A.

   Finner farten som funksjon av massen
   v^2 = m * 2*g/(rho * C_d * A)

   Lenke til Wikipedia-artikkel: https://en.wikipedia.org/wiki/Drag_(physics)

   Data er hentet herfra:
   https://www.coursehero.com/file/46425074/Cupcake-Cases-Dropping-Physics-2017docx/
"""

fart = [
    1.47,
    3.03,
    3.28,
    4.17,
    5.41
]
# masse i gram for 1, 5, 9, 17, 20 muffinsformer
masse = [
    0.43,
    2.15,
    3.87,
    7.31,
    8.60
]
masse = [x/1000 for x in masse] # Gjør om fra g til kg.

print(masse)

g = 9.81
rho = 1.293 # kg / m^3
A = np.pi * 0.025**2

# Tegner datapunktene som viser temperaturen
#plt.plot(masse,fart,"bx", label="Falltid")
#plt.show()

# Modellen vi bruker for terminal velocity fra innledningen øverst.
def terminal_velocity(m,C_d): 
    return  np.sqrt( m * 2*g/(rho * C_d * A) )

popt, pcov = opt.curve_fit(terminal_velocity, masse, fart)  # Her kjører regresjonen. Parametre er funksjonens navn, x-verdier, y-verdier.
print(popt[0])  # C_d = omgivelsestemperaturen


# Lager regresjonsplot med data fra regresjonsanalysen
x = []
y = []
xverdi = masse[0]
delta_x = 1/10000
C_d = popt[0]
for i in range(90):
    x.append(xverdi)
    y.append(terminal_velocity(xverdi,C_d))
    xverdi += delta_x

plt.plot(x,y,"-r", label=f"Teoretisk Cd={C_d:.2f}")
plt.plot(masse, fart,"bx", label="v_terminal")
plt.legend(loc="lower right")   # Legger merkelapp-vindu øverst til høyre
plt.show()