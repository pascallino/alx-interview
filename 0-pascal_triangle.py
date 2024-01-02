#!/usr/bin/python3
""" module to compute paascals traingle """


def pascal_triangle(n):
    """ function to return the traingle """
    if n <= 0:
        return []
    tran = []
    for i in range(n):
        if i == 0:
            tran.append([1])
        elif i == 1:
            tran.append([1, 1])
        elif i == 2:
            tran.append([1, 2, 1])
        elif i > 2:
            tran.append([])
            for k in range(len(tran[i - 1])):
                if tran[i - 1][k] == 1:
                    tran[i].append(1)
                if len(tran[i - 1]) > k + 1:
                    if type(tran[i - 1][k + 1]) is int:
                        val = tran[i - 1][k] + tran[i - 1][k + 1]
                        tran[i].append(val)
                    else:
                        continue
    return tran
