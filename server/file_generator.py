import json

# This file can be used to read in a text file and generate a json file
# that can be used to create bananagrams boards

scrabble_dict = {}

# Open the text file, remove newlines and make lowercase. Then create dictionary
with open('ScrabbleDict.txt', 'r') as input_file:
    words = input_file.read().splitlines()

    for word in words:
        word = word.lower()
        word_length = len(word)
        first_letter = word[0]

        if word_length not in scrabble_dict:
            scrabble_dict[word_length] = { first_letter: [word] }
            continue
        
        if first_letter not in scrabble_dict[word_length]:
            scrabble_dict[word_length][first_letter] = [word]
            continue
             
        scrabble_dict[word_length][first_letter].append(word)

# Write the Python Dict to JSON file
with open('JsonDict.json', 'w') as output_file:
    json.dump(scrabble_dict, output_file)