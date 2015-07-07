# Instalace

Ačkoliv je tato příručka dostupná on-line, na adrese 
<http://astrograzl.gitbooks.io/salome/>, je výhodné si stáhnout i její 
zdrojové kódy z repozitáře <https://github.com/astrograzl/salome/>. 
Tím, kromě vlastní kopie, získáš i možnost zkoumat jak byla tvořena. A 
můžeš mi posílat návrhy na vylepšení, aby více odpovídala tvojím 
představám. Ale hlavně se tím i něco nového naučíš.


## Stažení

Repozitář se zdrojovým kódem získáš pomocí nástroje Git zadáním 
následujícího příkazu do okna terminálu.

	$ git clone https://github.com/astrograzl/Salome.git

Že žádný Git nemáš a o nějakém terminálu jsi v životě neslyšela vůbec 
nevadí. Celá příručka je sice plná odborných termínů okolo počítačů, 
ale se slovníčkem na konci se s nimi jistě brzo zkamarádíš.


## Linux

Jsi-li hravá a ráda se učíš novým kouzlům, měla by sis nainstalovat 
Linux na svůj osobní počítač. Pokud si na to sama netroufáš, najdi si 
mě v kabinetě, nebo popros někoho jiného. O Windows ani svoje data se 
bát nemusíš.

Budu předpokládat, že jsi si vybrala [Fedoru](https://getfedora.org), 
což vůbec není špatná volba, neboť modrá ti sluší. V jiné distribuci 
bude příkaz pro instalaci programů jiný i názvy balíčků se mohou lišit.


## Git

Distribuovaný systém správy verzí [Git](https://git-scm.org) slouží k 
ukládání a sdílení zdrojového kódu, včetně historie jeho změn. S Gitem 
už nikdy znovu nepřijdeš o svou bakalářku nebo diplomku ani pár dní 
před jejím odevzdáním.

Takže si otevři okno terminálu a napiš do něj tento příkaz:

	$ sudo yum install git

a zmáčkni Enter. Zadej svoje heslo pro ověření, že jsi to skutečně ty 
a ani nemusíš zadržovat dech, je-li to pro tebe poprvé. Jest-li všechno 
dobře dopadlo, se můžeš ihned přesvědčit následujícím příkazem:

	$ git tip

Měla by jsi vidět takovýto výpis

```
git: 'tip' is not a git command. See 'git --help'.

Did you mean this?
        tag
```

Vidíš? Git je tak milý, že i když mu zadáš neplatný příkaz, tak se 
pokusí odhadnout, co jsi vlastně mohla mít na mysli. V tuhle chvíli by 
jsi ho mohla poslechnout jeho rady a zkusit zadat

	$ git --help

tak získáš alespoň základní nápovědu, jak jej používat a dozvíš se, co 
skutečně dělá první příkaz, který jsem na tebe zkoušel v úvodu.


## Python

Teď nastal čas vyzkoušet samotný Python. Takže zpátky do terminálu a 
zjisti verzi Pythonu, který máš nainstalovaný

	$ python --version

Hádám že to bude 2.7.x. Ten je totiž v tvém i mém systému jako výchozí 
už předinstalovaný. Ty jsi ale moderní astrofyzička a tak začneme 
rovnou se současnou verzí 3.4.x.

Vše co pro začátek budeš potřebovat je [IPython notebook](http://ipython.org/notebook.html),
respektive [Jupyter](https://jupyter.org), v nějž se vyvinul. Ten 
nainstaluješ včetně všech jeho závislostí jediným příkazem

	$ sudo yum install python3-ipython-notebook

Notebooky připojené k této příručce se nacházejí v adresáři notebooks 
uvnitř adresáře Salome, který vznikl, když sis příručku klonovala z 
gitu. Račte vejít madam...

	$ cd Salome/notebooks/

Spouštění notebooku se pak provádí zadáním příkazu

	$ ipython3 notebook

načež se ti v tvém oblíbeném webovém prohlížeči otevře nová karta s 
přehledem dostupných notebooků. Pokud však ne, najdeš ji na adrese 
<http://localhost:8888>. Jeden si vyber a klikni na 
něj[...](NOTEBOOK.md)
