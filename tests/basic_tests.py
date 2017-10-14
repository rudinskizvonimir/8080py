#!/usr/bin/env python
# coding=utf-8
import unittest
from binascii import hexlify
import os

from subprocess import Popen, PIPE


class SimpleRegressionTests(unittest.TestCase):
    """Some simple tests to make sure nothing major breaks while refactoring."""

    def test_no_data_corruption(self):
        with open("data/original_memcpy.rom", 'rb') as original_output:
            original_hex = hexlify(original_output.read())

        x = Popen(['python', '../bin/8080.py', '../examples/memcpy'], stdout=PIPE)
        print(x.stdout.read())
        with open('../examples/memcpy.rom', 'rb') as new_output:
            new_hex = hexlify(new_output.read())
        try:
            assert original_hex == new_hex, "{} != {}".format(original_hex, new_hex)
        finally:
            os.remove('../examples/memcpy.rom')
