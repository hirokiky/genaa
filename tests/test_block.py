import unittest


class TestRenderBlock(unittest.TestCase):
    def _getTarget(self):
        from genaa.block import render_block
        return render_block

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def _createDummyStyle(self):
        class DummyStyle(object):
            space = u' '
            body = u't'
            upperleft = u'g'
            upperright = u'r'
            lowerleft = u'm'
            lowerright = u'v'
            vertical = u'c'
            horizontal = u'h'
            cross = u'n'
        return DummyStyle()

    def test_render__cross(self):
        inp = [
            u'* ',
            u' *',
        ]
        expected = '\n'.join([
            u'gcr  ',
            u'hth  ',
            u'mcncr',
            u'  hth',
            u'  mcv'
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__vertical(self):
        inp = [u'**']
        expected = '\n'.join([
            u'gcccr',
            u'httth',
            u'mcccv',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__horizontal(self):
        inp = [u'*',
               u'*']
        expected = '\n'.join([
            u'gcr',
            u'hth',
            u'hth',
            u'hth',
            u'mcv',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__lower_left(self):
        inp = [u'*',
               u'**']
        expected = '\n'.join([
            u'gcr  ',
            u'hth  ',
            u'htmcr',
            u'httth',
            u'mcccv',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__lower_right(self):
        inp = [u' *',
               u'**']
        expected = '\n'.join([
            u'  gcr',
            u'  hth',
            u'gcvth',
            u'httth',
            u'mcccv',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__upper_right(self):
        inp = [u'**',
               u' *']
        expected = '\n'.join([
            u'gcccr',
            u'httth',
            u'mcrth',
            u'  hth',
            u'  mcv',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__upper_left(self):
        inp = [u'**',
               u'* ']
        expected = '\n'.join([
            u'gcccr',
            u'httth',
            u'htgcv',
            u'hth  ',
            u'mcv  ',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__body(self):
        inp = [u'**',
               u'**']
        expected = '\n'.join([
            u'gcccr',
            u'httth',
            u'httth',
            u'httth',
            u'mcccv',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__space(self):
        inp = [u'  ',
               u'  ']
        expected = '\n'.join([
            u'     ',
            u'     ',
            u'     ',
            u'     ',
            u'     ',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render(self):
        from genaa.block import ASCIIStyle
        inp = [u'** * ** *',
               u'**** ****',
               u'***   **',
               u'** *  **',
               u'** *  **']
        expected = '\n'.join([
            u'+---+ +-+ +---+ +-+',
            u'|   | | | |   | | |',
            u'|   +-+ | |   +-+ |',
            u'|       | |       |',
            u'|     +-+ +-+   +-+',
            u'|     |     |   |  ',
            u'|   +-+-+   |   |  ',
            u'|   | | |   |   |  ',
            u'|   | | |   |   |  ',
            u'|   | | |   |   |  ',
            u'+---+ +-+   +---+  ',
        ])
        actual = self._callFUT(inp, ASCIIStyle())
        self.assertEqual(expected, actual)
