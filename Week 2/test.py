'''hjuh'''
def largest_number(oh, no, yikes):
    '''i hate this'''
    str1 = str(oh)
    str2 = str(no)
    str3 = str(yikes)
    option1 = str1 + str2 + str3
    option2 = str1 + str3 + str2
    option3 = str2 + str1 + str3
    option4 = str2 + str3 + str1
    option5 = str3 + str1 + str2
    option6 = str3 + str2 + str1
    largest = option1
    if str1 == "0" and str2 == "0"and str3 == "0":
        return "0"
    if option2 > largest:
        largest = option2
    if option3 > largest:
        largest = option3
    if option4 > largest:
        largest = option4
    if option5 > largest:
        largest = option5
    if option6 > largest:
        largest = option6
    return largest
def main():
    """this is so stupid"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    print(largest_number(num1, num2, num3))
main()
