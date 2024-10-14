'''sequenceviii'''
# print(f"{number:02}") this is PAINFUL.
def main():
    '''vi''' 
    x = int(input())
    for i in range(1 , x+1):
        for j in range(1, i+1):
            print(f"{j:02}", end=" ")
        print()
main()
