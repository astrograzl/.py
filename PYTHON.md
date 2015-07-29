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
myšlenky, které stojí za filozofií Pythonu si můžeš přečíst po 
zadání následujícího příkazu do jeho interpretu

```python
>>> import this
```


## Skript

Aby jsi nemusela všechny instrukce stále dokola vypisovat do 
interaktivního shellu, můžeš je všechny zapsat do textového souboru s 
příponou `.py` a ten pak interpretu `PYTHON` předat ke spuštění jako 
parametr. V adresáři `scripts` nalezneš krátký skript `reboot.py`. 
Prohlédni si ho, klidně ho i uprav a pokus se pochopit co dělá. Spustit 
ho můžeš příkazem

	$ python reboot.py


### Komentáře

Komentář je pro Python cokoliv za znakem vězení `#` až do konce řádku. 
Python komentáře ignoruje, ale ty by jsi neměla. Právě naopak bys jich 
měla psát co nejvíce, aby jsi se ve svých skriptech vyznala nejen ty i 
po dlouhých letech.


### Typografie

Python používá pro definici funkčních bloků kódu odsazení. Zlatým 
standardem jsou přesně čtyři mezery. Dávej velký pozor, aby jsi 
je používala správně. Každá mezera se počítá.


## Program

Skript psaný v Pythonu lze přirovnat k receptu na chutnou buchtu. Jen 
namísto špinění nádobí importuješ moduly, za ingredience slouží data, 
které chceš zpracovat a celý postup zapisuješ abstraktně a algoritmicky 
tak jak se má provádět. K řízení programu slouží podmínky, cykly, 
funkce a metody objektů. V Pythonu je všechno objekt a metoda je jeho 
vlastní funkce, pomocí niž s ním můžeš manipulovat.


### Modul

Importování modulů je první věcí, kterou při psaní skriptů v Pythonu 
budeš často dělat. Moduly obsahují kód, který napsal někdo jiný a na 
tobě je jen ho správně použít. Mnoho modulů je sdruženo v knihovnách. 
Tou nejzajímavější pro tebe je bezpochyby 
[AstroPy](http://www.astropy.org/). Její použití je přímočaré

```python
>>> import astropy
```

![AstroPy](http://www.astropy.org/images/astropy_banner.svg)

Dalšími, které můžeš shledat užitečnými, jsou knihovny standardně 
používané pro vědecké výpočty a prezentaci jejich výsledků

* [NumPy](http://numpy.org/) pro výpočty s vektory a maticemi
* [SciPy](http://scipy.org/) obsahující nejrůznější vědecké funkce
* [Matplotlib](http://matplotlib.org/) pro kreslení grafů
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

Speciálně pro SymPy je doporučena dvojice příkazů, která připraví 
prostředí pro pohodlné hraní si s ním

```python
>>> from sympy import init_session
>>> init_session()
```


### Proměnné

Proměnné slouží k uchování hodnot, které se časem mohou měnit.

#### Číslo

```python
>>> cislo = 42
```

S čísly, která mohou být i komplexní, můžeš zacházet naprosto přirozeně 
a používat známé algebraické operace. Sčítání `+`, odčítání `-`, 
násobení `*` a dělení `/`. Celočíselné dělení se provádí pomoci `//` a 
zbytek po něm získáš operátorem modulo `%`.

#### Řetězec

```python
>>> slovo = "auto"
```

Jen ty operátory, která mají smysl, se dají použít i na proměnné 
obsahující text. Schválně hádej co bude výsledkem této operace

```python
>>> 3 * slovo + "bus"
```

Další kouzla můžeš s textovým řetězcem provádět pomocí jeho metod. 
Například změnit první písmeno na velké

```python
>>> slovo.title()
```

Seznam všech metod, které jsou pro daný objekt k dispozici ti napoví 
našeptávač v IPython shellu nebo notebooku. Prostě po napsání jména 
objektu a tečky `.`, která se používá jako oddělovač metod, zmáčkni 
klávesu `Tab` a uvidíš

```python
>>> slovo.<Tab>
```

#### Seznam

```python
>>> seznam = ["mleko", "maslo", "vajicka", "mouka"]
```

Seznamy se používají k uchování více hodnot, třeba i různých typů, 
pospolu. K jednotlivým položkám můžeš přistupovat pomocí indexu

```python
>>> seznam[0]
```

#### Entice

```python
>>> entice = (0, 1, 2, 3)
```

Obsah entice nemůžeš měnit. Jak ji jednou vytvoříš, už taková zůstane. 
Stejně jako u seznamu ale můžeš jednotlivé prvky získat pomocí indexu.

#### Slovník

```python
>>> slovnik = {"mleko": 0, "maslo": 1, "vajicka": 10, "mouka": 2}
```

Slovník je speciální seznam, jehož položky jsou pojmenované. Jméno 
slouží jako klíč pro přístup k hodnotám jednotlivých prvků

```python
>>> slovnik["mleko"]
```

Délku všech výčtových typů získáš pomocí funkce `len()`.


### Podmínky

Při rozhodování se uplatňují podmínky, které po vyhodnocení mohou 
nabývat hodnotu `True` nebo `False`. V podmínkách se používají logické 
operátory porovnání

* `<` menší než
* `>` větší než 
* `<=` menší nebo rovno než
* `>=` větší nebo rovno než
* `==` rovná se
* `!=` nerovná se

Podmínky můžeš kombinovat pomocí logických spojek `and` a `or`, 
případně použít slovíčko `not` pro negaci. Přítomnost položky v 
některém z výčtových typů můžeš zjistit slovíčkem `in`.

```python
if podminka1:
	# pokud platí první podmínka
elif podminka2:
	# pokud platí druhá podmínka
else:
	# pokud neplatí ani jedna podmínka
```

### Cykly

Často budeš chtít opakovat nějakou činnost pro každou položku ze 
seznamu

```python
for polozka in seznam:
	if slovnik[polozka] < 1:
		print("Kup prosim {}".format(polozka))
```

Nebo dokud platí nějaká podmínka

```python
while len(seznam) != 0:
	seznam.pop() 
```

### Funkce

Funkce je pojmenovaný kousek kódů, který můžeš opakovaně použít. Funkce 
přijímají vstupní parametry a po provedení požadované operace vracejí 
výstup. Takto může vypadat funkce pro výpočet N-tého členu Fibonacciho 
posloupnosti.

```python
def fibonacci(n):                   # definice funkce
	"""Fibonacciho posloupnost"""   # dokumentace 
	if n < 0:                       # při nesmyslném vstupu 
		return None                 # vrátí nijakou hodnotu
	a, b  = 0, 1                    # první dva členy posloupnosti
	for i in range(n):              # pro i z rozsahu n
		a, b = b, a+b               # výpočet dalšího členu
	return a                        # vrácení konečné hodnoty
```

Použití vlastní funkce je stejné jako všech ostatních

```python
>>> fibonacci(10)
```

Mnoho užitečných matematických funkcí nalezneš taky v modulu `math`.
