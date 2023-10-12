"""
Lag et program som tegner «kvadrater» ved hjelp av symbolet «#». Brukeren skal oppgi kvadratets sidelengde. Hvis brukeren for eksempel skriver 5, skal programmet tegne:
#####
#####
#####
#####
#####

#####
#####
## ##
#####
#####

#######
#######
##   ##
##   ##
##   ##
#######
#######

########
########
##    ##
##    ##
##    ##
##    ##
########
########

#########
#########
##     ##
##     ##
##     ##
##     ##
##     ##
#########
#########
"""

n = 8

# a) Printer ut et kvadrat.
for i in range(n):
    rad = ""
    for j in range(n):
        rad += "#"
    print(rad)

print("*"*50)
# b) Printer ut et kvadrat med hull i.
hull = n-4      # Hull er alltid mindre enn bredden til veggen (2x##)
for i in range(n):
    rad = ""
    # Hvis rad ikke er de to øverste eller de to nederste.
    if 1 < i < n-2:
        rad += "##"     # lager rammen til venstre.
        for j in range(hull):   # Fyller på med hull.
            rad += " "
        rad += "##"     # lager rammen til høyre.
    else:
        for k in range(n):  # Hvis raden er de to øverste eller de to nedrste.
            rad += "#"  # fyll på med hull for hele raden.
    print(rad)