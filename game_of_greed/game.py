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

        self._roller = roller or GameLogic.roll_dice(6)

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

    def start_game(self):
        self.round_num += 1
        self.start_round(self.round_num)

    def start_round(self, round_num, number=6):
        removed = 0
        remaining = 6
        roll = self._roller(number)
        new_roll = ' '.join((str(i) for i in roll))
        print(f"""Starting round {self.round_num}
Rolling {remaining} dice...
*** {new_roll} ***""")
        current_roll = GameLogic.calculate_score(roll)
        if current_roll == 0:
            print('Farkle!')
        else:
            # remaining = remaining - removed
            self.handle_selection(removed, current_roll, remaining)
    
    def handle_selection(self, removed, current_roll, remaining):
        save = input("""Enter dice to keep, or (q)uit:
> """)
        if save == 'q':
            self.quit_game()
            exit()
        else:
            tup = tuple([int(i) for i in save])
            score = GameLogic.calculate_score(tup)
            self.banker.shelf(score)
            removed += len(tup)
            while removed != 0:
                print(f'You have {self.banker.shelved} unbanked points and {6 - removed} dice remaining')
                roll_again = input("""(r)oll again, (b)ank your points or (q)uit:
> """)

                if roll_again == 'r':
                    if current_roll == 0:
                        print('Farkle!')
                        self.banker.shelved = 0
                        self.round_num += 1
                    else:
                        roll = GameLogic.roll_dice(remaining - removed)
                        current_roll = GameLogic.calculate_score(roll)
                        var = ''
                        for i in range(0, len(roll)):
                            var += f' {roll[i]}'
                        print(f"""Rolling {remaining - removed} dice...
***{var} ***""")
                        print(f'You have {self.banker.shelved} unbanked points and {6 - removed} dice remaining')
                        save = input("""Enter dice to keep, or (q)uit:
> """)
                        if save == 'q':
                            self.quit_game()
                            exit()
                        else:
                            tup = tuple([int(i) for i in save])
                            score = GameLogic.calculate_score(tup)
                            self.banker.shelf(score)
                            removed += len(tup)
                elif roll_again == 'b':
                    print(f"You banked {self.banker.shelved} points in round {self.round_num}")
                    self.banker.bank()
                    print(f'Total score is {self.banker.balance} points')
                    self.start_game()
                else:
                    self.quit_game()
                    exit()

# GameLogic.calculate_score(roll)
if __name__ == "__main__":
    game = Game()
    game.play()