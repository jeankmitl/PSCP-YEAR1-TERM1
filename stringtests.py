def main():
    '''vi'''
    x = int(input())
    
    # Calculate the maximum width needed for right alignment
    max_width = len(" ".join(f"{i:02}" for i in range(1, x + 1)))
    
    for i in range(1, x + 1):
        # Create the row with formatted numbers
        row = " ".join(f"{j:02}" for j in range(1, i + 1))
        
        # Right-align the row within the max width
        print(f"{row:>{max_width}}")

main()
