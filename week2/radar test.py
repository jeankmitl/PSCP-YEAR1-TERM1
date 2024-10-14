import math

def main():
    """Check if one circle is completely inside the other."""
    # Input values for Circle 1
    x = float(input("Enter x coordinate of the first circle: "))
    y = float(input("Enter y coordinate of the first circle: "))
    r = float(input("Enter radius of the first circle: "))

    # Input values for Circle 2
    xn = float(input("Enter x coordinate of the second circle: "))
    yn = float(input("Enter y coordinate of the second circle: "))
    rn = float(input("Enter radius of the second circle: "))

    # Calculate the distance between the centers of the two circles
    d = math.sqrt((xn - x)**2 + (yn - y)**2)

    # Check if Circle 1 is completely inside Circle 2
    if d + r <= rn:
        print("Yes")
    # Check if Circle 2 is completely inside Circle 1
    elif d + rn <= r:
        print("Yes")
    else:
        print("No")

main()
