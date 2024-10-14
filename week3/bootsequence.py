"""meow"""
def argh(x):
    '''scream'''
    for i in range(1,x):
        print(i,sep=" ", end="_")
    print(x)
argh(int(input()))
