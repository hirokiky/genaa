#! -*- coding: utf-8 -*-
def zipped_iter(iter1, iter2):
    iter1_finished = False
    iter2_finished = False

    iter1 = iter(iter1)
    iter2 = iter(iter2)

    while not iter1_finished or not iter2_finished:
        if not iter1_finished:
            try:
                yield next(iter1)
            except StopIteration:
                iter1_finished = True
        if not iter2_finished:
            try:
                yield next(iter2)
            except StopIteration:
                iter2_finished = True
