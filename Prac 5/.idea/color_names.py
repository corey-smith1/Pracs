"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
COLOR_NAMES = {"aliceblue": "#f0f8ff", "brown": "#a52a2a", "chocolate": "#d2691e", "black": "#000000",
               "darkgreen": "006400", "gray": "#bebebe", "HotPink": "ff69b4", "lavender": "e6e6fa",
               "light": "eedd82", "medium": "66cdaa"}
# print(STATE_NAMES)

color = input("Enter color Name: ").lower()
while color != "":
    if color in COLOR_NAMES:
        print( "{:<3} is {}".format(color,COLOR_NAMES[color]))
    else:
        print("Invalid color Name")
    color = input("Enter color Name: ").lower()