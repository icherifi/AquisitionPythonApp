import random
import time
import pygame
from pylsl import StreamInfo, StreamOutlet

# Initialisation de pygame pour le son
pygame.mixer.init()

def play_sound(marker):
    if marker == 'thumb':
        sound = pygame.mixer.Sound("thumb.wav")  # Insérez le chemin vers le son "thumb"
    elif marker == 'index':
        sound = pygame.mixer.Sound("index finger.wav")   # Insérez le chemin vers le son "index"
    elif marker == 'middle':
        sound = pygame.mixer.Sound("middle finger.wav")   # Insérez le chemin vers le son "middle"
    elif marker == 'ring':
        sound = pygame.mixer.Sound("ring finger.wav")   # Insérez le chemin vers le son "ring"
    elif marker == 'pinky':
        sound = pygame.mixer.Sound("little finger.wav")   # Insérez le chemin vers le son "pinky"
    else:
        return
    sound.play()

def main():
    # Création du flux LSL

    print("Début dans 10 secondes...")
    time.sleep(10)
    info = StreamInfo('MyMarkerStream', 'Markers', 1, 0, 'string')
    outlet = StreamOutlet(info)
    print("Envoi des marqueurs...")
    
    markernames = ['thumb', 'index', 'middle', 'ring', 'pinky']
    while True:
        rmarker = random.choice(markernames)
        print(rmarker)
        outlet.push_chunk([rmarker])
        play_sound(rmarker)
        time.sleep(10)

if __name__ == '__main__':
    main()
