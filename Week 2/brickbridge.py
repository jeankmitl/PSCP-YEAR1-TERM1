"""bricc bridge"""
a = int(input())
b = int(input()) * 5
goal = int(input())

def main():
    """meow"""
    if b <= goal:
        if a > goal - b:
            print(goal - b)
        else:
            print("-1")
    elif b >= goal:
        if not goal % 5:
            print("0")
        elif goal % 5 <= a:
            print(goal % 5)
        else:
            print("-1")
main()
