# Registermaschine
Einfache Simulation einer Registermaschine.

# Dokumentation
Die Befehle werden Zeilenweise aus der "text.txt" Datei gelesen.

Die Befehlsfrequenz kann als optionaler Parameter angegeben werden `Registermaschine.py 10`.

## Namenskonventionen
$PC$: Befehlszähler.

$f\left( 0 \right)$: Inhalt des Akkumulators.

$f\left( adresse \right)$: Inhalt des Datenspeichers an der Stelle _adresse_.

## Befehle
| Syntax        | Semantik                                | Beschreibung                  |
| ------------- | --------------------------------------- | ----------------------------- |
| ADD _adresse_ | $f(0)=f(0)+f(adresse)$                  | Addieren                      |
| SUB _adresse_ | $f(0)=f(0)-f(adresse)$                  | Subtrahieren                  |
| MUL _adresse_ | $f(0)=f(0) \cdot f(adresse)$            | Multiplizieren                |
| DIV _adresse_ | $f(0)=f(0) \div f(adresse)$             | Dividieren                    |
| LDA _adresse_ | $f(0)=f(adresse)$                       | Laden                         |
| LDK _zahl_    | $f(0)=zahl$                             | Konstante Laden               |
| STA _adresse_ | $f(adresse)=f(0)$                       | Speichern                     |
| INP _adresse_ | $f(adresse)=<Eingabe>$                  | Eingeben                      |
| OUT _adresse_ | $<Ausgabe> = f(adresse)$                | Ausgeben                      |
| HLT 99        |                                         | Programmende                  |
| JMP _adresse_ | $PC = adresse$                          | Jump                          |
| JEZ _adresse_ | Falls $f(0)=0$, dann $PC = adresse$     | Jump if equal zero            |
| JNE _adresse_ | Falls $f(0) \ne 0$, dann $PC = adresse$ | Jump if not equal zero        |
| JLZ _adresse_ | Falls $f(0) <0$, dann $PC = adresse$    | Jump if less than zero        |
| JLE _adresse_ | Falls $f(0) \le 0$, dann $PC = adresse$ | Jump if less or equal zero    |
| JGZ _adresse_ | Falls $f(0)>0$, dann $PC = adresse$     | Jump if greater than zero     |
| JGE _adresse_ | Falls $f(0) \ge 0$, dann $PC = adresse$ | Jump if greater or equal zero |


## Beispielprogramm
Berechnung von $\sum_{i=0}^{n}i^{3}$ für ein eingegebenes $n$:
```
INP01
LDK0
STA02
LDA01
MUL01
MUL01
ADD02
STA02
LDK-1
ADD01
STA01
JGE5
OUT02
HLT99
```
