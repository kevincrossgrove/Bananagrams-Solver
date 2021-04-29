# word = "HelloWorld"

# for index, x in enumerate(word):
#     print(index, x)


# Old function that found matches
# Take in the letter and length, and check that list for matches
# def checkListForMatches(letter, length, letters_counter):
#     if letter not in scrabble_dict[length]: return 

#     word_list = scrabble_dict[length][letter]

#     for word in word_list:
#         word_counter = Counter(word)
        
#         for key in word_counter:
#             if key not in letters_counter:
#                 break

#             if letters_counter[key] < word_counter[key]:
#                 break
#         else:
#             if length not in matches:
#                 matches[length] = [word]
#             else:
#                 matches[length].append(word)

list1 = [1, 2, 3, 4, 5, 6]
print(list1[1:])