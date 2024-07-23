from flask import Flask
from game import generate_grid
from utils import retry_until_successful

app = Flask(__name__)
grid = retry_until_successful(lambda: generate_grid(3, 3))


@app.route("/")
def get_grid():
    return f"<p>{str(grid)}</p>"
