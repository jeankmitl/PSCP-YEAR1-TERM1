'''postoffice'''
def main():
    '''post'''
    envelope = int(input())
    package = int(input())
    total = 0
    for _ in range(envelope):
        weight = float(input())
        if weight <= 10:
            total += 16
        elif weight <=20:
            total +=18
        elif weight <=100:
            total +=23
        elif weight <=250:
            total +=28
        elif weight <=500:
            total +=33
        elif weight <=1000:
            total +=48
        elif weight <=2000:
            total +=68
        total += 13
    for _ in range(package):
        weight = float(input())
        if weight <= 500:
            total += 45
        elif 500 < weight <=1000:
            total +=55
        elif 1000 < weight <=2000:
            total +=70
        total += 15
    print(total)
main()
