'''inflation'''
def infalte():
    '''no moar money'''
    price = int(float(input()) * 100)
    years = int(input())
    for _ in range(years):
        price = price + ((price * 381) // 10000)
    print(f"{price // 100}.{(price % 100):>02}")
infalte()
