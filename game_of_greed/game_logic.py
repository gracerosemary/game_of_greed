from collections import Counter
import random

class GameLogic:
    @staticmethod
    def calculate_score(score:tuple):
        pass

    @staticmethod
    def roll_dice(dice: int):
        if type(roll_dice) is  not int:
            raise TypeError("Dice must be a number")
        elif (dice <= 0 or dice > 6):
            raise ValueError("Dice number must be between 1-6")
        return tuple(random.randint(1,6) for _ in range(dice))

class Banker:

    def __init__(self):
        pass
        
    def shelf(self, shelf_points: int):
        pass

    def bank(self, bank_points: int):
        pass

    def clear_shelf(self):
        pass


if __name__ == "__main__":
    def roll_dice(dice: int):
        if type(dice) is  not int:
            raise TypeError("Dice must be a number")

        elif (dice <= 0 or dice > 6):
            raise ValueError("Dice number must be between 1-6")

        return tuple(random.randint(1,6) for _ in range(dice))
