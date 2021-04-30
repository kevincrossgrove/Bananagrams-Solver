from tile import tile

class board:
    banana_board = []

    '''
    To access dictionary
    -> [length of word][first letter]
    '''
    banana_dictionary = []

    @classmethod
    def placeWord(cls, word, startX, startY, direction):

        for index, letter in enumerate(word):
            if direction == 'down':
                new_tile = tile(letter=letter, x=startX, y=startY+index, direction=direction)
            elif direction == 'right':
                new_tile = tile(letter=letter, x=startX+index, y=startY, direction=direction)
            
            cls.banana_board.append(new_tile)


    @classmethod
    def printBoard(cls):
        minX = 1000
        minY = 1000
        maxX = -1000
        maxY = -1000
        for tile in cls.banana_board:
            if tile.x > maxX:
                maxX = tile.x
            if tile.x < minX:
                minX = tile.x

            if tile.y > maxY:
                maxY = tile.y
            if tile.y < minY:
                minY = tile.y

        xDistance = maxX - minX
        yDistance = maxY - minY

        print_board = [['' for i in range(xDistance+3)] for j in range(yDistance+3)]

        for tile in cls.banana_board:
            print_board[tile.y + (minY * -1) + 1][tile.x + (minX * -1) + 1] = tile.letter
        
        for row in print_board:
            print(row)

        return print_board