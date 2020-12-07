import numpy as np
import cv2 as cv
import sys

src = sys.argv[1]
cap = cv.VideoCapture(src)

pos_frame = cap.get(1)
print(pos_frame)

flag, frame = cap.read()
print(frame.shape)
cv.imshow("image", frame)
#cv.waitKey(0)

flag1, frame1 = cap.read()
cv.imshow("nextimage", frame1)
#cv.waitKey(0)

cap.set(1, pos_frame-1)

flag2, frame2 = cap.read()


if np.array_equal(frame2, frame1):
    print("####################################################equal###################################################")