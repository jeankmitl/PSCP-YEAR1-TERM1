"""coffee"""
def main():
    """coffee"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = int(input())
    if e == 1:
        p1 = a
    else:
        p1 = a + (e - 1) * a * (1 - b / 100)
    price = e * a
    if price >= d:
        p2 = price * (1 - c / 100)
    else:
        p2 = price
    if p1 == p2:
        print("2")
        print(f"{p2:.2f}")
    elif p1 < p2:
        print("1")
        print(f"{p1:.2f}")
    else:
        print("2")
        print(f"{p2:.2f}")
main()
