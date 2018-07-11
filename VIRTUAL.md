# Virtuální prostředí

Při hraní si s více nápady najednou je dobré si udržet pořádek v jejich závislostech. K tomuto účelu slouží virtuální prostředí. Můžeš si ho představit jako kreativní šuplík u stolu, nebo krabici ve skříni či na polici, kde schraňuješ všechny potřebné věci (nůžky, tužky, pastelky, drátky, lepidlo, útržky balících papírů, kousky provázků a podobné užitečnosti), které potřebuješ ke svému kratochvilnému koníčku.


## Projekty

Když budeš za projekt uvažovat adresář na Ploše ve své Domovské složce uživatelky, ale klidně i kdekoliv jinde, třeba na flashče ztracené v parku pod jabloní, s ním spojené nové virtuální prostředí vytvoříš příkazem

	$ python -m venv Salome

načež vznikne onen prostor pro tvou hravou fantazii s minimálním dopadem na okolní systém, který můžeš následně aktivovat příkazem

	$ source Salome/bin/activate

To je jedna možnost a ještě elegantněji lze brilantnějšího výsledku dosáhnout s trojicí zaklínadel

	$ conda create -n Salome
	$ conda activate Salome
	$ conda deactivate


## PIP

Nové moduly lze do tvojí instalace Pythonu přidávat různými způsoby.
Doporučenou cestou autorit vývojářské komunity je použití nástroje
[PIP](https://pypi.python.org/pypi/pip). Pip není třeba instalovat,
pokud máš dostatečně aktuální verzi Pythonu ve své distribuci. Pip se
pro instalaci balíčků používá následovně

	(Salome)$ pip install astropy

<!-- Ve windows by to mělo být stejné, snad jen bez toho `source`, které lze v
Linuxu zaměnit za pouhé `.` -->

Nastal čas vyzkoušet schopnosti tvého notebooku[...](NOTEBOOK.md)
