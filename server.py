from flask import Flask, render_template
from app.classes.sudoku_grid import SudokuGrid

app = Flask(__name__)


@app.route("/")
def render_page():
    sudoku_grid = SudokuGrid()

    return render_template("base.html", grid=sudoku_grid.get_grid())
