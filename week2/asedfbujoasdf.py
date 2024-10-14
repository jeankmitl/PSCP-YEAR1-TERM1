def largest_number(oh, no, yikes):
    '''Find the largest number formed by concatenating three given numbers in different orders.'''
    # Convert numbers to strings
    str1 = str(oh)
    str2 = str(no)
    str3 = str(yikes)
    
    # Generate all permutations of concatenated strings
    option1 = str1 + str2 + str3
    option2 = str1 + str3 + str2
    option3 = str2 + str1 + str3
    option4 = str2 + str3 + str1
    option5 = str3 + str1 + str2
    option6 = str3 + str2 + str1
    
    # Initialize largest with the first option
    largest = option1
    
    # Compare each option to find the largest
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
    # Get user inputs
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    
    # Compute and print the largest number
    result = largest_number(num1, num2, num3)
    print(f"The largest number formed by {num1}, {num2}, and {num3} is {result}.")

main()
