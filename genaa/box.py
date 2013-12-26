#! -*- coding: utf-8 -*-
from textwrap import wrap


class Box(object):
    min_width = 1
    min_height = 1

    def __init__(self, style, width=None, height=None, text=''):
        if width is None:
            self._width_auto = True
        else:
            self._width_auto = False
            self._width = width
            if self.min_width > self._width:
                raise ValueError('Applied width is too small %s (required %s)',
                                 width, self.min_width)

        if height is None:
            self._height_auto = True
        else:
            self._height_auto = False
            self._height = height

            if self.min_height > self._height:
                raise ValueError('Applied height is too small %s (required %s)',
                                 height, self.min_height)

        self.style = style
        self.text = text

    @property
    def body_width(self):
        if self._width_auto:
            return max(map(len, self.text.split('\n'))) or 1
        else:
            return self._width

    @property
    def body_area(self):
        return self.body_width * self.body_height

    @property
    def body_height(self):
        if self._height_auto:
            return len(self.body_content) or 1
        else:
            return self._height

    @property
    def body_content(self):
        return wrap(self.text, self.body_width)

    def render(self):
        missed = self.body_height - len(self.body_content)
        height_filled = (self.body_content[:self.body_height] +
                         [self.style.space * self.body_width] * missed)
        filled = [row.ljust(self.body_width, self.style.space)
                  for row in height_filled]

        vertical = self.style.vertical * self.body_width
        return '\n'.join(
            [self.style.upperleft + vertical + self.style.upperright] +
            [self.style.horizontal + row + self.style.horizontal for row in filled] +
            [self.style.lowerleft + vertical + self.style.lowerright]
        )


class ASCIIStyle(object):
    space = ' '
    upperleft = '+'
    upperright = '+'
    lowerleft = '+'
    lowerright = '+'
    vertical = '-'
    horizontal = '|'


class SimpleStyle(object):
    space = ' '
    upperleft = '┌'
    upperright = '┐'
    lowerleft = '└'
    lowerright = '┘'
    vertical = '─'
    horizontal = '│'


class HashStyle(object):
    space = ' '
    upperleft = '#'
    upperright = '#'
    lowerleft = '#'
    lowerright = '#'
    vertical = '#'
    horizontal = '#'


style_mapping = {
    'ascii': ASCIIStyle,
    'simple': SimpleStyle,
    'hash': HashStyle,
}
