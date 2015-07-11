# GNU/Linux

V dávné době, kdy se příkazy počítači psaly velkými písmeny se zrodil 
systém pro sdílení strojového času UNIX. Od té doby uplynulo mnoho 
cyklů během nichž se původní UNIX vyvinul v dnešní Linux. Samotný Linux 
tvoří jádro operačního systému, nebo-li kernel. Spolu s volně 
dostupnými programy z rodiny GNU ho získáš v praktickém balení doslova 
na stříbrném podnose jako takzvanou distribuci.

Jednotlivé distribuce se navzájem liší jen v detailech. Ve výchozím 
grafickém prostředí. Ve verzích obsažených programů. Způsobu 
konfigurace systému a správy balíčků s programy. V každé distribuci ale 
najdeš program, který emuluje Terminál. Tak si teď pojďme projít 
několik základních příkazů.

Příkaz se skládá z názvu programu, za kterým mohou následovat jeho 
argumenty. Těmi jsou přepínače ovlivňující jeho chování a parametry 
jako například názvy souborů, které má program pro tebe zpracovat. 
Název programu bývá velmi často tvořen jako zkratka z popisu jeho 
funkce a slouží tak zároveň i jako mnemotechnická pomůcka. Přepínače 
programu mívají zpravidla dvě varianty

* krátká varianta je uvozena jednou pomlčkou a je tvořena jedním 
písmenem jako například `-h` pro vypsání nápovědy

* dlouhá varianta je uvozena dvěma pomlčkami a může být tvořena i 
několika slovy vzájemně spojenými pomlčkami, jako například 
`--help-all`

Přepínače mohou mít samy své vlastní parametry. U krátkých přepínačů 
odděleny mezerou a u dlouhých přepínačů, které se prakticky používají 
převážně ve skriptech, rovnítkem `=`. Speciální přepínač `--` značí, že 
za ním následují už jenom parametry pro samotný program. Symbolicky 
zapsáno vypadá příkaz nějak takto

	$ program -p on --prepinac=off -- parametr1 parametr2


## Hledání nápovědy

Většina programů akceptuje přepínače `-h` nebo `--help` pro zobrazení 
nápovědy. Jejímu psaní věnují vývojáři někdy i více času než samotnému 
programování. Tím že si ji přečteš jim projevuješ respekt za jejich 
nezištnou práci. Když si s něčím nevíš rady, zeptej se svého muže. Ten 
má přehled o všech manuálech, které jsou k programům dostupné.

	$ man
	Kterou manuálovou stránku si přejete?

Když si nejsi jistá, můžeš vyhledat všechny manuály na dané téma

	$ apropos python

Pokud tě jenom zajímá co daný program dělá, není nic snazšího než 
zkusit

	$ whatis python

Prohlížeč manuálových stránek ukončíš stiskem klávesy `q`. Po stisknutí 
klávesy `h` získáš nápovědu k prohlížeči, která je platná i pro 
prohlížeč textových souborů LESS(1). Za prohlédnutí rozhodně stojí i 
samotná manuálová stránka programu MAN(1).

	$ man man

Alespoň tuhle jedinou by jsi mohla přečíst od začátku až do konce. 
Seznámíš se tak s její strukturou a příště se ti bude v dalších hledat 
už mnohem rychleji. Třeba taky zjistíš, co znamenají ty čísla za názvy 
programů.

Jako čtení na dlouhé zimní večery ti mohu doporučit Info stránky, které 
jsou rovněž součástí Linuxu a obsahuji nepřeberné množství informací. 
Dostaneš se k nim snadno

	$ info

Veškeré instrukce potřebné k jejich prohlížení se dočteš už v prvním 
odstavci. Info stránky jsou spíše takové pojednání o Linuxu a jeho 
programech. Pro praktické účely bohatě stačí občas nahlédnout do 
manuálových stránek, když si zrovna nejsi jistá, jak se který program 
přesně používá.


## Řešení problémů

Tak jako Neo v úvodní scéně Matrixu, můžeš zkusit opakovaně stisknout 
kombinací kláves `Ctrl+C`, pokud se ti bude zdát, že se právě běžící 
program zasekl. Pro sledování využití prostředků počítače, tedy 
vytížení procesoru a obsazení fyzické paměti i odkládacího prostoru 
slouží Správci úloh ne nepodobný program TOP(1).

	$ top
    
![top](screenshots/top.png)

Úlohy se v něm dají řadit podle vytížení procesoru pomocí klávesové 
zkratky `Shift+P` nebo podle množství zkonzumované paměti kombinací 
kláves `Shift+M`. A to nejdůležitější, že se ukončuje klávesou `q`.

Občas se může stát, že se některý program prostě zblázní a přestane 
odpovídat. Pak nezbývá nic jiného než ho bez milosti zabít. Pojďme si 
cvičně takovou situaci nasimulovat. Začni tím, že v Terminálu spustíš 
program YES(1), který neděla nic jiného, než že pořád dokola vypisuje 
text, který mu předáš jako parametr.

	$ yes "All work and no play makes Jack a dull boy"	
	
Použitím klávesové zkratky `Ctrl+Z` jeho běh pozastavíš. Podívej se na 
výpis všech svých spuštěných programů, ten získaš pomocí příkazu

	$ ps x

