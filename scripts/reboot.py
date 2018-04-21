#!python
# coding: utf-8
"""# Reboot

Klap, klap -- klape déšť na parapet.
A prsty na klávesnici jak kulomet.

V malém bytě vytvářím bity (z) bytí.
Za pár bajtů koupím si další pití.

Blik, blik -- blikají lampy za oknem.
Zelený kurzor v okně s telnetem.
"""


for byte in bytearray(__doc__, 'utf-8'):
    print(bin(byte), end="")
print(".")
