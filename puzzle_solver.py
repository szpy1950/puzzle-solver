# puzzle_solver.py

from PIL import Image
import cv2

def solve_puzzle(image_path):
    print("Doing some work")

    img = cv2.imread(image_path)
    cv2.imshow("Image", img)

    display_width = 800
    height, width = img.shape[:2]


    cv2.waitKey(0)
    cv2.destroyAllWindows()

    solution = "This is my solution"

    return solution

