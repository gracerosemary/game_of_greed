from game_logic import GameLogic, Banker

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
    
    def closing(self, score=0):
        print(f"Thanks for playing. You earned {score} points")

    def start_game(self):
        removed = 0
        remaining = 6
        self.round_num += 1
        roll = GameLogic.roll_dice(remaining)
        print(f"""
Starting round {self.round_num}
Rolling {remaining} dice...
*** {roll[0]} {roll[1]} {roll[2]} {roll[3]} {roll[4]} {roll[5]} ***
        """)
        current_roll = GameLogic.calculate_score(roll)
        if current_roll == 0:
            print('Farkle!')
        else:
            remaining = remaining - removed
            save = input("""Enter dice to keep, or (q)uit:
> """)
        if save == 'q':
            self.closing()
        else:
            print(save)
            dice = str([int(i) for i in remaining])
            tup = tuple([int(i) for i in save])
            score = GameLogic.calculate_score(tup)
            print(tup)
            removed += len(tup)
            while removed != 0:
                print(f'You have {score} unbanked points and {6 - removed} dice remaining')
                roll_again = input("""(r)oll again, (b)ank your points or (q)uit:
> 
                """)
                if roll_again == 'r':
                    if current_roll == 0:
                        print('Farkle!')
                        Banker.shelved = 0
                        self.round_num += 1
                    else:
                        roll = GameLogic.roll_dice(remaining)
                        print(dice)
                        print(f"""Rolling {remaining} dice...
*** {dice} ***
)""")
                    
                elif roll_again == 'b':
                    Banker.bank
                elif roll_again == 'q':
                    self.closing()
                    break
                else:
                    pass

# GameLogic.calculate_score(roll)
if __name__ == "__main__":
    game = Game()
    game.play()