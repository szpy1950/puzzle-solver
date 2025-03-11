# main.py

from puzzle_solver import solve_puzzle

def main():
    puzzle_image = "images/puzzle1.jpg"

    result = solve_puzzle(puzzle_image)

    print("End of puzzle solving", result)

if __name__ == "__main__":
    main()