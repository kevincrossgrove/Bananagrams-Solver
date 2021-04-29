class tile:
    def __init__(self, letter, x, y, direction, available = True):
        self.letter = letter
        self.x = x
        self.y = y
        self.direction = direction
        self.available = available

    def __str__(self):
        return '{} {} {} {}'.format(self.letter, self.x, self.y, self.available)

    def __repr__(self):
        return '{} {} {} {}'.format(self.letter, self.x, self.y, self.available)
