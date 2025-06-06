import csv

def process_csv_files(input_paths, output_path):
    all_rows = []

    # CSVs einlesen mit Quell-Datei
    for path in input_paths:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                row['__source_file'] = path
                all_rows.append(row)

    matched_ids = set()
    filtered_rows = []

    for i, row in enumerate(all_rows):
        if row['Betrag'] == '' or row['Waehrung'] != 'EUR':
            continue

        try:
            amount = float(row['Betrag'].replace('.', '').replace(',', '.'))
        except ValueError:
            continue

        # Nur negative Beträge → nur Ausgänge prüfen
        if amount < 0 and i not in matched_ids:
            for j, candidate in enumerate(all_rows):
                if i == j or j in matched_ids:
                    continue

                try:
                    candidate_amount = float(candidate['Betrag'].replace('.', '').replace(',', '.'))
                except ValueError:
                    continue

                # Prüfkriterien:
                if (
                    candidate_amount == -amount and
                    row['Buchungstag'] == candidate['Buchungstag'] and
                    row['Valutadatum'] == candidate['Valutadatum'] and
                    row['IBAN Auftragskonto'] == candidate['IBAN Zahlungsbeteiligter'] and
                    row['IBAN Zahlungsbeteiligter'] == candidate['IBAN Auftragskonto']
                ):
                    # Markieren
                    row['Bemerkung'] = 'Transferbuchung'
                    candidate['Bemerkung'] = 'Transferbuchung'
                    matched_ids.add(i)
                    matched_ids.add(j)
                    filtered_rows.append(row)  # nur ausgehende Buchung behalten
                    break
        elif i not in matched_ids:
            filtered_rows.append(row)

    # CSV schreiben
    fieldnames = list(all_rows[0].keys())
    if '__source_file' in fieldnames:
        fieldnames.remove('__source_file')
    
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for row in all_rows:
            # Transfer: Nur negative Buchung behalten
            if row.get('Bemerkung') == 'Transferbuchung':
                betrag = row['Betrag'].replace('.', '').replace(',', '.')
                if float(betrag) > 0:
                    continue  # positive Seite des Transfers überspringen
    
            row.pop('__source_file', None)
            writer.writerow(row)

