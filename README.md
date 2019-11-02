# Computer Vision freie Aufgabe
**Skript Bilder herrunterladen für Datensatz**  
Für Shutterscrape Skript muss man folgendes ausführen für Python 3.7:  
Bevor man es ausführt muss folgendes installiert werden:  
`pip install beautifulsoup4`  
`pip install selenium`  
`pip install lxml`  

Ausführen der Skript:  
`python shutterscrape.py`  

Schritte um Bilder zu speichern:  
* Speicherort aussuchen wo die Bilder gespeichert werden
* Anzahl der Suchwörter eingeben z.B: für große Schlüssel 2
* Anschließend den Suchwort eingeben
* Man kann es nochmal wiederholen mit anderen Suchwörtern

Diese Skript dient nur die Sammlung von Bilder für die Datensätze.
Diese Skript stammt aus: https://gist.github.com/chuanenlin/37b0c26718c7e83bbb6ab6b13951f9cf#file-shutterscrape-py

**Erstellen der Datensätze durch Annotation** 
*  Annotationtool:
    1. Ausführen: `py annotation_dataset.py`
    2. `Pfad mit Bilder: <Eingabe der Bilder>`    <= muss noch bissche bearbeitet werden
    3. Ausgabe der Texte als <Name des Bildes>.txt
        => Ausgabe der Textdatei: `ClassNr x y width height`


**Trainieren oder abspielen lassen in Google Colab**  
Tutorial:  
https://colab.research.google.com/drive/1lTGZsfMaGUpBG4inDIQwIJVW476ibXk_#scrollTo=WD5FBWmjrsks  

`ComputerVisionPraktikum.ipynb` beinhaltet Code für Ausführung in Colab  

In darknet Ordner sind erzeugte Datei darknet und aktuell NFPA-Bilder drinne die Später durch schlüsseln ersetzt werden.  

Trainierte Daten sind unter `darknet/bin/cfg/backup/` vorhanden  

Ausführung siehe in ipynb Datei. 
