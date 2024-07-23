from flask import Flask, render_template
from app.classes.sudoku_grid import SudokuGrid
from app.functions.utils import retry_until_successful

app = Flask(__name__)
sudoku_grid = retry_until_successful(lambda: SudokuGrid(3, 3))


@app.route("/")
def render_grid():
    return render_template("base.html", grid=sudoku_grid.get_grid())
