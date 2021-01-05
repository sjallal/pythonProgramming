class Rover:
    def __init__(self, x_coordinate, y_coordinate, direction, rover_instructions):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.direction = direction
        self.rover_instructions = rover_instructions

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
