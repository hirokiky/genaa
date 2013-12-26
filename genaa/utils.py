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
