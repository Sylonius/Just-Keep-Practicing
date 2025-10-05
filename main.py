import time
import io
import random

from gtts import gTTS
import pyttsx3
import pygame
import bomb_modules


def speak(text, speed = 180):
    print(f"speaking \"{text}\"")
    engine = pyttsx3.init()
    engine.setProperty("rate", speed)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.01)


if __name__ == "__main__":
    wantToExit = False
    while not wantToExit:
        toRun = input("Module to Run: ")
        if toRun.lower() in ["exit", "leave", "bye", "quit", "hasta la vista, baby"]:
            wantToExit = True
            if random.randint(1,2) == 1:
                with open("DontLook", 'r', encoding='utf-8') as file:
                    speak(file.read(), 300)
            else:
                speak("Bye bye")
        else:
            toSpeak = bomb_modules.get_bomb_module(toRun)
            speak(toSpeak)
