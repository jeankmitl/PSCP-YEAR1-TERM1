'''diamond'''
def main():
    """im mining"""
    row = int(input())
    column = int(input())
    diamondsum = [0] * column
    for _ in range(row):
        row = input().split()
        for col in range(column):
            diamondsum[col] += int(row[col])
    maxdiamond = max(diamondsum)
    print(maxdiamond)
main()
