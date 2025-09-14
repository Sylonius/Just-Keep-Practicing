import time
import io
from gtts import gTTS
import pygame
import bomb_modules


def speak(text):
    print(f"speaking \"{text}\"")
    # create mp3 bytes in memory
    tts = gTTS(text, lang="en")
    mp3Fp = io.BytesIO()
    tts.write_to_fp(mp3Fp)
    mp3Fp.seek(0)

    # initialize pygame mixer (use default settings)
    # you can adjust frequency/size/channels/buffer if needed
    pygame.mixer.init()
    # Try to load from file-like object (namehint 'mp3' helps some builds)
    pygame.mixer.music.load(mp3Fp, "mp3")
    pygame.mixer.music.play()

    # wait until playback finishes
    while pygame.mixer.music.get_busy():
        time.sleep(0.01)


if __name__ == "__main__":
    toRun = input("Module to Run: ")
    toSpeak = bomb_modules.get_bomb_module(toRun)
    speak(toSpeak)
