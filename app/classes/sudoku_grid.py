import random
from app.classes.numset import NumSet


class SudokuGrid:
    def __init__(self, clusters_per_row, cluster_size):
        self.__clusters_per_row = clusters_per_row
        self.__cluster_size = cluster_size
        self.__grid = self.__generate_grid()

    def __generate_grid(self):
        cells_per_row = self.__clusters_per_row * self.__cluster_size
        rows = list(
            map(lambda _: NumSet(cells_per_row), range(cells_per_row))
        )
        cols = list(
            map(lambda _: NumSet(cells_per_row), range(cells_per_row))
        )
        grid = []

        for row_index in range(self.__clusters_per_row):
            sub_row_index = row_index * self.__cluster_size

            for col_index in range(self.__clusters_per_row):
                sub_col_index = col_index * self.__cluster_size
                cluster_num_set = NumSet(cells_per_row)
                cluster = []

                for cluster_row_index in range(self.__cluster_size):
                    for cluster_col_index in range(self.__cluster_size):
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

                        # Restart the grid generation in the odd case that
                        # there are no available numbers left for a given cell
                        if len(available_nums) == 0:
                            return self.__generate_grid()

                        random_pick = random.choice(list(available_nums))

                        num_sets["cluster"].assign_num(random_pick)
                        num_sets["row"].assign_num(random_pick)
                        num_sets["col"].assign_num(random_pick)

                        cluster.append(random_pick)

                grid.append(cluster)

        return grid

    def get_clusters_per_row(self):
        return self.__clusters_per_row

    def get_cluster_size(self):
        return self.__cluster_size

    def get_grid(self):
        return self.__grid
