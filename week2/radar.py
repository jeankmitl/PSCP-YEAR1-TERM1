"""PointinCircle"""
import math
def main():
    """lmao"""
    x = float(input())
    y = float(input())
    r = float(input())
    xn = float(input())
    yn = float(input())

    d = math.sqrt((xn - x)**2 + (yn - y)**2)
    if d <= r:
        print("Yes")
    else:
        print("No")
main()
