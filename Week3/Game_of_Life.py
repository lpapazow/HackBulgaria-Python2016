class Cell:
    def __init__(self, is_alive):
        self.is_alive = is_alive
        self.will_live = None
        self.neighbors = []

    def iterate(self):
        self.is_alive = self.will_live
        self.will_live = None

    def set_current_state(self, state):
        self.is_alive = state

    def set_future_state(self, state):
        self.will_live = state

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors

class Matrix:

    NEIGHBORS = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)]

    def __init__(self, length, coordinates):
        self.size = length
        self.cells = []
        self.__initialize_cells()
        self.__fill_living_cells(coordinates)
        self.__set_neighbors()

    def __str__(self):
        res = ""
        for row_idx in range(self.size):
            for col_idx in range(self.size):
                if self.cells[row_idx][col_idx].is_alive:
                    res += "@ "
                else:
                    res += "* "
            res += "\n"
        return res

    def __initialize_cells(self):
        for row_idx in range(self.size):
            row = []
            for col_idx in range(self.size):
                row.append(Cell(False))
            self.cells.append(row)

    def __fill_living_cells(self, coordinates):
        for couple in coordinates:
            self.cells[couple[0]][couple[1]].set_current_state(True)

    def __validate_coordinates(self, at):
        if at[0] < 0 or at[0] >= self.size:
            return False
        if at[1] < 0 or at[1] >= self.size:
            return False
        return True

    def __set_neighbors(self):
        for row_idx in range(self.size):
            for col_idx in range(self.size):
                self.__set_neighbors_at([row_idx, col_idx])

    def __set_neighbors_at(self, at):
        neighbors = []
        for position in self.NEIGHBORS:
            position = (at[0] + position[0], at[1] + position[1])

            if self.__validate_coordinates(position):
                neighbors.append(position)
        self.cells[at[0]][at[1]].set_neighbors(neighbors)

    def __count_living_neighbors(self, at):
        neighbors = self.cells[at[0]][at[1]].neighbors
        alive_neigbors = 0
        for neighbor in neighbors:
            if self.cells[neighbor[0]][neighbor[1]].is_alive:
                alive_neigbors += 1
        return alive_neigbors

    def __decide_if_lives(self, at):
        neighbors_count = self.__count_living_neighbors(at)
        if self.cells[at[0]][at[1]].is_alive:
            if neighbors_count == 2 or neighbors_count == 3:
                self.cells[at[0]][at[1]].will_live = True
            else:
                self.cells[at[0]][at[1]].will_live = False
        else:
            if neighbors_count == 3:
                self.cells[at[0]][at[1]].will_live = True
            else:
                self.cells[at[0]][at[1]].will_live = False

    def iterate_matrix(self):
        for row_idx in range(self.size):
            for col_idx in range(self.size):
                self.__decide_if_lives([row_idx, col_idx])

        for row_idx in range(self.size):
            for col_idx in range(self.size):
                self.cells[row_idx][col_idx].iterate()

    def print_cell_state(self, row, col):
        print(self.cells[row][col].is_alive)


def main():
    import os
    import time

    board = Matrix(10, [[6, 5], [7, 5], [8, 5], [5, 6], [6, 6], [7, 6]])

    while True:
        os.system('clear')
        print(board)
        time.sleep(1)
        board.iterate_matrix()


if __name__ == "__main__":
    main()

