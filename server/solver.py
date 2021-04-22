import json
from collections import Counter

with open('JsonDict.json', 'r') as input_file:
    data = input_file.read()

scrabble_dict = json.loads(data)

# Convert keys to ints
scrabble_dict = {int(k):v for k,v in scrabble_dict.items()}

# Dictionary that will store the matches
matches = {}

#letters = input('What are your letters?')
letters = "kevincrossgroveismyname"
letters_counter = Counter(letters)
letters_length = len(letters)
starting_length = letters_length if letters_length <= 15 else 15

# Take in the letter and length, and check that list for matches
def checkListForMatches(letter, length):
    if letter not in scrabble_dict[length]:
        return 

    word_list = scrabble_dict[length][letter]

    for word in word_list:
        word_counter = Counter(word)
        temp = letters_counter.copy()
        
        for key in word_counter:
            if key not in temp:
                break

            if temp[key] > 0:
                temp[key] -= 1
            else:
                break
        else:
            if length not in matches:
                matches[length] = [word]
            else:
                matches[length].append(word)

for letter in letters:
    for x in range(2, starting_length):
        checkListForMatches(letter, x)

print(matches)

# Remove all letter counts when a word is selected
# def updateLettersCounter:
#     pass
