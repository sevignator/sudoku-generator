from flask import Flask, render_template
from app.classes.sudoku_grid import SudokuGrid

app = Flask(__name__)
sudoku_grid = SudokuGrid(3, 3)
clusters_per_row = sudoku_grid.get_clusters_per_row()
cluster_size = sudoku_grid.get_cluster_size()
grid_css = f"""
<style>
    .sudoku-grid {{
        display: grid;
        grid-template-columns: repeat({clusters_per_row}, 1fr);
    }}
    .sudoku-cluster {{
        display: grid;
        grid-template-columns: repeat({cluster_size}, 1fr);
    }}
</style>
"""


@app.route("/")
def render_grid():
    return render_template(
        "base.html",
        grid = sudoku_grid.get_grid(),
        grid_css = grid_css,
    )
