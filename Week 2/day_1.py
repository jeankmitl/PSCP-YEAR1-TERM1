"""day i"""
def main():
    """tester"""
    year  = int(input())
    if not year % 4:
        y = year / 4
    else:
        print("No")
    if not y % 100:
        z = y / 100
    else:
        print("Yes")
    if not z % 400:
        print("Yes")
    else:
        print("No")
main()
    