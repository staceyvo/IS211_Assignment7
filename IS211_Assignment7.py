import random


class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.tally = 0


class Die(object):
    def roll(self):
        return random.randint(1, 6)


class Game(object):
    def __init__(self):
        self.die = Die()
        self.player1 = Player(raw_input('Please enter your name: '))
        self.player2 = Player(raw_input('Please enter your name: '))
        self.current_player = self.player1

    def next_turn(self):
        # current player must choose roll or hold
        choice = raw_input('Please enter r or h to continue: ')

        if choice == 'r':
            # current player rolls
            # display current roll total and total players
            die_roll = self.die.roll()
            print('You rolled {}'.format(die_roll))
            print('Your score is: {}'.format(self.current_player.score))
            if die_roll != 1:
                self.current_player.tally += die_roll
            else:
                self.current_player.tally = 0
                # shifting the baton
                if self.current_player == self.player1:
                    self.current_player = self.player2
                else:
                    self.current_player == self.player1
                
        else:
            # current player holds
            # display current roll total and total players
            self.current_player.score += self.current_player.tally
            self.current_player.tally = 0
            print('Your score is: {}'.format(self.current_player.score))

