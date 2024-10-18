'''olypmic'''
def main():
    'gold'
    amount = int(input())
    competitors = []

    for _ in range(amount):
        string = input()
        #splits into different catagories
        country, gold, silver, bronze = string.split(" ")

        #count
        medal_count = int(gold) + int(bronze) + int(silver)
        competitors.append(f"{country} {gold} {silver} {bronze} {medal_count}")

    #sort
    for j in competitors:
        

    #print
    for i in competitors:
        print(i)
main()
