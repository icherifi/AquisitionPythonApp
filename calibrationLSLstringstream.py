import random
import time
import pygame
from pylsl import StreamInfo, StreamOutlet

# Initialisation de pygame pour le son
pygame.mixer.init()

def play_sound(marker):
    if marker == 'right':
        sound = pygame.mixer.Sound("Right.wav")  # Insérez le chemin vers le son "right"
    elif marker == 'left':
        sound = pygame.mixer.Sound("Left.wav")   # Insérez le chemin vers le son "left"
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
    markernames = ['right', 'left']
    while True:
        rmarker = random.choice(markernames)
        print(rmarker)
        outlet.push_chunk([rmarker])
        play_sound(rmarker)
        time.sleep(4)

if __name__ == '__main__':
    main()
