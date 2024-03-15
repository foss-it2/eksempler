import tkinter as tk
import random
import time
# Lager et vindu i tkinter
window = tk.Tk()
window.title("Dino Game")
windowWidth = 600
windowHeight = 400
window.minsize(windowWidth, windowHeight) # Geometrien til vinduet
# Lager et tegnebrett til animering av Chrome Dino spillet (se på det som en skjerm)
canvas = tk.Canvas(window, width=windowWidth, height=windowHeight, bg="white")
canvas.pack()
# Tegner bakken
bakke_høyde = 380
canvas.create_line(0, bakke_høyde, windowWidth, bakke_høyde, width=5)

# Status for om spillet kjører 
game_running = True

# Dino class for animasjon av dinosauren (en kloss)
class Dino:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 30
        self.y = bakke_høyde
        self.høyde = 30
        # Oppretter dinoen som et rektangel på lerretet
        self.dino_id = canvas.create_rectangle(self.x - 20, self.y - self.høyde, self.x + 20, self.y, fill="blue")
        self.hopper = False
        self.dukker = False
    
    # Funksjon for å definere og animere hopp
    def hopp(self):
        # Hindrer hopp og dukk samtidig
        if self.hopper or self.dukker:
            return
        self.hopper = True
        self.hopp_max = bakke_høyde - 150  # Justert for konsistent høyde på hopp
        self.start_y = self.y
        self.hopp_fart = -13  # Negativ for å flytte opp

        def animer_hopp():
            # Logikk for å animere hoppet
            if self.hopper:
                # Flytter Dino oppover så lenge den har negativ hastighet og er under maks høyde
                if self.hopp_fart < 0 and self.y > self.hopp_max:
                    self.y += self.hopp_fart
                elif self.hopp_fart > 0 and self.y < self.start_y:
                    self.y += self.hopp_fart
                else:
                    self.hopp_fart = -self.hopp_fart  # Endrer retning

                if self.y >= self.start_y:
                    self.y = self.start_y
                    self.hopper = False

                canvas.coords(self.dino_id, self.x - 20, self.y - self.høyde, self.x + 20, self.y)
                if self.hopper:
                    window.after(20, animer_hopp)
        animer_hopp()

    # Funksjon for å endre parametere for Dino ved dukking
    def dukk(self, start=True):
        # Hindrer dukking under hopp
        if self.hopper:
            return
        if start:
            self.dukker = True
            self.høyde = 20  # Reduserer høyden ved dukking
            # Justerer for synlighet ved dukking gjør også dino litt bredere :) 
            canvas.coords(self.dino_id, self.x - 30, self.y, self.x + 30, self.y - self.høyde) 
        else:
            self.dukker = False
            self.høyde = 30  # Tilbakestiller høyden og bredden
            canvas.coords(self.dino_id, self.x - 20, self.y - self.høyde, self.x + 20, self.y)

# Klasse for å lage hindringer som Dino må unngå
class Hindring:
    def __init__(self, canvas, y_offset=0):
        self.canvas = canvas
        self.x = windowWidth
        self.y_offset = y_offset # Hvor langt hindrene skal flyttes opp
        self.y = bakke_høyde - 20 - self.y_offset # Endrer høyden på hindringene basert på offset
        # Oppretter hindringen som et rektangel på lerretet
        self.hindring_id = canvas.create_rectangle(self.x, self.y, self.x + 20, bakke_høyde - self.y_offset, fill="red")

    def move(self):
        # Beveger hindringen mot venstre hvis spillet kjører
        if game_running:
            self.x -= 20
            # Beveger hindringene med canvas.move()
            canvas.move(self.hindring_id, -20, 0)
dino = Dino(canvas)

# Lager en funksjon for å spawne hindringer
hindringer = []
def spawn_hindring():
    # Genererer hindringer med varierende høyde for å kreve dukking for noen
    if game_running:
        y_offset = random.choice([5, 8, 9, 12, 15, 30])  # Y-offset betyr høyere hindringer, krever dukking - kan fortsatt dukke ved offset >=10 pga. dukk høyde
        hindring = Hindring(canvas, y_offset)
        hindringer.append(hindring)
        window.after(random.choice([500, 700, 1000, 1200, 1500]), spawn_hindring)

# Flytter hindringene så lenge spillet kjører
def game_loop():
    if game_running:
        for hindring in hindringer:
            hindring.move()
            if kollisjonssjekk(dino, hindring):
                game_over()
                return
        # Venter 50 ms før neste hinder kjører
        window.after(50, game_loop)

# Funksjon for å sjekke kollisjon mellom dino og hinder
# Leter etter samtidig overlapp mellom x og y koordinater
def kollisjonssjekk(dino, hindring):
    # Henter koordinatene til objektene
    dino_coords = canvas.coords(dino.dino_id)
    hindring_coords = canvas.coords(hindring.hindring_id)

    # Sjekker om dinoen dukker. Justerer dinoens effektive kollisjonsgrenser til å være lavere
    if dino.dukker:
        adjusted_dino_top = dino_coords[1] + 10  # Flytter toppen ned
    else:
        adjusted_dino_top = dino_coords[1]

    # Kollisjonssjekk vurderer den justerte toppen for dukking
    overlapp_i_x = dino_coords[2] >= hindring_coords[0] and dino_coords[0] <= hindring_coords[2]
    overlapp_i_y = adjusted_dino_top < hindring_coords[3] and dino_coords[3] > hindring_coords[1]

    if overlapp_i_x and overlapp_i_y:
        return True
    return False

# Lager en "game over" funksjon for å avslutte spillet ved kollisjon
def game_over():
    global game_running
    game_running = False
    # Gir poeng etter brukt tid
    elapsed_time = round(time.time() - start_time, 4)
    # Viser spill over-tekst og poengsum
    canvas.create_text(windowWidth / 2, windowHeight / 2 - 20, text="GAME OVER", font=('Arial', 30), fill="red")
    canvas.create_text(windowWidth / 2, windowHeight / 2 + 20, text=f"Score: {elapsed_time} seconds", font=('Arial', 20), fill="green")

# Definerer hendelser for trykk på knapper
def on_up_key(event):
    if game_running:
        dino.hopp()
def on_down_key(event):
    if game_running:
        dino.dukk(start=True)
def on_down_key_release(event):
    if game_running:
        dino.dukk(start=False)
def avslutt(event):
    window.destroy()

# Binder taster til deres respektive funksjoner
window.bind("<Up>", on_up_key)
window.bind("<Down>", on_down_key)
window.bind("<KeyRelease-Down>", on_down_key_release)
window.bind("<Escape>", avslutt)

#Vi er klare til å kjøre programmet
# Starter tiden når programmet kjører
start_time = time.time()
spawn_hindring()
game_loop()

window.mainloop()
