from enum import StrEnum
import random


class KeypadSymbol(StrEnum):
    Q = "Q"
    AT = "at"
    Y = "Y"
    Z = "Z"
    SPIDER = "spider"
    H = "H"
    BACKWARDS_C = "backwards c"
    E = "E"
    SPRING = "spring"
    WHITE_STAR = "white star"
    QUESTION = "question"
    COPYRIGHT = "copyright"
    TOOTH = "tooth"
    K = "K"
    R = "R"
    SIX = "6"
    P = "P"
    TB = "T B"
    SMILEY = "smiley"
    TRIDENT = "trident"
    C = "C"
    THREE = "3"
    BLACK_STAR = "black star"
    PUZZLE = "puzzle"
    AE = "A E"
    N = "N"
    OMEGA = "omega"


def keypad():
    LINES = [
            [KeypadSymbol.Q, 
             KeypadSymbol.AT, 
             KeypadSymbol.Y, 
             KeypadSymbol.Z, 
             KeypadSymbol.SPIDER, 
             KeypadSymbol.H, 
             KeypadSymbol.BACKWARDS_C],
            [KeypadSymbol.E,
             KeypadSymbol.Q,
             KeypadSymbol.BACKWARDS_C,
             KeypadSymbol.SPRING,
             KeypadSymbol.WHITE_STAR,
             KeypadSymbol.H,
             KeypadSymbol.QUESTION,],
            [KeypadSymbol.COPYRIGHT,
             KeypadSymbol.TOOTH,
             KeypadSymbol.SPRING,
             KeypadSymbol.K,
             KeypadSymbol.R,
             KeypadSymbol.Y,
             KeypadSymbol.WHITE_STAR,],
            [KeypadSymbol.SIX,
             KeypadSymbol.P,
             KeypadSymbol.TB,
             KeypadSymbol.SPIDER,
             KeypadSymbol.K,
             KeypadSymbol.QUESTION,
             KeypadSymbol.SMILEY,],
            [KeypadSymbol.TRIDENT,
             KeypadSymbol.SMILEY,
             KeypadSymbol.TB,
             KeypadSymbol.C,
             KeypadSymbol.P,
             KeypadSymbol.THREE,
             KeypadSymbol.BLACK_STAR,],
            [KeypadSymbol.SIX,
             KeypadSymbol.E,
             KeypadSymbol.PUZZLE,
             KeypadSymbol.AE,
             KeypadSymbol.TRIDENT,
             KeypadSymbol.N,
             KeypadSymbol.OMEGA,],
            ]

    chosenLine = random.choice(LINES)
    values = random.sample(chosenLine, 4)
    return ", ".join(values)

def wires():
    wireColors = ["red", "yellow", "blue", "white", "black"]
    wires = random.choices(wireColors, k= random.randint(3,6))
    return " ".join(wires)

class BombModules(StrEnum):
    KEYPAD = "keypad"
    ROUND_KEYPAD = "round keypad"
    WIRES = "wires"
    FORGET_ME_NOT = "forget-me-not"



def get_bomb_module(module):
    match module:
        case BombModules.KEYPAD:
            return keypad()
        case BombModules.ROUND_KEYPAD:
            raise NotImplementedError
        case BombModules.WIRES:
            return wires()
        case BombModules.FORGET_ME_NOT:
            raise NotImplementedError
    raise ValueError
