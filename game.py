import random
from classes import NumSet


class SudokuGrid:
    def __init__(self, clusters_per_row, cluster_size):
        self.__clusters_per_row = clusters_per_row
        self.__cluster_size = cluster_size
        self.__cells_per_row = clusters_per_row * cluster_size
        self.__grid = []
        self.__rows = list(
            map(lambda _: NumSet(self.__cells_per_row), range(self.__cells_per_row))
        )
        self.__cols = list(
            map(lambda _: NumSet(self.__cells_per_row), range(self.__cells_per_row))
        )

        self.__generate_grid()

    def __generate_grid(self):
        for row_index in range(self.__clusters_per_row):
            sub_row_index = row_index * self.__cluster_size

            for col_index in range(self.__clusters_per_row):
                sub_col_index = col_index * self.__cluster_size
                cluster_num_set = NumSet(self.__cells_per_row)
                cluster = []

                for cluster_row_index in range(self.__cluster_size):
                    for cluster_col_index in range(self.__cluster_size):
                        current_col = cluster_col_index + sub_col_index
                        current_row = cluster_row_index + sub_row_index
                        num_sets = {
                            "cluster": cluster_num_set,
                            "row": self.__rows[current_row],
                            "col": self.__cols[current_col],
                        }
                        available_nums = (
                            num_sets["cluster"].get_available_nums()
                            & num_sets["row"].get_available_nums()
                            & num_sets["col"].get_available_nums()
                        )

                        if len(available_nums) == 0:
                            raise Exception(
                                "There are no numbers available for this cell."
                            )

                        random_pick = random.choice(list(available_nums))

                        num_sets["cluster"].assign_num(random_pick)
                        num_sets["row"].assign_num(random_pick)
                        num_sets["col"].assign_num(random_pick)

                        cluster.append(random_pick)

                self.__grid.append(cluster)

    def get_grid(self):
        return self.__grid
