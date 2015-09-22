# Virtuální prostředí

Při hraní si s více projekty najednou je dobré si udržet pořádek v 
jejich závislostech na jednotlivých modulech. K tomuto účelu slouží 
virtuální prostředí pro Python poskytované balíčkem 
[Virtualenv](https://virtualenv.pypa.io/). Ten umožňuje vytvářet 
vzájemně se neovlivňující izolované prostředí. Jeho nadstavba 
[Virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/) pak 
ještě více zpříjemňuje práci s nimi. Proto si jej hned nainstaluj

	$ sudo dnf install python-virtualenvwrapper
	
Prvotní konfigurace obnáší přidání tři řádek do tvého souboru 
`~/.bashrc`. První nastaví proměnnou, která určuje, kde se nové 
virtuální prostředí budou ukládat. Druhý řádek nastavuje proměnnou s 
cestou k tvým projektům na Ploše. Třetí pak aktivuje samotný wrapper.

	$ echo 'export WORKON_HOME=$HOME/.virtualenvs/' >> ~/.bashrc
	$ echo 'export PROJECT_HOME=$HOME/Plocha/' >> ~/.bashrc
	$ echo 'source /usr/bin/virtualenvwrapper.sh' >> ~/.bashrc

Nejednoduší co teď můžeš udělat, aby se právě provedené změny 
ihned projevily, je zavřít a znovu otevřít okno Terminálu.


## Projekty

Když budeš za projekt uvažovat adresář na Ploše a s ním spojené 
virtuální prostředí, tak nový vytvoříš příkazem

	$ mkproject Salome

Všimni si změny promptu na `(Salome)$ `, ten značí, v kterém virtuálním 
prostředí se právě nacházíš. Přepínat mezi nimi, nebo jen zobrazit 
jejich seznam, můžeš příkazem

	$ workon

Až tě hraní si s ním omrzí, můžeš ho opustit příkazem

	(Salome)$ deactivate

a na dobro smazat, pokud jsi si jista, že už jej víckát nebudeš 
potřebovat

	$ rmvirtualenv Salome


## PIP

Nové moduly lze do tvojí instalace Pythonu přidávat různými způsoby. 
Doporučenou cestou autorit vývojářské komunity je použití nástroje 
[PIP](https://pypi.python.org/pypi/pip). Pip není třeba instalovat, 
pokud máš dostatečně aktuální verzi Pythonu ve své distribuci. Pip se 
pro instalaci balíčků používá následovně

	(Salome)$ pip install astropy


Nastal čas vyzkoušet schopnosti tvého notebooku[...](NOTEBOOK.md)
