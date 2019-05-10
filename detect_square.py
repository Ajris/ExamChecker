import cv2 as cv
import numpy as np


def angle_cos(p0, p1, p2):
    d1, d2 = (p0 - p1).astype('float'), (p2 - p1).astype('float')
    return abs(np.dot(d1, d2) / np.sqrt(np.dot(d1, d1) * np.dot(d2, d2)))


def find_squares(read_from, save_to, x, y):
    img = cv.imread(read_from, cv.IMREAD_GRAYSCALE)
    retval, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    el = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    img = cv.erode(img, el, iterations=1)
    squares = []
    middles = []
    for gray in cv.split(img):
        for thrs in range(0, 255, 26):
            if thrs == 0:
                bin = cv.Canny(gray, 0, 50, apertureSize=5)
                bin = cv.dilate(bin, None)
            else:
                _retval, bin = cv.threshold(gray, thrs, 255, cv.THRESH_BINARY)
            contours, _hierarchy = cv.findContours(bin, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                cnt_len = cv.arcLength(cnt, True)
                cnt = cv.approxPolyDP(cnt, 0.02 * cnt_len, True)
                if len(cnt) == 4 and 1000 < cv.contourArea(cnt) < 100000 and cv.isContourConvex(cnt):
                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos(cnt[i], cnt[(i + 1) % 4], cnt[(i + 2) % 4]) for i in range(4)])
                    if max_cos < 0.1:
                        m = np.arange(2).reshape(1, 2)
                        m[0] = [(cnt[0][0] + cnt[2][0]) / 2, (cnt[0][1] + cnt[2][1]) / 2]
                        middles.append(m)
                        squares.append(cnt)
    nowe = cv.imread(read_from, cv.IMREAD_ANYCOLOR)
    cv.drawContours(nowe, squares, -1, (0, 255, 0), 3)
    cv.drawContours(nowe, middles, -2, (255, 255, 0), 3)

    # res = []
    # for a in middles:
    #     if a not in res:
    #         print(a)
    #         print("A")
    #         res = np.append(res, a)
    # print(res)
    #88 88 737 88
    #
    for i in x:
        for j in y:
            cv.circle(nowe, (int(i*650/180) + middles[1][0][0]+35, int(j*650/180) + middles[61][0][1]+15), 4, (0, 0, 255), 3)

    cv.imwrite(save_to, nowe)
