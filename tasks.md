# Tasks

## Task 1: Installations-Script
Um uns die manuelle Arbeit für das Setup zu ersparen, wollen wir uns ein Installationsscript schreiben.

### Hints
* Erkläre zuoberst im Script, was es High-Level tun soll.
* Kopiere den entsprechenden Abschnitt des README 1:1 als Kommentar in dieses Script, und schreibe einen zusätzlichen Kommentar, was der Coding Assistant tun soll. Kommentare in Bash beginnen mit `#`. 
* Wenn der Assistent nicht versteht, was er tun soll, dann gib ihm weitere Hinweise oder einen Startpunk, an dem er anknüpfen kann.

Beispiel:

```bash
function installLinux {
```

## Task 2: Hello World
Stelle dir vor, du hättest noch nie ein Python Script geschrieben. Wie würdest du es schaffen, dass dein Script "Hello World" ausgibt?

### Hints
* Vergesse nicht, die virtuelle Umgebung zu aktivieren.


## Task 3: Calculator
Erstelle eine Klasse, welche simple Berechnungen ausführen kann. Die Klasse soll folgende Methoden haben:
- `add(a, b)`: Addiert zwei Zahlen
- `sub(a, b)`: Subtrahiert zwei Zahlen
- `mul(a, b)`: Multipliziert zwei Zahlen
- `div(a, b)`: Dividiert zwei Zahlen

Ausserdem nutzt du pytest, um deine Tests zu schreiben. Jede Methode soll mindestens 5 Tests haben.

Die Tests kannst du folgendermassen ausführen:
    
```bash
pytest ./tasks/03-calculator.py
```

### Hints
* Schreibe das Keyword "class" und warte auf die Vervollständigung.
* Vergesse nicht, pytest zu importieren

## Task 4: Code Understanding and Porting
Schaue dir folgende Funktion zusammen mit dem AI Assistenten an. 

```c++
float unknown_function(int n) {
    float unknown = 0.0;
    int unknown = 1;
    for (int i = 1; i < n; i += 2) {
        unknown += sign * 4.0 / i;
        sign *= -1;
    }
    return unknown;
}
```

Leider ist die Funktion für Menschen nicht verständlich. Versuche mit dem AI Assistenten herauszufinden, was die Funktion macht. Im Anschluss sollst du die Funktion in Python portieren und austesten.
