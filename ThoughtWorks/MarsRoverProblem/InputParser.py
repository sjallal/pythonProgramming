from ThoughtWorks.MarsRoverProblem.Rover import Rover


class InputParser:

    def parse_input(self):
        list_of_movements = []
        x_max, y_max = map(int, input().split())
        while True:
            rover_position = input()
            instructions = input()
            if not rover_position and not instructions:
                break
            x_coordinate = InputParser.x_position(rover_position)
            y_coordinate = InputParser.y_position(rover_position)
            direction = InputParser.rover_direction(rover_position)
            rover_instructions = InputParser.rover_instruction(instructions)
            list_of_movements.append(Rover(x_coordinate, y_coordinate, direction, rover_instructions))
        return list_of_movements

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
