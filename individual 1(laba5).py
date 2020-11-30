#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    A = [2, -4, 5, 6, 8, 9, 10, 12, 22, 4]
    a=max(A)
    A[8] = A[0]
    A[0] = a
    print(A)  