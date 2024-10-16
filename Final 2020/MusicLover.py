"""musichater"""
def main():
    """nah jk lol"""
    music = int(input())
    musicdict = {}

    for _ in range(music):
        micle = str(input()).replace('-','ฃ').split('ฃ')
        artist = micle[0]
        title = micle[1]

        if artist in musicdict:
            musicdict[artist].append(title)
        else:
            musicdict[artist] = [title]

    x = musicdict.items()

    for i in x:
        print(i[0])
        for j in i[1]:
            print(j)

main()
