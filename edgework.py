import random
import string
from enum import StrEnum

class Edgework():
    def __init__(self):
        self.serial = ""
        self.batteries = []
        self.ports = []
        self.litIndicators = []
        self.unlitIndicators = []

    def generateEdgework(self):
        possiblePorts = ["dvi-d", "parallel", "ps2", "rj-45", "serial", "stereo rca"]
        possibleIndicators = ["SND", "CLR", "CAR", "IND", "FRQ", "SIG", "NSA", "MSA", "TRN", "BOB", "FRK"]
        #generate serial
        self.serial = (''.join(random.choices(string.ascii_letters + string.digits, k=3)) + ''.join(random.choices(string.ascii_letters, k=2)) + ''.join(random.choices(string.digits, k=1))).upper()
        #generate batteries/ports/indicators
        #there are 5 edgework components, stats found from: https://www.reddit.com/r/ktane/comments/1jfemlx/bomb_generation/
        for i in range(5):
            edgeType = random.choice(["Battery", "Indicator", "Port"])
            match edgeType:
                case "Battery":
                    self.batteries.append(random.choice(["AA", "D"]))
                case "Indicator":
                    indicatorStr = random.choice(possibleIndicators)
                    if random.choice([True, False]):
                        self.litIndicators.append(indicatorStr)
                    else:
                        self.unlitIndicators.append(indicatorStr)
                case "Port":
                    self.ports.append(random.choice(possiblePorts))
        self.getEdgework()
        return
    def setEdgework(self):
        pass

    def getEdgework(self, getSerial = True, getBatteries = True, getPorts = True, getLit = True, getUnlit = True):
        listOfEdgework = []
        if getSerial :listOfEdgework.append(self.serial)
        if getBatteries: listOfEdgework.append(self.batteries)
        if getPorts: listOfEdgework.append(self.ports)
        if getLit: listOfEdgework.append(self.litIndicators)
        if getUnlit: listOfEdgework.append(self.unlitIndicators)
        return listOfEdgework

    def sayableEdgework(self, getSerial = True, getBatteries = True, getPorts = True, getLit = True, getUnlit = True):
        returnString = ""
        if getSerial:
            returnString += ("serial is " + self.serial)
            returnString += ". "
        if getBatteries and len(self.batteries) > 0:
            returnString += ("batteries: ")
            for battery in self.batteries:
                returnString += (battery)
        returnString += ". "
        if getPorts and len(self.ports) > 0:
            returnString += ("ports: ")
            for port in self.ports:
                returnString += (port) + ", "
            returnString = returnString[0:-2]
            returnString += ". "
        if getLit and len(self.litIndicators) > 0:
            returnString += ("lit indicators: ")
            for lit in self.litIndicators:
                returnString += (lit) + ", "
            returnString = returnString[0:-2]
            returnString += ". "
        if getUnlit and len(self.unlitIndicators) > 0:
            returnString += ("unlit indicators: ")
            for unlit in self.unlitIndicators:
                returnString += (unlit) + ", "
            returnString = returnString[0:-2]
            returnString += "."
        return returnString


class Ports(StrEnum):
    DVID = "dvi-d"
    PARALLEL = "parallel"
    PS2 = "ps/2"
    RJ45 = "rj-45"
    SERIAL = "serial"
    STEREORCA = "stereo rca"