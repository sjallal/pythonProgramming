from ThoughtWorks.MarsRoverProblem.InputParser import InputParser
from ThoughtWorks.MarsRoverProblem.Plateau import Plateau

if __name__ == "__main__":
    x_max, y_max = InputParser.parse_plateau_size()
    Plateau.set_plataue_size(x_max, y_max)
    list_of_rovers = InputParser.parse_list_of_rovers()
    for rover in list_of_rovers:
        x_cor, y_cor, direc = rover.final_coordinates()
        if direc != 'Z':
            print(x_cor, y_cor, direc, sep=" ")
        else:
            print("Out of range.")

"""

5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

"""
