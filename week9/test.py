import json

def main():
    'catgirls or fox girls'
    try:
        num = int(input())
    except ValueError:
        print("Please enter a valid number.")
        return

    # Separate dictionaries for cats and foxes
    foxes = {}
    cats = {}

    for _ in range(num):
        try:
            creature = json.loads(input())
            if not isinstance(creature, dict):
                raise ValueError("Input must be a JSON object.")
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Invalid input: {e}")
            continue

        for name, animal in creature.items():
            if 'Fox' in animal and name not in foxes:
                foxes[name] = animal  # Add to foxes dictionary if not already present
            elif 'Cat' in animal and name not in cats:
                cats[name] = animal  # Add to cats dictionary if not already present

    # Check for missing creatures and add them if necessary
    if not any(x in cats for x in ['Cat01', 'Garfield', 'Fubuki']):
        cats["Garfield"] = "Cat01"
    
    if not any(x in foxes for x in ['Fox01', 'Garfield', 'Fubuki']):
        foxes["Fubuki"] = "Fox01"

    # Sort by items (by value, then by key if necessary)
    cats = dict(sorted(cats.items(), key=lambda item: (item[1], item[0])))
    foxes = dict(sorted(foxes.items(), key=lambda item: (item[1], item[0])))

    # Count
    cats_amount = len(cats)
    foxes_amount = len(foxes)

    # Print results
    print(f"Cat : {cats_amount}")
    print(f"Fox : {foxes_amount}")
    for i in cats:
        print(f"{i} : {cats[i]}")
    for j in foxes:
        print(f"{j} : {foxes[j]}")

main()
