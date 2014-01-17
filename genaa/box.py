#! -*- coding: utf-8 -*-
from functools import partial

from genaa import multiwidth as genaa_multiwidth


class Box(object):
    min_width = 1
    min_height = 1

    def __init__(self, style, width=None, height=None, align='left', text=''):
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
        self.align = align
        self.text = text

    @property
    def body_width(self):
        if self._width_auto:
            return max(map(genaa_multiwidth.str_width, self.text.split('\n'))) or 1
        else:
            return self._width

    @property
    def body_height(self):
        if self._height_auto:
            return len(self.body_content) or 1
        else:
            return self._height

    @property
    def body_area(self):
        return self.body_width * self.body_height

    @property
    def body_content(self):
        content = self.text.split('\n')
        if self._width_auto:
            return content
        else:
            return sum((list(genaa_multiwidth.chunk_strings(row, self._width))
                        for row in content), [])

    def render(self):
        missed = self.body_height - len(self.body_content)
        height_filled = (self.body_content[:self.body_height] +
                         [self.style.space * self.body_width] * missed)

        align = {'right': lambda row: partial(genaa_multiwidth.rjust, row),
                 'center': lambda row: partial(genaa_multiwidth.center, row),
                 'left': lambda row: partial(genaa_multiwidth.ljust, row)}
        filled = [align.get(self.align, 'left')(row)(self.body_width, self.style.space)
                  for row in height_filled]

        padded = [genaa_multiwidth.center(row, self.body_width+2, self.style.space)
                  for row in filled]

        vertical = self.style.vertical * (self.body_width + 2)
        return '\n'.join(
            [self.style.upperleft + vertical + self.style.upperright] +
            [self.style.horizontal + row + self.style.horizontal for row in padded] +
            [self.style.lowerleft + vertical + self.style.lowerright]
        )


class ASCIIStyle(object):
    space = u' '
    upperleft = u'+'
    upperright = u'+'
    lowerleft = u'+'
    lowerright = u'+'
    vertical = u'-'
    horizontal = u'|'


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


class CCommentStyle(object):
    space = u' '
    upperleft = u'/'
    upperright = u'*'
    lowerleft = u'*'
    lowerright = u'/'
    vertical = u'*'
    horizontal = u'*'


style_mapping = {
    'ascii': ASCIIStyle,
    'simple': SimpleStyle,
    'hash': HashStyle,
    'ccomment': CCommentStyle,
}
