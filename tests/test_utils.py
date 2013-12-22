#! -*- coding: utf-8 -*-
import unittest


class TestChunks(unittest.TestCase):
    def _getTarget(self):
        from genaa.utils import chunks
        return chunks

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test__one_chunk(self):
        actual = self._callFUT('0123', 4)
        self.assertEqual(['0123'], list(actual))

    def test__divided_equally(self):
        actual = self._callFUT('01234567', 4)
        self.assertEqual(['0123', '4567'], list(actual))

    def test__with_a_rest(self):
        actual = self._callFUT('01234', 4)
        self.assertEqual(['0123', '4'], list(actual))
