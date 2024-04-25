import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(-2, 2, 20)
yverdier = xverdier**5

plt.axhline(0, color="black", zorder=0)
plt.axvline(0, color="black", zorder=0)
plt.plot(xverdier, yverdier, color="coral", linestyle="dashed", zorder=1)
plt.scatter(xverdier, yverdier, color="skyblue", marker="D", zorder=2, label="Data 1")
plt.scatter(yverdier, xverdier, color="magenta", marker="h", zorder=2, label="Data 1")
"""
MARKERS

marker

symbol

description

"."

m00

point

","

m01

pixel

"o"

m02

circle

"v"

m03

triangle_down

"^"

m04

triangle_up

"<"

m05

triangle_left

">"

m06

triangle_right

"1"

m07

tri_down

"2"

m08

tri_up

"3"

m09

tri_left

"4"

m10

tri_right

"8"

m11

octagon

"s"

m12

square

"p"

m13

pentagon

"P"

m23

plus (filled)

"*"

m14

star

"h"

m15

hexagon1

"H"

m16

hexagon2

"+"

m17

plus

"x"

m18

x

"X"

m24

x (filled)

"D"

m19

diamond

"d"

m20

thin_diamond

"|"

m21

vline

"_"

m22

hline

"""
plt.grid(which="major") # "major, minor, both"

plt.minorticks_on() # Tick marks on


plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("$y$")
plt.legend(loc="lower right") # "upper/lower left/right"

plt.show()
