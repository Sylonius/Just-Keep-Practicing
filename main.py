from gtts import gTTS
import io
import pygame
import time

def speak(text, lang="en"):
    # create mp3 bytes in memory
    tts = gTTS(text, lang=lang)
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    # initialize pygame mixer (use default settings)
    # you can adjust frequency/size/channels/buffer if needed
    pygame.mixer.init()
    # Try to load from file-like object (namehint 'mp3' helps some builds)
    pygame.mixer.music.load(mp3_fp, "mp3")
    pygame.mixer.music.play()

    # wait until playback finishes
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


if __name__ == "__main__":
    speak("Hello! This is played with pygame without permanently saving a file.")
