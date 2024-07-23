import random
from utils import retry_until_successful
from classes import NumSet


def main():
    grid = retry_until_successful(lambda: generate_grid(3, 3))
    print(grid)


def generate_grid(clusters_per_row, cluster_size):
    cells_per_row = clusters_per_row * cluster_size
    grid = []
    rows = list(map(lambda _: NumSet(cells_per_row), range(cells_per_row)))
    cols = list(map(lambda _: NumSet(cells_per_row), range(cells_per_row)))

    for row_index in range(clusters_per_row):
        sub_row_index = row_index * cluster_size

        for col_index in range(clusters_per_row):
            sub_col_index = col_index * cluster_size
            cluster_num_set = NumSet(cells_per_row)
            cluster = []

            for cluster_row_index in range(cluster_size):
                for cluster_col_index in range(cluster_size):
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

                    if len(available_nums) == 0:
                        raise Exception("There are no numbers available for this cell.")

                    random_pick = random.choice(list(available_nums))

                    num_sets["cluster"].assign_num(random_pick)
                    num_sets["row"].assign_num(random_pick)
                    num_sets["col"].assign_num(random_pick)

                    cluster.append(random_pick)

            grid.append(cluster)

    return grid


main()
