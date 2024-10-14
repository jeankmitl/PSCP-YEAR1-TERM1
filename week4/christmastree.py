'''christmastree'''
def tree():
    '''could you beilieve it? 3 months away from december!'''
    tree_size = int(input())
    bark_height = int(input())
    space = " "
    star = "*"
    bark = "---"
    for i in range(tree_size):
        print((space * ((tree_size - 1) - i)) + (star * (i + 1)) + (star * i))
    for i in range(bark_height):
        print((space * (tree_size - 2)) + bark)
tree()
