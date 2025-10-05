import time
import random

import pyttsx3
import bomb_modules
from edgework import Edgework

def speak(text, speed = 180):
    print(f"speaking \"{text}\"")
    engine = pyttsx3.init()
    engine.setProperty("rate", speed)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.01)


if __name__ == "__main__":
    edgework = Edgework()
    wantToExit = False
    speak("Do you want edgework?")
    response = input("y/n\n").lower()
    if response == "y":
        speak("you here")
        edgework.generateEdgework()
        edgework.getEdgework()

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
        input() #this is here so that you can wait for you to get your answer, mainly used when using the solver
