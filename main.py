import random

map = ["e", "df", "def", "acgi", "acegi", "acdfgi"]


def convert(char):
    if char == "a": return 1
    if char == "b": return 2
    if char == "c": return 3
    if char == "d": return 7
    if char == "e": return 8
    if char == "f": return 9
    if char == "g": return 13
    if char == "h": return 14
    if char == "i": return 15


def forma(roll):
    mapped = map[roll-1]
    output = list("[---]\n[   ]\n[   ]\n[   ]\n[---]")
    for place in mapped:
        output[convert(place)+6] = "0"

    return "".join(output)


running = True
while running:
    ran = random.randint(1, 6)
    print(forma(ran))
    res = input("press y to roll again and n to exit:")
    if res == "n":
        running = False
