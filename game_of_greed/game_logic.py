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

        if len(dice) > 6:
            raise Exception("Please pick a number from 1-6")

        scores = {            
            1: {'single': 100, 'mult': 1000}, 
            2: {'single': 0, 'mult': 200},
            3: {'single': 0, 'mult': 300},
            4: {'single': 0, 'mult': 400}, 
            5: {'single': 50, 'mult': 500}, 
            6: {'single': 0, 'mult': 600} 
            }

        for key, value in scores.items():
            counts = counter[key]
            score = 0
            if len(counter) == 6 or list(counter.values()) == [2, 2, 2]:
                score += 1500
                return score
            elif len(counter.most_common()) == 6:
                return 100000  
            for key2, value2 in value.items():
                single = value["single"]
                mult = value["mult"]
                if counts == 1:
                    score += single
                    return score
                elif counts == 2:
                    score += (single * 2)
                    return score
                elif counts >= 3:
                    score += (mult*(counts-2))
                    return score

    @staticmethod
    def roll_dice(dice: int):
        if type(roll_dice) is  not int:
            raise TypeError("Dice must be a number")
        elif (dice <= 0 or dice > 6):
            raise ValueError("Dice number must be between 1-6")
        return tuple(random.randint(1,6) for _ in range(dice))

class Banker:
    def __init__(self):
        self.roll = 0
        self.balance = 0
    
    # roll
    def shelf(self, shelf_points: int):
        # takes in var from calculate_score and adds it to def__init__
        self.roll += shelf_points

    # balance
    def bank(self):
        self.balance += self.roll
        shelf = self.shelved
        self.clear_shelf()
        return shelf
    
    def clear_shelf(self):
        self.roll = 0


   