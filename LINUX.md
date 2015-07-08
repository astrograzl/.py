# GNU/Linux

V dávné době, kdy se příkazy počítači psaly velkými písmeny se zrodil 
systém pro sdílení strojového času UNIX. Od té doby uplynulo mnoho 
cyklů během nichž se UNIX vyvinul v Linux. Samotný Linux tvoří jádro 
operačního systému, nebo-li kernel. Spolu s volně dostupnými programy z 
rodiny GNU ho získáš v praktickém balení jako distribuci.

Jednotlivé distribuce se liší jen v detailech. Ve výchozím grafickém 
prostředí. Ve verzích obsažených programů. Způsobu konfigurace systému 
a správy balíčků s programy. V každé distribuci ale najdeš program, 
který emuluje Terminál. Tak si teď pojďme projít několik základních 
příkazů.

Příkaz se skládá z názvu programu, za kterým mohou následovat přepínače 
ovlivňující jeho chování a na konec parametry, kterými se programu 
předávají potřebné informace.

## apropos whatis man

Když nevíš, můžeš se zeptat. Většina programů akceptuje přepínače `-h` 
nebo `--help` pro zobrazení nápovědy. Nebo ho můžeš spustit jen tak bez 
přepínačů a parametrů. Buď vypíše nějaké instrukce a skončí, nebo ho 
můžeš ukončit klávesovou zkratkou `Ctrl+C`.

	$ man
	Kterou manuálovou stránku si přejete?

Když jsi si nejsi jistá, můžeš vyhledat všechny manuály na dané téma

	$ apropos python

Pokud chceš jenom vědět co daný program dělá, není nic snazšího než 
zkusit

	$ whatis apropos

Pak už si stačí jen vybrat tu pravou a požadovanou stránku zobrazit

	$ man ipython

Prohlížeč manuálových stránek ukončíš stiskem klávesy `q`. Po stisknutí 
klávesy `h` získáš nápovědu k prohlížeči, která je platná i pro 
prohlížeč textových souborů LESS(1). Za prohlédnutí rozhodně stojí i 
samotná manuálová stránka programu MAN(1).

	$ man man

Alespoň tuhle jedinou by jsi mohla přečíst od začátku až do konce. 
Seznámíš se tak s její strukturou a příště se ti bude v dalších hledat 
už mnohem rychleji. Třeba taky zjistíš, co znamenají ty čísla za názvy 
programů.
