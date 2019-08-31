from typing import List

from com.wk.exercise.leetCode.Q import Q


class Q977(Q):

    def answer(self):

        pass

    def sortedSquares(self, A: List[int]):
        a = [-4, -1, 0, 3, 10]
        b = []
        for i in a:
            b.append(i ** 2)
        i = 0
        while i < len(b):
            for j in range(i + 1, len(b)):
                if b[i] > b[j]:
                    b[i], b[j] = b[j], b[i]
            i += 1
        print(b)
