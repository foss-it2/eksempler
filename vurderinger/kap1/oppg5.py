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
hull = n-4

# a) Printer ut et kvadrat.
for i in range(n):
    rad = ""
    for j in range(n):
        rad += "#"
    print(rad)

print("*"*50)
# b) Printer ut et kvadrat med hull i.
for i in range(n):
    rad = ""
    if 1 < i < n-2:
        rad += "##"
        for j in range(hull):
            rad += " "
        rad += "##"
    else:
        for k in range(n):
            rad += "#"
    print(rad)