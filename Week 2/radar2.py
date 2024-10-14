"""imactuallygoinginsane"""
import math
def main():
    """soemthingsomethingpleasework"""
    x = float(input())
    y = float(input())
    r = float(input())
    xn = float(input())
    yn = float(input())
    rn = float(input())
    d = math.sqrt((xn - x)**2 + (yn - y)**2)
    if d < r + rn:
        print("Yes")
    else:
        print("No")
main()
