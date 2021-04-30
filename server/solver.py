import json
import time
from collections import Counter
from letter_values import letter_values_dict
from board import board

start_time = time.time()

with open('JsonDict.json', 'r') as input_file:
    data = input_file.read()

scrabble_dict = json.loads(data)

# Convert keys to ints
scrabble_dict = {int(k):v for k,v in scrabble_dict.items()}

def selectBestWord(words):
    biggestSum = 0
    biggestWord = ''

    for word in words:
        sum = 0
        for letter in word:
            sum += letter_values_dict[letter]
        
        if (sum > biggestSum):
            biggestSum = sum
            biggestWord = word
    
    words.remove(biggestWord)
    return biggestWord

# Remove all playable letters when a word is selected
def updateLetters(letters, word):
    if (word == None): return letters
    for letter in word:
        letters = letters.replace(letter, '', 1)

    return letters
    

# Remove the selected word from the dictionary
def removeWordFromDictionary(selected_word):
    if selected_word == None: return
    length = len(selected_word)
    letter = selected_word[0]
    board.banana_dictionary[length][letter].remove(selected_word)


# Returns the first list of matches it finds, starting at largest length
def findMatches(letters):
    dictionary = board.banana_dictionary
    letters_counter = Counter(letters)
    starting_length = len(letters) if len(letters) <= 15 else 15

    for length in range(starting_length, 2, -1):
        
        for letter in letters:
            if letter not in dictionary[length]: continue

            word_list = dictionary[length][letter]
            match_list = []

            for word in word_list:
                word_counter = Counter(word)
                
                for key in word_counter:
                    if key not in letters_counter:
                        break

                    if letters_counter[key] < word_counter[key]:
                        break
                else:
                    match_list.append(word)
        
            if (len(match_list) > 0):
                return match_list
    
    return None

def findIntersectMatch(letters):
    dictionary = board.banana_dictionary

    start_letters = letters

    starting_length = len(letters)+1 if len(letters)+1 <= 15 else 15

    for length in range(starting_length, 2, -1):
        tile_set = set()
        for tile in board.banana_board:
            if (tile.available):
                if tile.letter in tile_set: continue
                else: tile_set.add(tile.letter)

                letters = start_letters + tile.letter
                letters_counter = Counter(letters)

                for letter in letters:
                    word_list = dictionary[length][letter]
                    match_list = []

                    for word in word_list:
                        word_counter = Counter(word)

                        for key in word_counter:
                            if key not in letters_counter:
                                break

                            if letters_counter[key] < word_counter[key]:
                                break
                        else:
                            if tile.letter in word:
                                match_list.append(word)
                
                    if (len(match_list) > 0):
                        best_word = selectBestWord(match_list)
                        # match_list.remove(best_word)
                        print(best_word)
                        tile.available = False
                        if (tile.direction == 'right'):
                            magnitude = best_word.index(tile.letter)
                            print(tile.y, magnitude)
                            x = tile.x
                            y = tile.y - magnitude
                            board.placeWord(best_word, x, y, 'down')
                        else:
                            magnitude = best_word.index(tile.letter)
                            x = tile.x - magnitude
                            y = tile.y
                            board.placeWord(best_word, x, y, 'right')
                        
                        return best_word
                        
    return None


# Main function that will accept letters and create 2D array with them
def createBoard(letters, update=False, extensive=True):
    # Save letters in case we need to try again
    starting_letters = letters

    # Reset the dictionary if it is not an update
    if (update == False): 
        dictionary = scrabble_dict.copy()
        board.banana_dictionary = dictionary

    board.banana_board = []
    match_list = findMatches(letters)
    
    # Find the best starting word
    best_word = selectBestWord(match_list)
    print(letters)
    letters = updateLetters(letters, best_word)
    removeWordFromDictionary(best_word)

    # Add first word to the board
    board.placeWord(best_word, 0, 0, 'right')
    print(letters)

    while best_word != None and letters != None:
        best_word = findIntersectMatch(letters)
        letters = updateLetters(letters, best_word)
        print(letters)

    final_board = board.printBoard()

    print('Remaining Letters: ', letters, len(letters))
    if (extensive and len(letters) != 0): createBoard(starting_letters, True)
    
    data = {'data': [], 'remaining': letters}
    for row in final_board:
        data['data'].append(row)

    print("Program executed in", time.time() - start_time, "seconds.")        
    return data 


# createBoard("kevincrossgroveismyname")
# createBoard("kevincrossgroveismyname", True)
    