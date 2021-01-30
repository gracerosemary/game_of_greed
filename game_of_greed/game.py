import os
import sys
# from collections import Counter
from game_of_greed.game_logic import GameLogic, Banker
# from game_logic import GameLogic, Banker

class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):
        self.banker = Banker()
        self.num_rounds = num_rounds
        
    def play(self, roller=None):
        """Entry point for playing (or declining) a game
        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """

        self.round_num = 0

        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")

        response = input("> ")

        if response == "y" or response == "yes":
            self.start_game()
        else:
            self.decline_game()

    def decline_game(self):
        print("OK. Maybe another time")
    
    def quit_game(self, score=0):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()
    
    def start_game(self):
        self.round_num += 1
        self.start_round(self.round_num)

    def start_round(self, round_num, number=6):
        print(f"Starting round {round_num}")
        current_round_score = 0
        while True:
            roll = self.rolling_dice(number)
            if self.farkle(roll):
                self.start_round
                # break
            selection = self.handle_selection(roll)
            print("(r)oll again, (b)ank your points or (q)uit:")
            response = input("> ")
            if response == "q":
                self.quit_game()
                return
            elif response == "b":
                current_round_score = self.banker.bank()
                print(f"You banked {str(current_round_score)} points in round {round_num}")
                print(f'Total score is {self.banker.balance} points')
                self.start_game()
                # break
            else:
                number -= len(selection)
                if number == 0:
                    number = 6

    def handle_selection(self, roll):
        while True:
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")
            if response == 'q':
                self.quit_game()
            saved_dice = self.saved_dice(roll, response)
            tup = tuple([int(i) for i in response])
            score = GameLogic.calculate_score(tup)
            break
        self.banker.shelf(score)
        print(f'You have {self.banker.shelved} unbanked points and {len(roll) - len(saved_dice)} dice remaining')
        return saved_dice
    
    def rolling_dice(self, number):
        print(f"Rolling {number} dice...")
        roll = self._roller(number)
        var = ' '
        for i in range(0, len(roll)):
            var += f'{roll[i]} '
        print(f"***{var}***")
        return roll

    def check_cheater(self, response, roll):
        tup = tuple([int(i) for i in response])
        for x in tup:
            if x not in roll:
                return False
        return True

    def saved_dice(self, roll, response):
        tup = tuple([int(i) for i in response])
        check = self.check_cheater(response, roll)
        if check == 0:
            print("Cheater!!! Or possibly made a typo...")
            var = ' '
            for i in range(0, len(roll)):
                var += f'{roll[i]} '
                if response == "q":
                    sys.exit()
            print(f"***{var}***")
            tup = tuple([int(i) for i in response])
            # print("Enter dice to keep, or (q)uit:")
            # response = input("> ")
        return tup

    def farkle(self, roll):
        score = GameLogic.calculate_score(roll)
        if score == 0:
            print(f"""****************************************
**        Zilch!!! Round over         **
****************************************""")
            self.banker.clear_shelf()
        # self.banker.shelved = 0
        # self.round_num += 1
        # self.start_round

# GameLogic.calculate_score(roll)
if __name__ == "__main__":
    game = Game()
    game.play()