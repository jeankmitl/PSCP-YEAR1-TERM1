def cloudy(hour, wetness):
    '''cloudy'''
    if 6 <= hour < 18:
        wetness -= 0.50
    else:
        wetness -= 0.25
    return wetness

def normal(hour, wetness):
    '''SUN'''
    if 6 <= hour < 18:
        wetness -= 1.00
    else:
        wetness -= 0.50
    return wetness

def windy(hour, wetness):
    '''AAAAAAAAAAAA'''
    if 6 <= hour < 18:
        wetness -= 1.50
    else:
        wetness -= 0.75
    return wetness

def rain(wetness):
    ''':('''
    return wetness + 2.00

def storm(wetness):
    '''AAAAAAAAAAAAAAAAAAAAAAA'''
    return wetness + 3.00

def main():
    '''amf'''
    hour = int(input())
    log = input()
    wetness = 8
    
    for weather in log:
        if wetness <= 0:
            print('Dry')
            return
        
        if weather.lower() == 'c':
            wetness = cloudy(hour, wetness)
        elif weather.lower() == 'n':
            wetness = normal(hour, wetness)
        elif weather.lower() == 'w':
            wetness = windy(hour, wetness)
        elif weather.lower() == 'r':
            wetness = rain(wetness)
        elif weather.lower() == 's':
            print('CLOTHES GONE.')
            return
        
        hour = hour % 24 + 1
    
    print(f'Wetness: {wetness:.2f}')

main()