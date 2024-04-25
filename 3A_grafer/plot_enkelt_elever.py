from matplotlib import pyplot as plt

xverdier = [1,2,3]
yverdier = [1,4,9]

yverdier2 = [16, -5, 7]

plt.scatter(xverdier,yverdier,marker="p",color="magenta",label="Mine data") # Plotter PUNKTENE
plt.scatter(xverdier,yverdier2,marker="+",color="black",label="Datasett 2") # Plotter PUNKTENE
plt.legend(loc="lower right") # Sier at vi vil vise legend med de ulike labels. "upper/lower"
plt.show()
