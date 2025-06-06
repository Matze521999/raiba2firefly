# CSV Transfer GUI

Ein winziges Vorwort zu diesem noch winzigeren Projekt:
Dieses Tool wurde für die private Verwendung dreckig in 15mins heruntergeschrieben.
Bugs, Fehler, Abstürze nicht auszuschließen. Für meine spezifischen Zwecke reicht es, mehr soll es auch nicht können.
Benutzen auf eigene Gefahr! ;)

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
   http://localhost:5000
   ```

3. CSV-Dateien hochladen und bereinigte Datei herunterladen

## Format der CSV-Dateien

CSV-Dateien müssen mit `;` getrennt sein und folgendes Format haben (Raiffeisenbank CSV-Export):

```
Bezeichnung Auftragskonto;IBAN Auftragskonto;BIC Auftragskonto;Bankname Auftragskonto;Buchungstag;Valutadatum;Name Zahlungsbeteiligter;IBAN Zahlungsbeteiligter;BIC (SWIFT-Code) Zahlungsbeteiligter;Buchungstext;Verwendungszweck;Betrag;Waehrung;Saldo nach Buchung;Bemerkung;Gekennzeichneter Umsatz;Glaeubiger ID;Mandatsreferenz
```

Nur EUR-Umsätze mit gültigen Beträgen werden verarbeitet.

## Lizenz

MIT
