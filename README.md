# Sudoku Generator

Projec 1 built in the context of the Boot.dev curriculum.

## Objective

Put into practice some of the concepts and techniques taught in the [Programming and CS Fundamentals](https://github.com/bootdotdev/curriculum?tab=readme-ov-file#section-1-programming-and-cs-fundamentals).

## Terminology

- **Cluster**: A 3x3 set of numbers, where each number may only appear once.
- **Row**: A 9-cell horizontal set of numbers, where each number may only appear once.
- **Column**: A 9-cell vertical set of numbers, where each number may only appear once.

## Implementation details

- Make a `Group` class to instantiate clusters, rows and columns. It should ensure that numbers are only found once. Each instance must be able to:
  - Add numbers to a list of assigned numbers.
- Render a 9x9 grid, subdivided into three 3x3 clusters.

  ```text
  ┏━━━━━━━┳━━━━━━━┳━━━━━━━┓
  ┃ X X X ┃ X X X ┃ X X X ┃
  ┃ X X X ┃ X X X ┃ X X X ┃
  ┃ X X X ┃ X X X ┃ X X X ┃
  ┣━━━━━━━╋━━━━━━━╋━━━━━━━┫
  ┃ X X X ┃ X X X ┃ X X X ┃
  ┃ X X X ┃ X X X ┃ X X X ┃
  ┃ X X X ┃ X X X ┃ X X X ┃
  ┣━━━━━━━╋━━━━━━━╋━━━━━━━┫
  ┃ X X X ┃ X X X ┃ X X X ┃
  ┃ X X X ┃ X X X ┃ X X X ┃
  ┃ X X X ┃ X X X ┃ X X X ┃
  ┗━━━━━━━┻━━━━━━━┻━━━━━━━┛
  ```

- Each row, column and cluster may only contain a number once.

## Tools used

- Python
  - `Pipenv` for dependency management
