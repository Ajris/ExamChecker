import cv2 as cv


def find_squares(read_from, save_to):
    img = cv.imread(read_from, cv.IMREAD_GRAYSCALE)
    img = cv.GaussianBlur(img, (5, 5), 0)
    retval, img = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
    el = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    img = cv.dilate(img, el, iterations=1)
    squares = []
    contours, _hierarchy = cv.findContours(img, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        cnt_len = cv.arcLength(cnt, True)
        cnt = cv.approxPolyDP(cnt, 0.02 * cnt_len, True)
        if len(cnt) == 4 and 1 < cv.contourArea(cnt) < 200000 and cv.isContourConvex(cnt):
            squares.append(cnt)
    nowe = cv.imread(read_from, cv.IMREAD_ANYCOLOR)
    cv.drawContours(nowe, squares, -1, (0, 255, 255), 3)
    cv.imwrite(save_to, nowe)
