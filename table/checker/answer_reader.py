class Answer:
    marked = []
    correct = []

    def __init__(self):
        self.marked = []
        self.correct = []

    def addCorrect(self, v):
        self.correct.append(v)

    def addMarked(self, v):
        self.marked.append(v)

    def calcPoints(self):
        self.correct.sort()
        self.marked.sort()
        res = 0
        for i in self.correct:
            if self.marked.__contains__(i):
                res = res + 1
            else:
                res = res - 1
        return res

    def __str__(self):
        return "CORRECT:" + str(self.correct) + "MARKED:" + str(self.marked)


def f1():
    f = open("/home/ajris/PycharmProjects/examChecker/.data/ans/newans5x16.txt", 'r')
    line = f.readlines()
    good_answers = []
    for i in range(2, len(line)):
        values = line[i].rstrip("\n").split()
        ans = Answer()
        for val in values:
            ans.addCorrect(ord(val) - 48)
        good_answers.append(ans)
    print(good_answers[1])
    f.close()
    return


if __name__ == '__main__':
    f1()
