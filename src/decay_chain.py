#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A class to represent a decay chain."""

from collections import deque

import settings


class DecayChain():
    """
    A class to represent a decay chain.

    ...

    Attributes
    ----------
    _A: int
        atomic mass of the seed of the decay chain
    _Z : int
        atomic number of the seed of the decay chain
    chain : deque
        decay chain
    Methods
    -------
    build_chain():
        Populate the decay chain from both ends
    is_in(A: int, Z: int) -> bool:
        Check if an isotope belongs to the chain
    print():
        Print the decay hierarchy
    draw():
        Draw the decay hierarchy
    """

    def __init__(self, atomic_mass: int, atomic_number: int):
        """Construct the DecayChain object."""
        self._A = atomic_mass
        self._Z = atomic_number
        self.chain = deque()
        self.build_chain()

    def build_chain(self):
        """Populate the decay chain from both ends."""
        # Searching for children, if any
        tmpA = self._A
        tmpZ = self._Z
        while True:
            decays = settings.get_decays(tmpA, tmpZ)

            if decays:
                self.chain.append([tmpA, tmpZ, decays])
                tmpA -= 4
                tmpZ -= 2
            else:
                break

        # Searching for parents, if any
        tmpA = self._A+4
        tmpZ = self._Z+2
        while True:
            decays = settings.get_decays(tmpA, tmpZ)
            if decays:
                self.chain.appendleft([tmpA, tmpZ, decays])
                tmpA += 4
                tmpZ += 2
            else:
                break

    def is_in(self, A: int, Z: int) -> bool:
        """Check if an isotope belongs to the chain."""
        for d in self.chain:
            if d[0] == A and d[1] == Z:
                return True
        return False

    def print(self):
        """Print the decay chain."""
        i = 0
        for c in self.chain:
            print("="*80)
            print(" "*4*i, end=" ")
            print(f" {c[0]} / {c[1]} :")
            for d in c[2]:
                print("-"*80)
                print(" "*(4*i+2), end=" ")
                msg = (f"Intensity: {d['I']}% "+f"- Energy: {d['E']} MeV "
                       + f"- Half-life: {d['HL']} s")
                print(msg)
            i += 1

    def draw(self):
        """Draw the decay chain."""
        # TODO: implement drawing the decay chain, using GraphViz?
        pass
