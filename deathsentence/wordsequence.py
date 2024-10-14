'''wordsequence'''
def main():
    'why'
    word = input()
    for i in range(1, len(word) + 1):
        print(word[:i])
main()
