class Plateau:
    def __init__(self, list_of_movements):
        self.list_of_movements = list_of_movements

    def final_coordinates(self):
        for rover in self.list_of_movements:
            x_cor = rover.x_coordinate
            y_cor = rover.y_coordinate
            direc = rover.direction
            ins = rover.rover_instructions

            for movement in ins:

                if rover.is_north(direc):
                    x_cor, y_cor, direc = rover.north(x_cor, y_cor, direc, movement)
                elif rover.is_east(direc):
                    x_cor, y_cor, direc = rover.east(x_cor, y_cor, direc, movement)
                elif rover.is_west(direc):
                    x_cor, y_cor, direc = rover.west(x_cor, y_cor, direc, movement)
                elif rover.is_south(direc):
                    x_cor, y_cor, direc = rover.south(x_cor, y_cor, direc, movement)
            print(x_cor, y_cor, direc)
