import unittest


class TestRenderBlock(unittest.TestCase):
    def _getTarget(self):
        from genaa.block import render_block
        return render_block

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def _createDummyStyle(self):
        class DummyStyle(object):
            space = ' '
            body = 't'
            upperleft = 'g'
            upperright = 'r'
            lowerleft = 'm'
            lowerright = 'v'
            vertical = 'c'
            horizontal = 'h'
            cross = 'n'
        return DummyStyle()

    def test_render__cross(self):
        inp = [
            '* ',
            ' *',
        ]
        expected = '\n'.join([
            'gcr  ',
            'hth  ',
            'mcncr',
            '  hth',
            '  mcv'
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__vertical(self):
        inp = ['**']
        expected = '\n'.join([
            'gcccr',
            'httth',
            'mcccv',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__horizontal(self):
        inp = ['*',
               '*']
        expected = '\n'.join([
            'gcr',
            'hth',
            'hth',
            'hth',
            'mcv',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__lower_left(self):
        inp = ['*',
               '**']
        expected = '\n'.join([
            'gcr  ',
            'hth  ',
            'htmcr',
            'httth',
            'mcccv',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__lower_right(self):
        inp = [' *',
               '**']
        expected = '\n'.join([
            '  gcr',
            '  hth',
            'gcvth',
            'httth',
            'mcccv',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__upper_right(self):
        inp = ['**',
               ' *']
        expected = '\n'.join([
            'gcccr',
            'httth',
            'mcrth',
            '  hth',
            '  mcv',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__upper_left(self):
        inp = ['**',
               '* ']
        expected = '\n'.join([
            'gcccr',
            'httth',
            'htgcv',
            'hth  ',
            'mcv  ',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__body(self):
        inp = ['**',
               '**']
        expected = '\n'.join([
            'gcccr',
            'httth',
            'httth',
            'httth',
            'mcccv',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render__space(self):
        inp = ['  ',
               '  ']
        expected = '\n'.join([
            '     ',
            '     ',
            '     ',
            '     ',
            '     ',
        ])
        actual = self._callFUT(inp, self._createDummyStyle())
        self.assertEqual(expected, actual)

    def test_render(self):
        from genaa.block import ASCIIStyle
        inp = ['** * ** *',
               '**** ****',
               '***   **',
               '** *  **',
               '** *  **']
        expected = '\n'.join([
            '+---+ +-+ +---+ +-+',
            '|   | | | |   | | |',
            '|   +-+ | |   +-+ |',
            '|       | |       |',
            '|     +-+ +-+   +-+',
            '|     |     |   |  ',
            '|   +-+-+   |   |  ',
            '|   | | |   |   |  ',
            '|   | | |   |   |  ',
            '|   | | |   |   |  ',
            '+---+ +-+   +---+  ',
        ])
        actual = self._callFUT(inp, ASCIIStyle())
        self.assertEqual(expected, actual)
