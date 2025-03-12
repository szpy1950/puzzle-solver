"""import cv2
import numpy as np
import glob

CHECKERBOARD = (6,9)
images = glob.glob('images/calibration/*.jpg')
print(images)

for fname in images:
    img = cv2.imread(fname)
    img = cv2.resize(img,(int(400),int(400)))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH+cv2.CALIB_CB_FAST_CHECK+cv2.CALIB_CB_NORMALIZE_IMAGE)
    print(corners)

    corners = np.int_(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(img,(x,y),3,(0,0,255),-1)

    cv2.imshow('Corners',img)

    cv2.waitKey(0)"""

"""
--------------------------------------------------  Calibration -----------------------------------------------------------------
"""

import numpy as np
import cv2 as cv,cv2
import glob

# Insert number of rows and columns of checkerboard model in CHECKERBOARD
CHECKERBOARD = (6,9)
 
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
 
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:6,0:9].T.reshape(-1,2)
 
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('images/calibration/*.jpg')
print(images)
 
for fname in images:
    img = cv.imread(fname)
    img = cv2.resize(img,(400,400))
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
 
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray,CHECKERBOARD,None)
    print(ret)
 
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
 
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        cv.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(0)
 
cv.destroyAllWindows()

# Get camera matrix, distortion coefficients, rotation and translation vectors
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print(mtx)

img = cv.imread('images/calibration/3PF7XMPh.jpg')
h,  w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

# undistort
dst = cv.undistort(img, mtx, dist, None, newcameramtx)
cv.imwrite('calibresult.png', dst)
