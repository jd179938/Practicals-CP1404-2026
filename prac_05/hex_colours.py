"""
CP1404 Practical Week 5
Search for colours hexadecimal value in dictionary
"""

colour_name_to_hexadecimal = {'Aqua': '#00ffff', 'Ash Gray': '#b2beb5', 'Baby Pink': '#f4c2c2',
                              'Banana Yellow': '#ffe135', 'Bubble Gum': '#ffc1cc', 'Candy Red Apple': '#ff0800',
                              'Chocolate': '#d2691e', 'Corn': '#fbec5d', 'Denim': '#1560bd'}

colour_name = input("Enter colour: ")
while colour_name != '':
    try:
        print(colour_name_to_hexadecimal[colour_name])
    except KeyError:
        print("Invalid colour")
    colour_name = input("Enter colour: ")
