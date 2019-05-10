from __future__ import print_function
import sys

PY3 = sys.version_info[0] == 3

if PY3:
    xrange = range

import numpy as np
import cv2 as cv


def angle_cos(p0, p1, p2):
    d1, d2 = (p0 - p1).astype('float'), (p2 - p1).astype('float')
    return abs(np.dot(d1, d2) / np.sqrt(np.dot(d1, d1) * np.dot(d2, d2)))


def find_squares(img):
    img = cv.GaussianBlur(img, (5, 5), 0)
    squares = []
    i=0
    for gray in cv.split(img):
        for thrs in xrange(0, 255, 26):
            _retval, bin = cv.threshold(gray, thrs, 255, cv.THRESH_BINARY)
            contours, _hierarchy = cv.findContours(bin, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                cnt_len = cv.arcLength(cnt, True)
                cnt = cv.approxPolyDP(cnt, 0.02 * cnt_len, True)
                if len(cnt) == 4 and cv.contourArea(cnt) > 1000 and cv.isContourConvex(cnt):

                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos(cnt[i], cnt[(i + 1) % 4], cnt[(i + 2) % 4]) for i in xrange(4)])
                    if max_cos < 0.1:
                        i = i + 1
                        print("==" + str(i))
                        print(cnt)
                        squares.append(cnt)
    return squares

def main():
    img = cv.imread('test.jpg')
    squares = find_squares(img)
    cv.drawContours(img, squares, -1, (0, 0, 0), 3)
    cv.imshow('squares', img)

    cv.waitKey()
    return

if __name__ == '__main__':
    main()
    cv.destroyAllWindows()
