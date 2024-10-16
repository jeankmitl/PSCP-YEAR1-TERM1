import json

def format_input(user_input):
    user_input = user_input.strip()
    if not user_input.startswith("{") and not user_input.endswith("}"):
        user_input = "{" + user_input + "}"
    user_input = user_input.replace("'", '"')
    return user_input

def main():
    num = int(input())
    foxes = {}
    cats = {}
    for _ in range(num):
        temp = input().strip()
        formatted_temp = format_input(temp)
        try:
            creature = json.loads(formatted_temp)
        except json.JSONDecodeError:
            continue
        for name, animal in creature.items():
            if 'Fox' in animal:
                foxes[name] = animal
            elif 'Cat' in animal:
                cats[name] = animal
    if 'Cat01' not in cats.values() and 'Garfield' not in cats:
        if 'Garfield' not in foxes:
            cats["Garfield"] = "Cat01"
    if 'Fox01' not in foxes.values() and 'Fubuki' not in foxes:
        if 'Fubuki' not in cats:
            foxes["Fubuki"] = "Fox01"
    if cats:
        cats = dict(sorted(cats.items(), key=lambda item: item[1]))
    if foxes:
        foxes = dict(sorted(foxes.items(), key=lambda item: item[1]))
    cats_amount = len(cats)
    foxes_amount = len(foxes)
    print(f"Cat : {cats_amount}")
    print(f"Fox : {foxes_amount}")
    for i, ij in cats.items():
        print(f"{i} : {ij}")
    for j, jj in foxes.items():
        print(f"{j} : {jj}")

main()
