#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SAId script.

SAId (Serial Alpha Identifer) is a python script to generate alpha decays,
chains for a given isotope (A, atomic mass and Z, atomic number).
"""

__author__ = "Xavier Derkx"
__copyright__ = "Copyright 2024"
__credits__ = ["Xavier Derkx"]
__license__ = "CeCILL 2.1"
__version__ = "0.1"
__maintainer__ = "Xavier Derkx"
__email__ = "[email protected]"
__status__ = "Proof of concept"

import sys

import settings
from decay_chain import DecayChain


def main():
    """Call the main function."""
    if len(sys.argv) != 3:
        print("Please provide a mass (A) and an atomic number (Z)")
        exit()
    else:
        try:
            A = int(sys.argv[1])
            Z = int(sys.argv[2])
        except:
            # TODO custom exception
            print("The mass (A) and the atomic number (Z) need to be integers")
            exit()

        settings.init()
        # decays = settings.get_decays(A, Z)
        tmp = DecayChain(A, Z)
        tmp.print()


if __name__ == "__main__":
    main()
