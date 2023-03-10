# Techbier über AI-powered Coding Assistants

>**Achtung**: die erste Aufgabe wird es sein, ein Setup Script zu erstellen. Dh. folgende Schritte müssen noch nicht zwingend durchgeführt werden. Bitte dennoch durchlesen. Allerdings ist dies nur mit Copilot möglich, da Codewhisperer noch nicht in der Lage ist, ein Bash oder Powershell Scripte zu schreiben.

## Setup

### Python & pip
Python 3 und pip werden benötigt, um die Python-Umgebung zu installieren.

Linux:
```bash
sudo apt-get install python3 python3-pip
```

Windows:
* [Python 3](https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe) herunterladen und installieren
* [pip](https://bootstrap.pypa.io/get-pip.py) herunterladen und ausführen

Mac:

```bash
brew install python3
```

### Virtualenv
Virtualenv wird benötigt, um die Python-Umgebung zu isolieren. Damit wird verhindert, dass die Python-Umgebung des Systems verändert wird.

Installation:
```bash
pip3 install virtualenv
```

Virtuelle Umgebung einmalig aufsetzen:
```bash
virtualenv -p python3 venv
```

Virtuelle Umgebung aktivieren:
```bash
source venv/bin/activate # Linux oder Mac
```

```powershell
venv\Scripts\activate.ps1 # Windows
```

Virtuelle Umgebung deaktivieren:
```bash
deactivate
```

### Requirements
Die Python-Umgebung kann mit den Requirements installiert werden, die in der Datei `requirements.txt` hinterlegt sind.

```bash
pip3 install -r requirements.txt
```

## Scripte erweitern und ausführen

* Im Ordner Tasks sind die Aufgaben direkt als Python-oder Bash-Skripte hinterlegt. Diese können mit `<taskname>.py` ausgeführt werden, sofern die virtuelle Umgebung aktiviert ist.


# Lösungen
Da sich der AI Assistent an den Lösungen orientieren würde, haben wir die Lösungen nur Base64 kodiert hinterlegt. Um die Lösungen zu sehen, müssen sie erst dekodiert werden.

Um die Lösung der ersten Aufgabe im Terminal auszugeben, folgendes Script ausführen:

Linux oder Mac:
```bash
./get-solution.sh 1
```

Windows:
```powershell
./get-solution.ps1 1-windows # bei Lösung 1 gibt's eine Windows Variante
./get-solution.ps1 2 # bei den restlichen ist es die gleiche Lösung wie unter Linux/Mac
```

# Tips & Tricks

## Alternative Lösungsvorschläge anzeigen
Die AI-Assistenten sind in der Lage mehrere Vorschläge zu generieren, damit der/die Entwickler:in die beste Lösung finden und mit einem Klick akzeptieren und übernehmen kann.

### Github Copilot und VSCode
Dazu die Tastenkombination `Ctrl + Shift + P` oder `⌘ + Shift + P)` drücken und `copilot` eingeben. Mit der Option 'Open Github Copilot' sollte ein neues Fenster öffnen.

# Troubleshooting

### Der AI-Assistent schlägt keine Lösung vor
Es kann vorkommen, dass der Assistant auch nach mehreren Sekunden noch keine Lösung vorschlägt. Meistens hilft es, die zusätzliche Anzeige von Copilot zu öffnen. Dazu einfach die Tastenkombination `Ctrl + Shift + P` oder `⌘ + Shift + P)` drücken und `copilot` eingeben. Mit der Option 'Open Github Copilot' sollte ein neues Fenster mit dem Assistant geöffnet werden. Die Synthetisierung der Lösung wird dann nochmals getriggert und man kann zwischen den verschiedenen Lösungsmöglichkeiten auswählen.

### Der AI-Assistent schlägt immer wieder die gleich falsche Lösung vor
Manchmal werden unbrauchbare Lösungen generiert. Meistens fehlen dem Assistenten zusätzliche Informationen (z.B. Business Logik), welche man zB in Form von Code-Schnippsel oder Kommentaren an der entsprechenden Stelle im Code hinterlegen kann. Ausserdem kann es hilfreich sein, sich die alternativen Lösungsvorschläge anzuschauen. Siehe Frage oben.

### Mein Python Script lässt sich nicht ausführen
Stelle sicher, dass die virtuelle Python-Umgebung aktiviert ist, die Requirements korrekt installiert wurden und die Datei ausführbar ist.

Aktiviere die virtuelle Python-Umgebung:
```bash
source venv/bin/activate
```

Python Datei ausführbar machen:
```bash
chmod +x ./tasks/0X_task.py
```

Stelle sicher, dass die erste Zeile des Python Scripts korrekt ist:
```python
#!/usr/bin/env python3
```
