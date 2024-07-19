import random


class NumSet:
    def __init__(self):
        self.available_nums = set(range(cluster_size * cluster_size))
        self.assigned_nums = []

    def assign_num(self, num):
        self.available_nums.remove(num)
        self.assigned_nums.append(num)

    def get_available_nums(self):
        return self.available_nums


clusters_per_row = 2
cluster_size = 2

grid = []
rows = [NumSet()] * (clusters_per_row**2)
cols = [NumSet()] * (clusters_per_row**2)


for row_index in range(clusters_per_row):
    sub_row_index = row_index * cluster_size

    for col_index in range(clusters_per_row):
        sub_col_index = col_index * cluster_size
        cluster = []

        for cluster_row_index in range(cluster_size):
            for cluster_col_index in range(cluster_size):
                coords = {
                    "x": cluster_row_index + sub_row_index,
                    "y": cluster_col_index + sub_col_index,
                }
                num_sets = {
                    "cluster": NumSet(),
                    "row": rows[coords["x"]],
                    "col": cols[coords["y"]],
                }
                available_nums = (
                    num_sets["cluster"].get_available_nums()
                    & num_sets["row"].get_available_nums()
                    & num_sets["col"].get_available_nums()
                )
                random_pick = random.choice(list(available_nums))

                print(coords)

                cluster.append(random_pick)

        grid.append(cluster)


print(grid)
