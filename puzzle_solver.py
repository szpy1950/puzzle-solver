# puzzle_solver.py

from PIL import Image
import cv2

class PuzzlePiece(self,image):
    # This class stores all necesary details about each piece
    # Store image, corners, contours, etc.
    # Additional methods to rotate and set position

def process_image(path:str):
    img = cv2.imread(path)
    # apply grayscale and binarization on picture
    # copy modified picture into new directory

def detect_pieces(path:str):
    # Identify puzzle pieces on image using edge detection
    # Extract and highlight contours

def segment_pieces(path:str):
    # Segment the image into individual puzzle piece
    # Crop image using the contours
    # Make sure each piece is isolated

def extract_features(piece_path:str):
    # Extract key features from piece such as edges, corner feature and texture patterns
    # Create a puzzle piece object for each piece

def assemble_puzzle():
    # Assemble final picture using puzzle piece edges and corners.
    # Can be done using BFS / DFS

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

