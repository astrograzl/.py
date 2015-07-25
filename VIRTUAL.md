# Virtuální prostředí

Tato kapitola nebude o použití Pythoního modulu 
[venv](https://docs.python.org/dev/library/venv.html). Koho více zajímá 
samotné vytváření vlastních balíčků pro Python mohu v tuto chvíli 
odkázat na jinou elektronickou příručku psanou v anglickém jazyce
[PyGUG](https://packaging.python.org/).


## PIP

Nové moduly lze do tvojí instalace Pythonu přidávat různými způsoby. 
Doporučenou cestou autorit vývojářské komunity je použití nástroje 
[PIP](https://pypi.python.org/pypi/pip). Pip není třeba instalovat, 
pokud máš dostatečně aktuální verzi Pythonu ve své distribuci. Pip se 
pro instalaci balíčků používá následovně

	$ pip install astropy


## VirtualEnv

Součástí distribuce Pythonu [*Anaconda*](INSTALL.md#Anaconda) je již 
zabudovaná podpora správy virtuálních prostředí. Nové virtuální 
prostředí s Pythonem pro účely bezpečného zkoušení příkazů v této 
příručce vykouzlíš z terminálu zadáním příkazu

	$ conda create -n Salome python

následně ho můžeš aktivovat příkazem

	$ source activate Salome

Měla by jsi si všimnout změny promptu na `(Salome)$`, který značí, že 
se nacházíš právě v tomto virtuálním prostředí. Až tě práce s ním 
omrzí, můžeš ho lehce opustit příkazem

	(Salome)$ source deactivate

Nastal čas vyzkoušet schopnosti tvého notebooku[...](NOTEBOOK.md)
