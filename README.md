# CSV Transfer GUI

Ein minimalistisches Web-Tool zur Erkennung und Bereinigung von internen Transferbuchungen in CSV-Dateien von Bankkonten.

## Funktionen

- Upload von 2 bis beliebig vielen CSV-Dateien per Drag & Drop
- Automatische Erkennung interner Umbuchungen
- Zusammenführung der Daten in eine bereinigte CSV
- Download der Ergebnisdatei direkt nach Verarbeitung

## Verwendung

1. Projekt starten (Docker):
   ```bash
   docker compose up
   ```

2. Webbrowser öffnen:
   ```
   http://<IP-Adresse>:5000
   ```

3. CSV-Dateien hochladen und bereinigte Datei herunterladen

## Format der CSV-Dateien

CSV-Dateien müssen mit `;` getrennt sein und folgendes Format haben:

```
Bezeichnung Auftragskonto;IBAN Auftragskonto;...;Betrag;Waehrung;...
```

Nur EUR-Umsätze mit gültigen Beträgen werden verarbeitet.

## Lizenz

MIT
