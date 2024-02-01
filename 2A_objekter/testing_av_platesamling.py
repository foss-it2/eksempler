from Platesamling import * # importer alt er det * betyr.

fatOfTheLand = CD("Prodigy","Fat of the land",1997)
sam = CD("Metallica", "Symphony and Metallica",1999,True)

samling = Platesamling("Henrik",[fatOfTheLand,sam])
samling.visAlbum()
print("")

home = Vinyl("Mhoo", "Home is where you are", 2013, 12)
samling.leggTilAlbum(home)
samling.visAlbum()
print("")

samling.visArtister()