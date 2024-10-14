"""WOW."""
def main():
    """HIT HARD A BROKEN WALL"""
    total = float(input())
    highest = float(input())
    second = min(total - highest, highest)
    lowest = total - highest - second
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
