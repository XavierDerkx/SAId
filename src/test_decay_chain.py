#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test class for DecayChain."""


import unittest

import settings
import decay_chain as dc


class test_DecayChain(unittest.TestCase):
    """Test class for DecayChain."""

    settings.init()

    def test_build_chain(self):
        """Test build_chain."""
        decay_chain = dc.DecayChain(242, 94)

        self.assertEqual(len(decay_chain.chain), 5)
        # First isotope
        self.assertEqual(decay_chain.chain[0][0], 254)
        self.assertEqual(decay_chain.chain[0][1], 100)
        # Second isotope
        self.assertEqual(decay_chain.chain[1][0], 250)
        self.assertEqual(decay_chain.chain[1][1], 98)
        # Third isotope
        self.assertEqual(decay_chain.chain[2][0], 246)
        self.assertEqual(decay_chain.chain[2][1], 96)
        # Fourth isotope
        self.assertEqual(decay_chain.chain[3][0], 242)
        self.assertEqual(decay_chain.chain[3][1], 94)
        # Fith isotope
        self.assertEqual(decay_chain.chain[4][0], 238)
        self.assertEqual(decay_chain.chain[4][1], 92)

    def test_is_in(self):
        """Test is_in."""
        decay_chain = dc.DecayChain(242, 94)
        self.assertTrue(decay_chain.is_in(246, 96))
        self.assertTrue(decay_chain.is_in(238, 92))
        self.assertFalse(decay_chain.is_in(208, 82))


if __name__ == '__main__':
    unittest.main()
