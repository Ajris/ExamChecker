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

    def correctContains(self, v):
        return self.correct.__contains__(v)

    def __str__(self):
        return "CORRECT:" + str(self.correct) + "MARKED:" + str(self.marked)


def convert_answer_file(answer_file):
    f = open(answer_file, 'r')
    line = f.readlines()
    good_answers = []
    for i in range(2, len(line)):
        values = line[i].rstrip("\n").split()
        ans = Answer()
        for val in values:
            ans.addCorrect(ord(val) - 48)
        good_answers.append(ans)
    f.close()
    return good_answers
