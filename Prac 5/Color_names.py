"""
CP1404/CP5632 Practical
State colors in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
COLOR_NAMES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "azure1": "#f0ffff", "beige": "#f5f5dc",
               "black": "#000000", "blue1": "#0000ff", "cyan1": "#00ffff", "darkgreen": "#006400",
               "darkorange": "#ff8c00", "gold1": "#ffd700"}
# print(COLOR_NAMES)

color = input("Enter color name: ").lower()
while color != "":
    if color in COLOR_NAMES:
        print( "{:<3} is {}".format(color,COLOR_NAMES[color]))
    else:
        print("Invalid color name")
    color = input("Enter color name: ").lower()
