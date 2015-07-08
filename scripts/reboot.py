#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""# Reboot

Klap, klap -- klape déšť na parapet.
A prsty na klávesnici jak kulomet.

V malém bytě vytvářím bity (z) bytí.
Za pár bytů koupím si další pití.

Blik, blik -- blikají lampy za oknem.
Zelený kurzor v okně s telnetem.
"""

from __future__ import print_function

if __name__ == "__main__":
    print("".join([bin(byte) for byte in bytearray(__doc__, "utf-8")]))
