import cv2 as cv
import numpy as np


def angle_cos(p0, p1, p2):
    d1, d2 = (p0 - p1).astype('float'), (p2 - p1).astype('float')
    return abs(np.dot(d1, d2) / np.sqrt(np.dot(d1, d1) * np.dot(d2, d2)))


def find_squares(read_from, save_to, x, y, answer_file):
    f = open(answer_file, 'r')
    contents = f.readline()
    contents = f.readline()
    line = f.readline()
    good_answers = []
    for i in range(len(line)):
        if ord(line[i]) != 10:
            good_answers.append(ord(line[i]) - 48)
    print(good_answers)
    f.close()
    img = cv.imread(read_from, cv.IMREAD_GRAYSCALE)
    retval, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    el = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    img = cv.erode(img, el, iterations=1)
    squares = []
    middles1 = [], []
    middles2 = [], []
    middles3 = [], []
    middles4 = [], []
    width, height = img.shape
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
                        x_mid, y_mid = (cnt[0][0] + cnt[2][0]) / 2, (cnt[0][1] + cnt[2][1]) / 2
                        if x_mid < width / 2 and y_mid < height / 2:
                            middles1[0].append(x_mid)
                            middles1[1].append(y_mid)
                        elif x_mid > width / 2 and y_mid < height / 2:
                            middles2[0].append(x_mid)
                            middles2[1].append(y_mid)
                        elif x_mid < width / 2 and y_mid > height / 2:
                            middles3[0].append(x_mid)
                            middles3[1].append(y_mid)
                        elif x_mid > width / 2 and y_mid > height / 2:
                            middles4[0].append(x_mid)
                            middles4[1].append(y_mid)

                        squares.append(cnt)

    nowe = cv.imread(read_from, cv.IMREAD_ANYCOLOR)
    top_left = sum(middles1[0]) / len(middles1[0]), sum(middles1[1]) / len(middles1[1])
    top_right = sum(middles2[0]) / len(middles2[0]), sum(middles2[1]) / len(middles2[1])

    print(top_left, top_right)
    cv.drawContours(nowe, squares, -1, (0, 255, 0), 3)
    scale = (top_right[0] - top_left[0]) / 165.0
    answers = [-1 for i in range(len(y))]
    print("len")
    print(len(x))
    print(len(y))
    for k in range(len(x)):
        i = x[k]
        for l in range(len(y)):
            j = y[l]
            pos = int(i * scale + np.floor(top_left[0])), int(j * scale + np.floor(top_left[1]))
            cropped = nowe[pos[1]:pos[1] + int(7 * scale), pos[0]: pos[0] + int(7 * scale)]
            avg_color_per_row = np.average(cropped, axis=0)
            avg_colors = np.average(avg_color_per_row, axis=0)
            print(str(good_answers[l]) + " " + str(k))
            if good_answers[l] == k:
                cv.circle(nowe, pos, 4, (0, 255, 0), 3)
            if avg_colors[1] + avg_colors[2] + avg_colors[0] < 550:
                cv.circle(nowe, pos, 4, (0, 0, 255), 3)
                if answers[l] == -1:
                    answers[l] = k


    cv.imwrite(save_to, nowe)
    return answers
