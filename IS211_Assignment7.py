#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a game of pig"""


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
        """next_turn accepts user input and performs game actions."""

        print('{} score is: {}'.format(self.current_player.name, self.current_player.score))
        # current player must choose roll or hold
        choice = 'pig'
        # check if correct input given
        while choice not in ['r', 'h']:
            choice = raw_input('{} enter r or h to continue: '.format(self.current_player.name))

        while choice == 'r':
            # current player rolls
            # display current roll total and total players
            die_roll = self.die.roll()
            print('You rolled {}'.format(die_roll))

            # roll anything other than 1, add to tally
            if die_roll != 1:
                self.current_player.tally += die_roll
                print('Your roll tally is: {}'.format(self.current_player.tally))
                # roll another turn
                choice = 'anything'
                while choice not in ['r', 'h']:
                    choice = raw_input('{} enter r or h to continue: '.format(self.current_player.name))
            else:
                self.current_player.tally = 0
                choice = 'not r'

        # current player holds
        # display current roll total and total players
        self.current_player.score += self.current_player.tally
        self.current_player.tally = 0
        print('{} score is: {}'.format(self.current_player.name, self.current_player.score))
        # shifting the baton
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

if __name__ == '__main__':
    # create game
    pig = Game()
    # run game
    while pig.player1.score < 100 and pig.player2.score < 100:
        pig.next_turn()
    if pig.player1.score > 99:
        winner = pig.player1
    else:
        winner = pig.player2
    print('The winner is: {}'.format(winner.name))
