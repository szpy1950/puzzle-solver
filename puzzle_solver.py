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
    img = cv2.imread(path)
    img = cv.resize(img,(1000,1000))
    gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_img, threshold1=50, threshold2=200)

    cv2.imshow("Edges", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

    #_, binary_image = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
    adaptive_thresh = cv2.adaptiveThreshold(gray_img, 
                                       255, 
                                       cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                       cv2.THRESH_BINARY, 
                                       blockSize=11, 
                                       C=2)

    cv2.imshow("Binary", adaptive_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  

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
    