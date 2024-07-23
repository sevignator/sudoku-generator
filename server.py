from flask import Flask, render_template
from app.classes.sudoku_grid import SudokuGrid

app = Flask(__name__)
sudoku_grid = SudokuGrid(3, 3)
grid_css = f"""
<style>
    .sudoku-grid {{
        display: grid;
        grid-template-columns: repeat({sudoku_grid.get_clusters_per_row()}, 1fr);
        max-width: 600px;
        aspect-ratio: 1;
        outline: solid 2px red;
    }}
    .sudoku-cluster {{
        display: grid;
        grid-template-columns: repeat({sudoku_grid.get_cluster_size()}, 1fr);
        outline: solid 1px red;
    }}
    .sudoku-cell {{
        display: grid;
        place-items: center;
        outline: solid 1px;
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
