#! -*- coding: utf-8 -*-
from genaa import utils as genaa_utils


class Box(object):
    min_width = 1
    min_height = 1

    def __init__(self, width, height, style, text=u''):
        if self.min_width > width:
            raise ValueError('Applied width is too small %s (required %s)',
                             width, self.min_width)
        if self.min_height > height:
            raise ValueError('Applied height is too small %s (required %s)',
                             height, self.min_height)
        self.body_width = width
        self.body_height = height
        self.style = style
        self.text = text

    @property
    def body_area(self):
        return self.body_width * self.body_height

    @property
    def body_content(self):
        return sum((list(genaa_utils.chunks(row, self.body_width))
                    for row in self.text.split('\n')), [])

    def fillup(self, content):
        missed = self.body_height - len(content)
        height_filled = content[:self.body_height] + [self.style.space * self.body_width] * missed
        return [row.ljust(self.body_width, self.style.space)
                for row in height_filled]

    def render(self):
        body_content = self.fillup(self.body_content)
        vertical = self.style.vertical * self.body_width
        return '\n'.join(
            [self.style.upperleft + vertical + self.style.upperright] +
            [self.style.horizontal + row + self.style.horizontal for row in body_content] +
            [self.style.lowerleft + vertical + self.style.lowerright]
        )


class SimpleStyle(object):
    space = u' '
    upperleft = u'┌'
    upperright = u'┐'
    lowerleft = u'└'
    lowerright = u'┘'
    vertical = u'─'
    horizontal = u'│'


class HashStyle(object):
    space = u' '
    upperleft = u'#'
    upperright = u'#'
    lowerleft = u'#'
    lowerright = u'#'
    vertical = u'#'
    horizontal = u'#'


style_mapping = {
    'simple': SimpleStyle,
    'hash': HashStyle,
}
