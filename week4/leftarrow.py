'''leftarrow'''
import math
def arrow():
    '''slide to the left!'''
    width = int(input())
    height = int(input())
    space = " "
    star = "*"
    top = math.ceil(height / 2)
    bottom = math.floor(height // 2)
    for i in reversed(range(0, top)):
        print((space * i) + (star * width))
    for j in range(0, bottom):
        print((space * (j + 1)) + (star * width))
arrow()
