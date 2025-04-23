from music import *


def main():
    guitar = Guitar()
    print(f'guitar: {guitar.play()}')
    violin = Violin()
    print(f'violin: {violin.play()}')
    drum = Drum()
    print(f'drum: {drum.play()}')
    music_instrument = MusicInstrument()
    print(f'musicinstrument: {music_instrument.play()}')
main()