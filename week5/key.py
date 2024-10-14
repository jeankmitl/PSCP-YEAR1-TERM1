"key"
def firstcon(x):
    "applies first con"
    total = 0
    for nums in x:
        total = total + int(nums)
    return total
def secondcon(x):
    "applies second condition"
    return int(x[10:]) * 10

def main():
    "the thing that does things wow"
    key = input()
    ans1 = firstcon(key) #it's 13 numbers btw
    ans2 = secondcon(key)
    final = ans1 + ans2
    string_final = str(final)
    if final >= 10000:
        print(string_final[-4:])
    elif final < 1000:
        print(final + 1000)
    else:
        print(final)
main()
