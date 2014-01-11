def chunks(seq, chunk_size):
    """ Partition sequence by size of each chunks.chunk_size.

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
    for i in range(0, len(seq), chunk_size):
        yield seq[i:i+chunk_size]


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
