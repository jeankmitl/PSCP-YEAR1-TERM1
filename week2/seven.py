"""seven"""
def calc(x):
    """meow"""
    #indexes idk it counts the last num of the result from pwr
    calcnum = [7, 9, 3, 1]
    if not x:
        return 1
    y = (x - 1) % 4
    return calcnum[y]

def main():
    """MEEEEEEEEEEEOW"""
    x = int(input())
    print(calc(x))
main()
