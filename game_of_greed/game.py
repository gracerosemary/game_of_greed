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
    
    def closing(self, score):
        print(f"Thanks for playing. You earned {score} points")

    def start_game(self):
        removed = 0
        roll = GameLogic.roll_dice(6)
        print(f"""
Starting round 1
Rolling 6 dice...
*** {roll[0]} {roll[1]} {roll[2]} {roll[3]} {roll[4]} {roll[5]} ***
        """)
        save = input("""Enter dice to keep, or (q)uit:
> """)
        if save == 'q':
            self.closing()
        else:
            print(save)
            tup = tuple([int(save)])
            score = GameLogic.calculate_score(tup)
            print(tup)
            removed += len(tup)
            print(f'You have {score} unbanked points and {6 - removed} dice remaining')


if __name__ == "__main__":
    game = Game()
    game.play()