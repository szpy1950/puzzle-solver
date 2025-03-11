# puzzle_solver.py

from PIL import Image
import cv2

def process_image(path:str):
    img = cv2.imread(path)
    # apply grayscale and binarization on picture
    # copy modified picture into new directory

def detect_pieces(path:str):
    # Extract jigsaw pieces from processed image
    # Save all pieces into a new directory

def identify_pieces(path:str):
    # For each piece, create a new puzzle piece object
    # Each puzzle piece 

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

