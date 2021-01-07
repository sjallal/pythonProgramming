from ThoughtWorks.MarsRoverProblem.Rover import Rover


class InputParser:
    x_max = 0
    y_max = 0
    x_coordinate = 0
    y_coordinate = 0
    direction = ''
    rover_instructions = []

    @classmethod
    def parse_plateau_size(cls):
        cls.x_max, cls.y_max = map(int, input().split())
        return cls.x_max, cls.y_max

    # @classmethod
    # def get_plateau_size(cls):
    #     return cls.x_max, cls.y_max

    @classmethod
    def parse_list_of_rovers(cls):
        list_of_rovers = []
        while True:
            rover_position = input()
            instructions = input()
            if not rover_position and not instructions:
                break
            cls.x_coordinate = InputParser.x_position(rover_position)
            cls.y_coordinate = InputParser.y_position(rover_position)
            cls.direction = InputParser.rover_direction(rover_position)
            cls.rover_instructions = InputParser.rover_instruction(instructions)
            list_of_rovers.append(Rover(cls.x_coordinate, cls.y_coordinate, cls.direction, cls.rover_instructions))
        return list_of_rovers

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
