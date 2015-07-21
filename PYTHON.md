# Python

> Python je vysokoúrovňový skriptovací programovací jazyk, který v roce
> 1991 navrhl Guido van Rossum. Nabízí dynamickou kontrolu datových 
> typů a podporuje různá programovací paradigmata, včetně objektově 
> orientovaného, imperativního, procedurálního nebo funkcionálního.
> -- [Wiki](https://cs.wikipedia.org/wiki/Python)

Python byl původně navržený jako jazyk pro výuku programování. Proto se 
výborně hodí jako tvůj první programovací jazyk. Říká se, že nejtěžší 
je naučit se právě ten první, neboť to obnáší i nemalou změnu myšlení. 
Ale s Pythonem je naučit se myslet jako počítač snadné. Hlavní 
myšlenky, které stojí za filozofií Pythonu si můžeš prohlédnou po 
zadání následujícího příkazu, do jeho interpretu

```python	
>>> import this
```


## Skripty

Aby jsi nemusela všechny instrukce stále dokola vypisovat do 
interaktivního shellu, můžeš je všechny zapsat do textového souboru s 
příponou `.py` a ten pak interpretu `PYTHON` předat ke spuštění jako 
parametr. V adresáři `scripts` nalezneš krátký skript `reboot.py`. 
Prohlédni si ho, klidně ho i uprav a pokus se pochopit co dělá. Spustit 
ho můžeš příkazem

	$ python reboot.py


## Import

Importování modulů je první věcí, kterou při psaní skriptů v Pythonu 
budeš často dělat. Moduly obsahují kód, který napsal někdo jiný a na 
tobě je jen ho správně použít. Mnoho modulů je sdruženo v knihovnách. 
Tou nejzajímavější pro tebe je bezpochyby 
[AstroPy](http://www.astropy.org/). Její použití je přímočaré

```python
import astropy
```

Dalšími, které můžeš shledat užitečnými, jsou knihovny standardně 
používané pro vědecké výpočty a prezentaci jejich výsledků

* [NumPy](http://numpy.org/) pro výpočty s vektory a maticemi
* [SciPy](http://scipy.org/) obsahující nejrůznější vědecké funkce
* [Matplotlib](http://matplotlib.org/) pro vykreslování grafů
* [SymPy](http://sympy.org/) pro symbolické výpočty
* [Pandas](http://pandas.úydata.org/) pro pohodlnou manipulaci s 
komplexními daty

V mnoha skriptech se můžeš na prvních řádcích shledat s jejich použitím 
následujícím způsobem

```python
import numpy as np
import scipy as sp
import pandas as pd
from matplotlib import pyplot as plt
```
