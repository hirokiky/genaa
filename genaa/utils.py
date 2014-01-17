#! -*- coding: utf-8 -*-
import math
import os
import unicodedata


def chunks(string, chunk_size):
    """ Partition string by width of each chunks.chunk_size.

    >>> gen_chunks = chunks('0123456789', 4)
    >>> gen_chunks.next()
    '0123'
    >>> gen_chunks.next()
    '4567'
    >>> gen_chunks.next()
    '89'
    >>> gen_chunks.next()
    Traceback (most recent call last):
      ...
    StopIteration
    """
    buf = []
    buf_width = 0
    for c in string:
        char_width = _char_width(c)

        if buf_width + char_width > chunk_size:
            if buf_width < chunk_size:
                # XXX: should I pud buffer with white spaces?
                #buf.extend([' '] * chunk_size - buf_width
                pass

            yield u''.join(buf)
            buf = [c]
            buf_width = char_width
        else:
            buf.append(c)
            buf_width += char_width

    if buf:
        yield u''.join(buf)


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


def str_width(string):
    """Return width of string

    >>> str_width('0123456789')
    10
    >>> str_width(u'あいうえお')
    10
    """
    return sum(_char_width(c) for c in string)


def rjust(string, width, fillchar=' '):
    s_width = str_width(string)
    if s_width > width:
        return string

    f_width = str_width(fillchar)

    return fillchar * int((width - s_width) / f_width) + string


def ljust(string, width, fillchar=' '):
    s_width = str_width(string)
    if s_width > width:
        return string

    f_width = str_width(fillchar)

    return string + fillchar * int((width - s_width) / f_width)


def center(string, width, fillchar=' '):
    s_width = str_width(string)
    if s_width > width:
        return string

    f_width = str_width(fillchar)

    l_fillstr = fillchar * math.floor((width - s_width) / f_width / 2)
    r_fillstr = fillchar * math.ceil((width - s_width) / f_width / 2)
    return l_fillstr + string + r_fillstr


def _char_width(c):
    eaw = unicodedata.east_asian_width(c)

    if eaw in ['F', 'W']:
        char_width = 2

    elif eaw == 'A':
        lang = os.environ.get('LC_ALL', '') or \
            os.environ.get('LC_CTYPE', '') or \
            os.environ.get('LANG', '')

        if lang[:2].lower() in ('ja', 'ko', 'vi', 'zh'):
            char_width = 2
        else:
            char_width = 1

    else:
        char_width = 1

    return char_width
