def count_vowels(word, vowels):
    return sum(word.count(vowel) for vowel in vowels)

letters = ['a', 'e', 'i', 'o', 'u']
sortlist = []
transd = "arcu ut a a eu".split()  # Splitting the input string into words

for word in transd:
    vowel_count = count_vowels(word, letters)
    if vowel_count >= 2 and len(word) > 2:
        sortlist.append(word)

print(sortlist)