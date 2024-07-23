from flask import Flask
from game import SudokuGrid
from utils import retry_until_successful

app = Flask(__name__)
grid = retry_until_successful(lambda: SudokuGrid(3, 3))


@app.route("/")
def get_grid():
    return f"<p>{str(grid.get_grid())}</p>"
