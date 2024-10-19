'''olypmic'''
def main():
    'gold'
    amount = int(input())
    competitors = []
    competitors_list = []

    #appends to list
    for _ in range(amount):
        competitors.append(input())

    #add medal count
    for i in competitors:
        country, gold, silver, bronze = i.split(" ")
        medals = int(gold) + int(silver) + int(bronze)
        competitors_list.append([country, gold, silver, bronze, medals])

    #sorting
        competitors_list = sorted(competitors_list, key=lambda x: x[4], reverse=True)

    #print
    for rank, competitor in enumerate(competitors_list, start=1):
        country, gold, silver, bronze, medals = competitor
        print(f"{rank} {country} {gold} {silver} {bronze} {medals}")
main()
