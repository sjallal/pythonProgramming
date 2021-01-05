from ThoughtWorks.MarsRoverProblem.InputParser import InputParser
from ThoughtWorks.MarsRoverProblem.Plateau import Plateau
from ThoughtWorks.MarsRoverProblem.Rover import Rover


if __name__ == "__main__":
    list_of_moves = InputParser().parse_input()
    Plateau_obj = Plateau(list_of_moves)
    Plateau_obj.final_coordinates()

"""

5 5
1 2 N
LMLMLMLMM

"""