"""fishies"""
def main():
    """eat this fish"""
    sharkdictionary = {
        'Bull shark': 'THE SHALLOW ZONE',
        'Great white shark': 'THE TWILIGHT ZONE',
        'Chain catshark': 'THE TWILIGHT ZONE',
        'Gummy shark': 'THE TWILIGHT ZONE',
        'Blue shark': 'THE TWILIGHT ZONE',
        'Mako shark': 'THE TWILIGHT ZONE',
        'Frilled shark': 'THE MIDNIGHT ZONE',
        'Goblin shark': 'THE MIDNIGHT ZONE',
        'Sixgill shark': 'THE MIDNIGHT ZONE',
        'Greenland shark': 'THE MIDNIGHT ZONE',
        'Cookiecutter shark': 'THE MIDNIGHT ZONE',
        'Megamouth shark': 'THE ABYSSAL ZONE',
        }

    #checks what level the shark is from
    fishy = str(input()).capitalize()

    if 'shark' not in fishy:
        print('ZONE JAI MA KLUNG RAK DUAY KAN MAI.')
    elif fishy in sharkdictionary:
        print(sharkdictionary[fishy].upper())
    else:
        print('ZONE JAI MA KLUNG RAK DUAY KAN MAI.')

main()
