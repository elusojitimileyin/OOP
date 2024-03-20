from enum import Enum


class Player(Enum):
    X = 'x'
    O = 'O'
    EMPTY = '-'


def X():
    return 'X'


def O():
    return 'O'


def EMPTY():
    return '-'
