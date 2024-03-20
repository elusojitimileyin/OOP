from collections import namedtuple

Player = namedtuple("player", ["name"])

p1 = Player("timi")
print(p1.name)
