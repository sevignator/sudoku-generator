from flask import Flask, render_template
from app.classes.sudoku_grid import SudokuGrid

app = Flask(__name__)

def generate_grid_css(clusters_per_row, cluster_size):
    return f"""
        <style>
            .sudoku-grid {{
                display: grid;
                grid-template-columns: repeat({clusters_per_row}, 1fr);
                gap: 3px;
                aspect-ratio: 1;
                margin-block: 30px;
                background-color: #000;
                border: solid 3px #000;
                border-radius: 4px;
            }}
            .sudoku-cluster {{
                display: grid;
                grid-template-columns: repeat({cluster_size}, 1fr);
                gap: 2px;
                background-color: #ccc;
            }}
            .sudoku-cell {{
                display: grid;
                place-items: center;
                background-color: #fff;
                font-size: 2rem;
            }}
        </style>
    """


@app.route("/")
def render_grid():
    sudoku_grid = SudokuGrid(3, 3)
    grid_css = generate_grid_css(sudoku_grid.get_clusters_per_row(), sudoku_grid.get_cluster_size())

    return render_template(
        "base.html",
        grid = sudoku_grid.get_grid(),
        grid_css = grid_css,
    )
