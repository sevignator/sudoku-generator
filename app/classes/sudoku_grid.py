from random import choice
from app.classes.numset import NumSet


class SudokuGrid:
    def __init__(self):
        self.__grid = None

        # Keep looping until a valid grid has been generated
        while self.__grid == None:
            self.__grid = self.__generate_grid()

    def __generate_grid(self):
        grid_width = 9
        cluster_width = 3
        rows = list(map(lambda _: NumSet(grid_width), range(grid_width)))
        cols = list(map(lambda _: NumSet(grid_width), range(grid_width)))
        grid = []

        for row_index in range(cluster_width):
            sub_row_index = row_index * cluster_width

            for col_index in range(cluster_width):
                sub_col_index = col_index * cluster_width
                cluster_num_set = NumSet(grid_width)
                cluster = []

                for cluster_row_index in range(cluster_width):
                    for cluster_col_index in range(cluster_width):
                        current_col = cluster_col_index + sub_col_index
                        current_row = cluster_row_index + sub_row_index
                        num_sets = {
                            "cluster": cluster_num_set,
                            "row": rows[current_row],
                            "col": cols[current_col],
                        }
                        available_nums = (
                            num_sets["cluster"].get_available_nums()
                            & num_sets["row"].get_available_nums()
                            & num_sets["col"].get_available_nums()
                        )

                        # Exit if there are no more available numbers for a given cell
                        if len(available_nums) == 0:
                            return None

                        random_pick = choice(list(available_nums))

                        num_sets["cluster"].assign_num(random_pick)
                        num_sets["row"].assign_num(random_pick)
                        num_sets["col"].assign_num(random_pick)

                        cluster.append(random_pick)

                grid.append(cluster)

        return grid

    def get_grid(self):
        return self.__grid
