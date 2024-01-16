#!/usr/bin/python3
""" In a text file, there is a single character H
Your text editor can execute only two operations in this file: Copy
All and Paste . Given a number n ,
write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file."""


def calculate_factors(number):
    """ calculate factors of n-0. Minimum Operations  """
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def is_prime(number):
    """calculate prime number 0. Minimum Operations"""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def minOperations(n):
    """ 0. Minimum Operations """
    copy = 1
    getindex = 0
    numcp = 0
    div = 0
    op_list = []
    if not n:
        return 0
    if is_prime(n):
        return n
    if n <= 1 or not (type(n) is int):
        return 0
    factor = calculate_factors(n)
    for i, value in enumerate(factor):
        if i < getindex:
            continue
        if (factor[i] + factor[i] in factor and i != 0):
            getindex = factor.index(factor[i] + factor[i])
            copy = factor[i]
            op_list.append('Copy All')
            op_list.append('Paste')
            i = getindex
        elif ((i + 1) < len(factor) and factor[i + 1] == n):
            op_list.append('Copy All')
            copy = factor[i]
            div = int(factor[i + 1]/factor[i]) - 1
            for k in range(div):
                op_list.append('Paste')
            return len(op_list)
        elif i == 0 and i + 1 < len(factor):
            op_list.append('Copy All')
            copy = 1
            for k in range(factor[i + 1] - factor[i]):
                op_list.append('paste')
        elif i + 1 < len(factor):
            numcp = factor[i]
            for k in range(n):
                numcp = numcp + copy
                op_list.append('paste')
                if numcp > n:
                    return 0
                if numcp in factor:
                    getindex = factor.index(numcp)
                    break
    return (len(op_list))
