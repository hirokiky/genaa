#! -*- coding: utf-8 -*-
from genaa import utils as genaa_utils


class Box(object):
    min_width = 2
    min_height = 2

    def __init__(self, width, height, border, text=u''):
        if self.min_width > width:
            raise ValueError('Applied width is too small %s (required %s)',
                             width, self.min_width)
        if self.min_height > height:
            raise ValueError('Applied height is too small %s (required %s)',
                             height, self.min_height)
        self.width = width
        self.height = height
        self.border = border
        self.text = text

    @property
    def body_width(self):
        return self.width - 2

    @property
    def body_height(self):
        return self.height - 2

    @property
    def body_area(self):
        return self.body_width * self.body_height

    @property
    def body_content(self):
        return sum((list(genaa_utils.chunks(row, self.body_width))
                    for row in self.text.split('\n')), [])

    def fillup(self, content):
        missed_height = self.body_height - len(content)
        height_filled = content[:self.body_height] + [self.border.space * self.body_width] * missed_height
        return [row.ljust(self.body_width, self.border.space)
                for row in height_filled]

    def render(self):
        body_content = self.fillup(self.body_content)
        vertical = self.border.vertical * self.body_width
        return '\n'.join(
            [self.border.upperleft + vertical + self.border.upperright] +
            [self.border.horizontal + row + self.border.horizontal for row in body_content] +
            [self.border.lowerleft + vertical + self.border.lowerright]
        )


class SimpleBorder(object):
    space = u' '
    upperleft = u'┌'
    upperright = u'┐'
    lowerleft = u'└'
    lowerright = u'┘'
    vertical = u'─'
    horizontal = u'│'
