def shuffle_ball(commands):
    # Initialize the ball position to 1
    pos = 1
    
    # Process each command
    for command in commands:
        if command == 'A':
            if pos == 1:
                pos = 2
            elif pos == 2:
                pos = 1
        elif command == 'B':
            if pos == 1:
                pos = 2
            elif pos == 2:
                pos = 1
        elif command == 'C':
            if pos == 1:
                pos = 3
            elif pos == 3:
                pos = 1
    
    return pos

# Example usage:
commands = input()
final_position = shuffle_ball(commands)
print(f"Final position of the ball: {final_position}")

