# 🧩 Python Algorithms

A curated collection of foundational Artificial Intelligence (AI) and search algorithms implemented in Python. This repository covers state-space search, graph traversals, informed search, adversarial game search, and classic constraint satisfaction puzzles.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

## 📌 Features

- **Uninformed Graph Search**: Breadth-First Search (`bfs.py`) and Depth-First Search (`dfs.py`) for traversal and shortest path computation.
- **Informed / Heuristic Search**: A* Search algorithm (`astar.py`) utilizing heuristic distance functions via `simpleai`.
- **Adversarial Search**: Alpha-Beta Pruning (`alphabetaprun.py`) for optimizing minimax decision trees.
- **Constraint Satisfaction & Backtracking**: N-Queens problem solver (`nqueens.py`) with visual board representation.
- **State-Space Search**: 3 Water Jugs problem (`3jugs.py`) solved through visited state tracking.
- **Classic Recursion**: Tower of Hanoi (`towerofhanoi.py`) recursive step-by-step puzzle solution.
- **Stochastic Search**: Randomized goal finder (`sample_random_goalfinder.py`) searching arithmetic operations to hit target values.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher installed on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/joeljose/python_algorithms.git
   cd python_algorithms
   ```

2. (Optional) Install external dependencies for A* search:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: All algorithms except `astar.py` use only Python's standard library.*

## 💻 Usage

Run any algorithm directly using Python:

- **Breadth-First Search**:
  ```bash
  python bfs.py
  ```
- **Depth-First Search**:
  ```bash
  python dfs.py
  ```
- **A\* Search**:
  ```bash
  python astar.py
  ```
- **Alpha-Beta Pruning**:
  ```bash
  python alphabetaprun.py
  ```
- **3 Water Jugs Puzzle**:
  ```bash
  python 3jugs.py
  ```
- **N-Queens Solver** *(prompts for board size `n`)*:
  ```bash
  python nqueens.py
  ```
- **Tower of Hanoi** *(prompts for number of disks)*:
  ```bash
  python towerofhanoi.py
  ```
- **Randomized Goal Finder**:
  ```bash
  python sample_random_goalfinder.py
  ```

## 📂 Project Structure

```text
python_algorithms/
├── 3jugs.py                    # 3 Water Jugs state-space search
├── alphabetaprun.py            # Minimax search with Alpha-Beta pruning
├── astar.py                    # A* heuristic search implementation
├── bfs.py                      # Breadth-First Search traversal & shortest path
├── dfs.py                      # Depth-First Search recursive traversal
├── nqueens.py                  # N-Queens backtracking puzzle solver
├── sample_random_goalfinder.py # Randomized arithmetic search solver
├── towerofhanoi.py             # Recursive Tower of Hanoi solver
├── requirements.txt            # Python dependencies (simpleai)
├── LICENSE                     # MIT License
└── README.md                   # Project documentation
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
