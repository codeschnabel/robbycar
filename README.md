# Inhalt

- [Inhalt](#inhalt)
- [1. Schnellstart für Entwickler](#1-schnellstart-für-entwickler)
  - [1.1 MicroPython auf dem Raspberry Pi Pico installieren](#11-micropython-auf-dem-raspberry-pi-pico-installieren)
  - [1.2 Entwicklungsumgebung einrichten](#12-entwicklungsumgebung-einrichten)
  - [1.3 Weitere Hinweise](#13-weitere-hinweise)
- [2. Quick-Deployment](#2-quick-deployment)

# 1. Schnellstart für Entwickler

> Für eine Schnellanleitung wie man das Projekt auf einen neuen Buggy / ein neues Raspberry Pi Pico W deployed, bitte Kapitel 2 dieser Readme lesen.

## 1.1 MicroPython auf dem Raspberry Pi Pico installieren

* Anmerkung: Voraussetzung: Python (das "normale") muss installiert sein.

* Die "Boot Sel"-Taste auf dem 'Raspberry Pi Pico W' gedrückt HALTEN.

* 'Raspberry Pi Pico W' mit dem PC über ein Micro-USB-Kabel verbinden und dann die Taste los lassen sobald das Gerät im Datei Explorer erscheint.

* Das Pico sollte als USB-Laufwerk namens "RPI-RP2" erscheinen.

* Auf dem USB-Laufwerk befindet sich ein Weblink namens "Index.htm". Den anklicken. Der Link führt zur Pico-Webseite.

* Auf den Tab mit der Bezeichnung "Microcontrollers" den Button "Pico-series Microcontrollers" anklicken. Links im Menü dann auf Microcontrollers/ MicroPython klicken und den Anweisungen folgen. Die UF2-Datei herunter laden und auf das PRI-RP2-Laufwerk (Datei-Explorer) kopieren. Alternativ kann die UF2-Datei im Assets-Verzeichnis dieses Repos verwendet werden.

* Raspberry Pi Pico neu starten, indem das USB Kabel aus und eingesteckt wird.

## 1.2 Entwicklungsumgebung einrichten

* Die VSCode Extension MicroPico installieren

* Das interaktive Pico Terminal ("REPL") öffnen (Ctrl+Ö und dann das Pico Terminal im Dropdown des Terminals auswählen).

* Folgendes Zeile für Zeile eingeben:

```
from machine import Pin
pin = Pin("LED", Pin.OUT)
pin.on()
pin.off()
```

Bei pin.on() müsste die LED auf dem Pico angehen.

* Nächster Schritt: test-scripts/test_pico_led.py ausführen. Dazu Datei öffnen und per rechtsklick im File-Explorer (vscode) oder per Command Palette auf dem Pico ausführen. Über die Command Pallete von VS Code kann man die Ausführung der Datei beenden: "MicroPico: Stop execution".

* Wenn im VSCode die Python Imports nicht erkannt werden liegt es daran: Pylance, der Python-Sprachserver für Visual Studio Code, versucht, die Module, die importiert werden zu analysieren, kann jedoch die MicroPython-spezifischen Module nicht finden, da diese in der Standard-Python-Bibliothek nicht existieren. Lösungsvorschlag: micropython-stubs installieren (das sind quasi typings wie die micropython module aussehen (die eigentlichen Module liegen nur auf dem Pico und nicht in der IDE vor)). Die genaue Vorgehensweise zur Installation ist hier erklärt: https://micropython-stubs.readthedocs.io/en/latest/20_using.html

Falls die Quelle nicht verfügbar ist siehe Datei assets/using-the-micro-python-stubs.md in diesem Repo. HINWEIS: wenn die UF2 Datei aus dem assets Verzeichnis geflasht wurde dann können die Typings mittels "pip install -U micropython-rp2-stubs==1.23.*" auf der CMD installiert werden. Vorher jedeoch VENV anlegen (siehe die o.g. Installationsanweisung oder .md Datei).

* Wenn das Pico nach dem Verbinden mit dem PC irgendetwas tut kann es sein dass bereits Dateien darauf sind (diese sieht man NICHT wenn man beim Verbinden den BOOT SEL Button auf dem Pico gedrückt hält - der BOOT SEL Button ist nur zum Flashen der Firmware). Zum Anzeigen der Dateien in der REPL folgendes eingeben:

```
import os
os.listdir()
```

Zum Anzeigen einer Datei:

```
import os
with open('main.py', 'r') as file:
    print(file.read())
```

Zum Löschen einer Datei vom Pico:

```
import os
os.remove('main.py')
```

## 1.3 Weitere Hinweise

* Damit man mit dem Pico die Kitronik Roboter Buggy Plattform verwenden kann muss die "PicoAutonomousRobotics.py" aus dem root Verzeichnis an das Pico gesendet (übertragen) werden.

* Danach kann man eine main.py schreiben und an das Pico senden (übertragen). Die main.py wird immer nach dem Start des Picos ausgeführt!

* Als nächstes würde ich empfehlen die test-horn.py auszuprobieren, da diese mit der API des Buggys kommuniziert. Dazu muss der Buggy selber mit Strom (Batterien) versorgt werden.

* Flashen der Firmware und aller Dateien auf dem Pico geht mit der assets/flash_nuke.uf2


# 2. Quick-Deployment


1. Die "Boot Sel"-Taste auf dem 'Raspberry Pi Pico W' gedrückt HALTEN.

2. 'Raspberry Pi Pico W' mit dem PC über ein Micro-USB-Kabel verbinden und dann die Taste los lassen sobald das Gerät im Datei Explorer erscheint.

3. Das Pico sollte als USB-Laufwerk namens "RPI-RP2" erscheinen.

4. Die UF2 Datei RPI_PICO_W-20240602-v1.23.0.uf2 aus dem assets Verzeichnis auf das PICO kopieren

5. Raspberry Pi Pico neu starten, indem das USB Kabel aus und eingesteckt wird.

6.  Verbindung zum Rasbperry Pi Pico W mittels Micro USB Kabel herstellen.

7. Folgende Dateien auf das Pico übertragen:
   1. PicoAutonomousRobotics.py
   2. main.py
   
8. Übertragung der Dateien prüfen:
   1. REPL öffnen
   2. Zeile für Zeile eingeben:
        ```
        import os
        os.listdir()
        ```