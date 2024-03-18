import random
import time
import pygame
from pylsl import StreamInfo, StreamOutlet
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--sound", action="store_true", help="Play sound if specified")
parser.add_argument("--duration", type=float, help="Duration of each marker (in seconds)")
parser.add_argument("--stream", type=str, help="Name of the LSL stream")
args = parser.parse_args()

# Initialize pygame for sound
pygame.mixer.init()

def play_sound(marker):
    if marker == 'right':
        sound = pygame.mixer.Sound("Right.wav")  # Insert the path to the "right" sound
    elif marker == 'left':
        sound = pygame.mixer.Sound("Left.wav")   # Insert the path to the "left" sound
    else:
        return
    sound.play()

def main():
    # Création du flux LSL
    print("Début dans 10 secondes...")
    time.sleep(10)
    info = StreamInfo(args.stream , 'Markers', 1, 0, 'string')
    outlet = StreamOutlet(info)
    print("Envoi des marqueurs...")
    markernames = ['right', 'left']
    while True:
        rmarker = random.choice(markernames)
        print(rmarker)
        outlet.push_chunk([rmarker])
        if args.sound :
            play_sound(rmarker)
        time.sleep(args.duration)

if __name__ == '__main__':
    main()
