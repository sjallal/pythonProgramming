class InputParser:

    def __init__(self):
        self.x_ = 0

    def plat_size(self):
        x_max, y_max = map(int, input().split())
        return x_max, y_max

    def parse_input(self):

        list_of_inputs = []
        while True:
            rover_position = input()
            instructions = input()
            if not rover_position:
                break
            x_coordinate = self.x_position(rover_position)
            y_coordinate = self.y_position(rover_position)
            direction = self.rover_direction(rover_position)
            rover_instructions = self.rover_instruction(instructions)
            list_of_inputs.append([x_coordinate, y_coordinate, direction, rover_instructions])

        return list_of_inputs

    @staticmethod
    def x_position(rover_position):
        x_pos = rover_position.split(" ")[0]
        return int(x_pos)

    @staticmethod
    def y_position(rover_position):
        y_pos = rover_position.split(" ")[1]
        return int(y_pos)

    @staticmethod
    def rover_direction(rover_position):
        direction = rover_position.split(" ")[-1]
        return direction

    @staticmethod
    def rover_instruction(instructions):
        instruction = list(instructions)
        return instruction


class Rover:

    def _init_(self, x_max, y_max, x_coordinate=0, y_coordinate=0, direction='N', rover_instructions=[]):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.direction = direction
        self.rover_instructions = rover_instructions
        self.x_max = x_max
        self.y_max = y_max

    def update_rover(self, update_inp):
        self.x_coordinate = update_inp[0]
        self.y_coordinate = update_inp[1]
        self.direction = update_inp[2]
        self.rover_instructions = update_inp[3]

    @staticmethod
    def is_out_of_range(x_cor, y_cor):

        if x_cor > x_max or y_cor > y_max:
            return True
        return False

    @staticmethod
    def is_north(direc):
        if direc == "N":
            return True
        return False

    @staticmethod
    def is_south(direc):
        if direc == "S":
            return True
        return False

    @staticmethod
    def is_east(direc):
        if direc == "E":
            return True
        return False

    @staticmethod
    def is_west(direc):
        if direc == "W":
            return True
        return False

    @staticmethod
    def north(x_cor, y_cor, direc, mov):
        if mov == "M":
            y_cor = y_cor + 1
            x_cor = x_cor
            if is_out_of_range(y_cor, x_cor):
                print("out of range")
                return -1


        elif mov == "L":
            direc = "W"
        elif mov == "R":
            direc = "E"

        return x_cor, y_cor, direc

    @staticmethod
    def east(x_cor, y_cor, direc, mov):
        if mov == "M":
            y_cor = y_cor
            x_cor = x_cor + 1
        elif mov == "L":
            direc = "N"
        elif mov == "R":
            direc = "S"

        return x_cor, y_cor, direc

    @staticmethod
    def west(x_cor, y_cor, direc, mov):
        if mov == "M":
            y_cor = y_cor
            x_cor = x_cor - 1
        elif mov == "L":
            direc = "S"
        elif mov == "R":
            direc = "N"

        return x_cor, y_cor, direc

    @staticmethod
    def south(x_cor, y_cor, direc, mov):
        if mov == "M":
            y_cor = y_cor - 1
            x_cor = x_cor
        elif mov == "L":
            direc = "E"
        elif mov == "R":
            direc = "W"

        return x_cor, y_cor, direc

    def final_coordinates(self):

        for movement in self.rover_instructions:

            if rover.is_north(self.direction):
                self.x_coordinate, self.y_coordinate, self.direction = rover.north(self.x_coordinate, self.y_coordinate,
                                                                                   self.direction, movement)
            elif rover.is_east(self.direction):
                self.x_coordinate, self.y_coordinate, self.direction = rover.east(self.x_coordinate, self.y_coordinate,
                                                                                  self.direction, movement)
            elif rover.is_west(self.direction):
                self.x_coordinate, self.y_coordinate, self.direction = rover.west(self.x_coordinate, self.y_coordinate,
                                                                                  self.direction, movement)
            elif rover.is_south(self.direction):
                self.x_coordinate, self.y_coordinate, self.direction = rover.south(self.x_coordinate, self.y_coordinate,
                                                                                   self.direction, movement)
        print(self.x_coordinate, self.y_coordinate, self.direction)


if __name__ == "__main__":
    plateau_height, plateau_width = InputParser().plat_size()
    list_of_inputs = InputParser().parse_input()
    rover = Rover(plateau_height, plateau_width)

    for inp in list_of_inputs:
        rover.update_rover(inp)
        rover.final_coordinates()

'''
5 5
1 2 N
LMLMLMLMM

'''