Vidíš toho šílence jen pár řádek před koncem výpisu? To je on. Zachovej 
klid a nepropadej panice! Nezbedný program ukončíš tak, že mu zašleš 
speciální signál

	$ kill -9 ####
	
Za znaky `####` dosaď správný PID, tedy to číslo z prvního 
sloupce, ale dej si dobrý pozor, aby jsi ho opsala ze správného řádku. 
Jistější přeci jen bude ho zkopírovat a vložit.


## Standardní vstup a výstup

Počítač s tebou komunikuje pomocí takzvaného standardního vstupu, 
výstupu a chybového výstupu. Vstup představuje klávesnice, pomocí které 
zadáváš příkazy a výstupem je obrazovka, na které se vše zobrazuje.
Vstup může být přesměrován ze souboru, ve kterém jsou zapsány 
instrukce, které by jsi jinak musela zadávat ručně

	$ program < vstup.in

Stejně tak i výstup programu můžeš podobně přesměrovat do souboru

	$ program > vystup.out

Chybový výstup můžeš buď přesměrovat zvlášť pomocí `2>` nebo můžeš oba 
výstupy přesměrovat do jednoho souboru použitím `&>`. Pokud se má 
výstup jednoho programu stát zároveň i vstupem pro druhý program, 
použij tak zvanou roupu, neboli PIPE

	$ program1 | program2

Chceš-li použít standardní vstup nebo výstup v místě, kde program 
očekává běžný soubor, napiš místo něj pomlčku `-`.


## Spouštění úloh na pozadí

Spuštěný program po dobu svého běhu blokuje Terminál pro další použití. 
To můžeš obejít tak, že danou úlohu spustíš na pozadí přidáním znaku 
`&` na konec příkazu

	$ program &

Potřebuješ-li do pozadí přenést již běžící program, napřed ho 
pozastavíš pomocí klávesové zkratky `Ctrl+Z` a následně použiješ příkaz 
`bg`. Naproti tomu příkaz `fg` přepne program zpátky do popředí.

Všechny tyto techniky se dají kombinovat, tak že za chvíli budeš 
naprosto s přehledem používat třeba takovéto konstrukce příkazů

	$ program1 < vstup.in | program2 | program3 > vystup.out &

Od této chvíle se z tebe stává nebezpečná hackerka ;-)


## Vzdálené přihlášení

Další předností Linuxu je, že prostřednictvím jednoho počítače můžeš 
ovládat druhý, klidně až na opačné straně Zeměkoule, aniž by ses musela 
hnout z pohodlí své pohovky. Program pro přihlášení ke vzdálenému 
počítači se jmenuje SSH(1) a používá se následovně

	$ ssh -X uživatel@počítač

Toto je taky důvod, proč počítače dostávají smysluplná jména, která se 
objevují v jejich adrese. Přepínač `-X` přesměruje grafický výstup ze 
vzdáleného na tvůj počítač. A tak, i když spouštíš programy na 
vzdáleném počítači, jejich výstup se zobrazuje na tvém vlastním.


## Vzdálené odhlášení

Na co by sis měla dát pozor je, že při ukončení spojení se vzdáleným 
počítačem se automaticky ukončí i všechny tvoje úlohy běžící na pozadí. 
Proto je třeba abys byla prozíravá a myslela na to, ještě dřív než je 
spustíš. Jednou z možností je použití příkazu NOHUP(1) spolu se 
spuštěním programu na pozadí.

	$ nohup ... &
	
Druhou možností je použití programu SCREEN(1), který ti vytvoří 
virtuální obrazovku, od které se můžeš bez obav odpojit a posléze k ní 
znovu připojit.

	$ screen

Teď můžeš spustit nějaký program, třeba známý TOP(1) a pomoci kombinace 
kláves `Ctrl+A Ctrl+D` se od screenu odpojit. Program v něm bude běžet 
dál i po odhlášení se ze vzdáleného počítače. Znovu se k němu připojíš 
zadáním

	$ screen -r

Pokud screen už dále nepotřebuješ, ukonči ho jak jsi zvyklá, buď pomocí 
klávesové zkratky `Ctrl+D` nebo příkazem `exit`.


## Podmíněné spuštění

Někdy se může stát, že budeš chtít spustit nějaký příkaz, jen pokud 
předchozí příkaz zkončil úspěšně. Takovou typickou situací je kompilace 
a instalace speciálních programů. Standardní postup výpadá následovně

	$ ./configure
	$ make
	$ sudo make install

Než čekat až některý krok doběhne do konce, můžeš mezi příkazy použít 
logický operátor `&&`, který zajistí, že se následující příkaz vykoná 
jen pokud předchozí příkaz skončil úspěšně. Předchozí tři příkazy se 
pomocí něj dají přepsat v jeden

	$ ./configure && make && sudo make install

Jako protiklad existuje logický operátor `||`, který následující příkaz 
vykoná jen v případě neúspěchu prvního příkazu. Pokud chceš, aby se 
všechny příkazy vykonaly postupně bez ohledu na jejich výsledek, prostě 
je odděl středníkem `;`. 
