"bgi plan"
#reowrk later
order = input()
num1 = int(input())
num2 = int(input())
num3 = int(input())
def checkerasc(num1, num2, num3):
    'checks ascendally'
    if num1 <= num2 <= num3:
        print(f"{num1}, {num2}, {num3}")
    elif num1 <= num3 <= num2:
        print(f"{num1}, {num3}, {num2}")
    elif num2 <= num1 <= num3:
        print(f"{num2}, {num1}, {num3}")
    elif num2 <= num3 <= num1:
        print(f"{num2}, {num3}, {num1}")
    elif num3 <= num2 <= num1:
        print(f"{num3}, {num2}, {num1}")
    else:
        print(f"{num3}, {num1}, {num2}")

def checkerdsc(num1, num2, num3):
    'checks desendally'
    if num1 >= num2 >= num3:
        print(f"{num1}, {num2}, {num3}")
    elif num1 >= num3 >= num2:
        print(f"{num1}, {num3}, {num2}")
    elif num2 >= num1 >= num3:
        print(f"{num2}, {num1}, {num3}")
    elif num2 >= num3 >= num1:
        print(f"{num2}, {num3}, {num1}")
    elif num3 >= num2 >= num1:
        print(f"{num3}, {num2}, {num1}")
    else:
        print(f"{num3}, {num1}, {num2}")

def main():
    "too many plans"
    if order == "Ascend":
        checkerasc(num1, num2, num3)
    if order == "Descend":
        checkerdsc(num1, num2, num3)
main()
