#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Příručka moderní astrofyzičky"""

import webbrowser
import qrcode


url = "http://astrograzl.gitbooks.io/salome/"


def qrme(data):
    """Ukaž mi QR kód pro tyto data"""
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make()
    qr.print_ascii()
    return


if __name__ == "__main__":
    qrme(url)
    print("    Příručka moderní astrofyzičky\n")
    print("Chceš si prohlédnout příručku online?\n«{}»".format(url))
    print("Ano nebo ne? ", end="")
    ans = input()
    if ans == "Ano":
        print("Tak jdeme na to...")
        webbrowser.open(url)
    elif ans == "ne":
        print("Dobře, jak chceš.")
        pass
    else:
        print("Správná odpověď je buď «Ano» nebo «ne»!")
        print("Ale můžeš to zkusit znovu ;-)")
