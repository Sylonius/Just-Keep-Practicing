import string
import time
import random

import pyttsx3
import bomb_modules
from edgework import Edgework

def speak(text, speed = 180, convertToNatoPhonetic = True):
    natoPhoneticDict = {
        "A":"alpha",
        "B":"bravo",
        "C": "charlie",
        "D": "delta",
        "E": "echo",
        "F": "foxtrot",
        "G": "golf",
        "H": "hotel",
        "I": "india",
        "J": "juliett",
        "K": "kilo",
        "L": "lima",
        "M": "mike",
        "N": "november",
        "O": "oscar",
        "P": "papa",
        "Q": "quebec",
        "R": "romeo",
        "S": "sierra",
        "T": "tango",
        "U": "uniform",
        "V": "victor",
        "W": "whiskey",
        "X": "xray",
        "Y": "yankee",
        "Z": "zulu",

    }
    tempText = ""
    if convertToNatoPhonetic:
        for charIndex in range(len(text)):
            if text[charIndex] in natoPhoneticDict and charIndex != 0 and not (text[charIndex-1] == " " and text[charIndex-2] == "."):
                tempText += natoPhoneticDict.get(text[charIndex])
                if text[charIndex+1] not in [" ", ".", ","]:
                    tempText += " "
            else:
                tempText += text[charIndex]
            if tempText[-1] in string.digits and text[charIndex+1] not in [" ", ".", ","] and text[charIndex+1] not in string.digits:
                tempText += " "
    text = tempText
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
    # if they put anything but "y" it is the same as saying no
    if response == "y":
        edgework.generateEdgework()
        speak(edgework.sayableEdgework(),150)
    while not wantToExit:
        toRun = input("Module to Run: ")
        if toRun.lower() in ["exit", "leave", "bye", "quit", "hasta la vista, baby"]:
            wantToExit = True
            if random.randint(1,50) == 1:
                with open("DontLook", 'r', encoding='utf-8') as file:
                    speak(file.read(), 300)
            else:
                speak("Bye bye")
        else:
            toSpeak = bomb_modules.get_bomb_module(toRun)
            speak(toSpeak)
        input("Press enter to continue.") #this is here so that you can wait for you to get your answer, mainly used when using the solver
