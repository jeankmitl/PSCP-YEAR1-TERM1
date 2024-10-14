'calc'
def count_press(num):
    'stupidcalcs'
    if num == 1:
        return 1
    press = 0
    digits = len(str(num))
    for i in range(1, digits):
        press += 9 * i * (10 ** (i - 1))
    press += digits * (num - 10 ** (digits - 1) + 1)
    press += num
    return press
print(count_press(int(input())))
