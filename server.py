from flask import Flask
from app.classes.sudoku_grid import SudokuGrid
from app.functions.utils import retry_until_successful

app = Flask(__name__)
grid = retry_until_successful(lambda: SudokuGrid(3, 3))


@app.route("/")
def get_grid():
    return f"<p>{str(grid.get_grid())}</p>"
