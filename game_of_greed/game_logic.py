from collections import Counter
import random

class GameLogic:
    """Class GameLogic handles calculating score for the dice roll.
    """
    @staticmethod
    def calculate_score(dice:tuple)->int:
        """[summary]

        Args:
            dice (tuple): integers that represent the dice roll

        Returns:
            int: roll's score
        """
        counter = Counter(dice)
        # print(counter)

        if len(dice) > 6:
            raise Exception("Please enter a max of 6 numbers")

        scores = {            
            1: {'single': 100, 'mult': 1000}, 
            2: {'single': 0, 'mult': 200},
            3: {'single': 0, 'mult': 300},
            4: {'single': 0, 'mult': 400}, 
            5: {'single': 50, 'mult': 500}, 
            6: {'single': 0, 'mult': 600} 
            }

        score = 0
        if len(counter) == 6 or list(counter.values()) == [2, 2, 2]:
            score += 1500
            return score
        elif len(counter.most_common()) == 6:
            return 10000

        for key, value in scores.items():
            counts = counter[key]
            single = value["single"]
            mult = value["mult"]
            if counts >= 3:
                score += (mult*(counts-2))
            if counts == 2:
                score += (single * 2)   
            if counts == 1:
                score += single
        return score

    @staticmethod
    def get_scorers(test_input):
        # tup = tuple([int(i) for i in test_input])
        scores_available = GameLogic.calculate_score(test_input)
        if scores_available == 0:
            return tuple()
        list = []
        for i in range(len(test_input)):
            print(test_input[i])
            if test_input[i] == 1 or test_input[i] == 5:
                list.append(test_input[i])
        print(list)
        return list

    @staticmethod
    def roll_dice(dice: int):
        """Rolls random dice.
        Args:
            dice (int): integers that represent the number of dice to roll
        Returns:
            int: roll nth number of dice and returns 1-6 random
        """
        if type(dice) is  not int:
            TypeError("Dice must be a number")
        elif (dice <= 0 or dice > 6):
            ValueError("Dice number must be between 1-6")
        return tuple(random.randint(1,6) for _ in range(dice))

class Banker:
    """Class Banker
    """
    def __init__(self):
        self.shelved = 0
        self.balance = 0
    
    # roll
    def shelf(self, shelf_points: int):
        """[takes in var from calculate_score and adds it to def__init__]
        Args:
            shelf_points (int): [int]
        """
        self.shelved += shelf_points

    # balance
    def bank(self):
        """
        Moves temporary (shelved) points to bank (balance).
        """
        self.balance += self.shelved
        self.shelved = 0
        return self.balance
    
    def clear_shelf(self):
        """clears shelf
        """
        self.shelved = 0


if __name__ == "__main__":

    GameLogic.get_scorers((1, 2))