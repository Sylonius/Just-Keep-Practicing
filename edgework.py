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
        possiblePorts = ["dvi-d", "parallel", "ps/2", "rj-45", "serial", "stereo rca"]
        possibleIndicators = ["SND", "CLR", "CAR", "IND", "FRQ", "SIG", "NSA", "MSA", "TRN", "BOB", "FRK"]
        #generate serial
        self.serial = ''.join(random.choices(string.ascii_letters + string.digits, k=3)), ''.join(random.choices(string.ascii_letters, k=2)), ''.join(random.choices(string.digits, k=1))
        #generate batteries/ports/indicators
        #there are 5 edgework components, stats found from: https://www.reddit.com/r/ktane/comments/1jfemlx/bomb_generation/
        for i in range(5):
            edgeType = random.choice("Battery", "Indicator", "Port")
            match edgeType:
                case "Battery":
                    self.batteries.append(random.choice("AA", "D"))
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
        if getSerial : listOfEdgework.append(self.serial)
        if getBatteries: listOfEdgework.append(self.batteries)
        if getPorts: listOfEdgework.append(self.ports)
        if getLit: listOfEdgework.append(self.litIndicators)
        if getUnlit: listOfEdgework.append(self.unlitIndicators)
        return listOfEdgework

class Ports(StrEnum):
    DVID = "dvi-d"
    PARALLEL = "parallel"
    PS2 = "ps/2"
    RJ45 = "rj-45"
    SERIAL = "serial"
    STEREORCA = "stereo rca"