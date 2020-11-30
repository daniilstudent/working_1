#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    A = [-5, 10, 6, 7, -1, 2, 5, 34, 8, -2]
    a = max(A)
    print("Максимальное число списка: ", a)
sum = 0
for i in A:
    if i > 0:
        sum += i
        print("Сумма положительных элементов массива: ", sum)
del A[1:3]
del A[-3:-1]
A.insert(8, 0)
A.insert(9, 0)
print("Сжатый список: ", A)
