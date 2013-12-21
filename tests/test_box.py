#! -*- coding:utf-8 -*-
import unittest


class TestRender(unittest.TestCase):
    def _getTarget(self):
        from genaa.box import Box
        return Box

    def _makeOne(self):
        class DummyBorder(object):
            space = u' '
            upperleft = u'g'
            upperright = u'r'
            lowerleft = u'm'
            lowerright = u'v'
            vertical = u'c'
            horizontal = u'h'

        return self._getTarget()(4, 4, DummyBorder())

    def test__4_x_4(self):
        actual = self._makeOne().render()
        expected = u"""\
gccr
h  h
h  h
mccv\
"""
        self.assertEqual(expected, actual)
