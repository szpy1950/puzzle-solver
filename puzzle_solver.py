# puzzle_solver.py

from PIL import Image
import cv2 as cv,cv2
import numpy as np
import glob

#class PuzzlePiece(self,image):
    # This class stores all necesary details about each piece
    # Store image, corners, contours, etc.
    # Additional methods to rotate and set position

def process_image(path:str):
    image = cv2.imread(path)
    image = cv.resize(image,(1000,1000))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # Manual thresholding
    (T, thresh) = cv2.threshold(blurred, 148, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("Threshold Binary", thresh)
    cv.waitKey(0)

    (T, threshInv) = cv2.threshold(blurred, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cv2.imshow("Threshold", threshInv)
    cv.waitKey(0)
    print("[INFO] otsu's thresholding value: {}".format(T))
     
    return


def detect_pieces(path:str):
    # Identify puzzle pieces on image using edge detection
    # Extract and highlight contours
    return

def segment_pieces(path:str):
    # Segment the image into individual puzzle piece
    # Crop image using the contours
    # Make sure each piece is isolated
    return

def extract_features(piece_path:str):
    # Extract key features from piece such as edges, corner feature and texture patterns
    # Create a puzzle piece object for each piece
    return

def assemble_puzzle():
    # Assemble final picture using puzzle piece edges and corners.
    # Can be done using BFS / DFS
    return

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

if __name__ == '__main__':
    process_image('images/puzzle1.jpg')
    