from collections import namedtuple

from genaa.boundinnerclass import BoundInnerClass

Point = namedtuple('Point', 'x y')


class Mapping(object):
    def __init__(self, mapping):
        self.mapping = mapping

    def __iter__(self):
        for y in range(len(self.mapping)):
            for x in range(len(self.mapping[y])):
                yield self.Cell(x, y)

    @BoundInnerClass
    class Cell(object):
        def __init__(self, outer, x, y):
            if not 0 <= y < len(outer.mapping):
                raise ValueError
            if not 0 <= x < len(outer.mapping[y]):
                raise ValueError

            self.outer = outer
            self.coordinate = Point(x, y)

        @property
        def upper(self):
            return self.outer.Cell(self.coordinate.x,
                                   self.coordinate.y-1)

        @property
        def right(self):
            return self.outer.Cell(self.coordinate.x+1,
                                   self.coordinate.y)

        @property
        def lower(self):
            return self.outer.Cell(self.coordinate.x,
                                   self.coordinate.y+1)

        @property
        def left(self):
            return self.outer.Cell(self.coordinate.x-1,
                                   self.coordinate.y)

        @property
        def value(self):
            try:
                return self.outer.mapping[self.coordinate.y][self.coordinate.x]
            except IndexError:
                return None
