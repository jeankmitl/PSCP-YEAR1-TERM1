"""pain"""
def main(num):
    """thank you"""
    size = (num*2)-1
    matrix = ''
    for i in range(size):
        sett = ''
        for j in range(size):
            if i == j or i == size - 1 - j:
                value = num
            elif abs(i - j) == 1 or abs(i + j - size + 1) == 1:
                value = num - 1
            else:
                value = num - 2
            sett += f"{value:02d} "
        matrix += sett + "\n"
    print(matrix)
main(int(input()))
