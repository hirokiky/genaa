#! -*- coding: utf-8 -*-
import unittest


class TestZippedIter(unittest.TestCase):
    def _getTarget(self):
        from genaa.utils import zipped_iter
        return zipped_iter

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test__longer_iter2(self):
        actual = self._callFUT([0]*3,
                               [1]*5)
        expceted = [0, 1, 0, 1, 0, 1, 1, 1]
        self.assertEqual(expceted, list(actual))

    def test__longer_iter1(self):
        actual = self._callFUT([0]*5,
                               [1]*3)
        expceted = [0, 1, 0, 1, 0, 1, 0, 0]
        self.assertEqual(expceted, list(actual))

    def test__same_length(self):
        actual = self._callFUT([0]*3,
                               [1]*3)
        expceted = [0, 1, 0, 1, 0, 1]
        self.assertEqual(expceted, list(actual))

    def test__with_string(self):
        actual = self._callFUT('aaa',
                               'bbbb')
        expceted = ['a', 'b', 'a', 'b', 'a', 'b', 'b']
        self.assertEqual(expceted, list(actual))
