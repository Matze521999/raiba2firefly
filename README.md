# 💸 CSV Transfer GUI für Firefly III

Ein schlankes Python-Webtool zur Zusammenführung mehrerer CSV-Dateien von Bankkonten. Es erkennt interne Umbuchungen automatisch und bereitet die Daten so auf, dass sie korrekt als **Transfers** in [Firefly III](https://www.firefly-iii.org/) importiert werden können.

---

## 🚀 Funktionen

- Drag-and-Drop Upload von **mindestens 2 CSV-Dateien**
- Automatische Erkennung interner Transfers zwischen eigenen Konten
- Korrekte Zusammenführung aller Transaktionen in einer CSV-Datei
- Weboberfläche auf Basis von Flask
- Bereinigte Datei wird automatisch heruntergeladen
- Alle temporären Daten werden sicher gelöscht
- Bereit für den Einsatz via **Docker & Portainer**

---

## 🖼️ Web-GUI

![Screenshot der Web-GUI](screenshot.png) <!-- Optional: Screenshot hinzufügen -->

---

## 📁 Verzeichnisstruktur

```
csv-transfer-gui/
├── app.py                  # Flask-Server & Upload-Handling
├── processing.py           # Logik zum Verarbeiten und Bereinigen der CSVs
├── requirements.txt        # Abhängigkeiten (Flask, pandas, etc.)
├── Dockerfile              # Docker-Containerdefinition
├── docker-compose.yml      # Für Deployment via Portainer
├── templates/
│   └── index.html          # Weboberfläche
```

---

## 🐳 Deployment via Portainer

### 1. GitHub-Repo in Portainer verwenden

- **Portainer** → **Stacks** → **+ Add Stack**
- Wähle **Git Repository**
- Git-URL eingeben: `https://github.com/DEIN_USERNAME/DEIN_REPO`
- Stelle sicher, dass das Repository diese Dateien enthält:
  - `Dockerfile`
  - `docker-compose.yml`
- **Deploy the Stack**

### 2. Weboberfläche aufrufen

Gehe auf:  
```
http://<deine-server-ip>:5000
```

---

## ⚙️ Lokal testen (ohne Docker)

```bash
git clone https://github.com/DEIN_USERNAME/DEIN_REPO.git
cd DEIN_REPO
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Dann im Browser: `http://localhost:5000`

---

## 📝 Anforderungen an CSV-Dateien

Die hochgeladenen CSV-Dateien müssen dem folgenden Aufbau entsprechen (Bankformat):

```csv
Bezeichnung Auftragskonto;IBAN Auftragskonto;...;Buchungstag;...;Betrag;...;Bemerkung
```

- Trennzeichen: **Semikolon (;)**
- Bei internen Transfers wird automatisch `"Transferbuchung"` in der Spalte **Bemerkung** ergänzt

---

## 🛡️ Datenschutz & Sicherheit

- Keine Speicherung von Bankdaten auf dem Server
- Temporäre Dateien werden nach dem Herunterladen sofort gelöscht
- Kein externer Netzwerkzugriff

---

## 👤 Autor

Matthias  
📍 Süddeutschland  
💼 IT-Systemintegration, Netzwerke, Server, Automatisierung

---

## 📄 Lizenz

MIT License – frei nutzbar & anpassbar
