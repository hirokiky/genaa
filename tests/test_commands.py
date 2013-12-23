#! -*- coding: utf-8 -*-
import subprocess
import unittest


class TestBoxCommand(unittest.TestCase):
    def _callSUT(self, input=None):
        p = subprocess.Popen(['genaa', 'box'],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        return p.communicate(input)

    def test__without_input(self):
        out, err = self._callSUT()
        self.assertEqual(b'', err, msg=err.decode('utf-8'))
        self.assertEqual('''\
┌───┐
│   │
│   │
│   │
└───┘
'''.encode('utf-8'), out)

    def test__with_input(self):
        out, err = self._callSUT(b'mio')
        self.assertEqual(b'', err, msg=err.decode('utf-8'))
        self.assertEqual('''\
┌───┐
│mio│
│   │
│   │
└───┘
'''.encode('utf-8'), out)
