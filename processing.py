import csv

def process_csv_files(input_paths, output_path):
    all_rows = []

    # Lese alle Dateien ein und merke, woher jede Zeile kommt
    for path in input_paths:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            rows = list(reader)
            for row in rows:
                row['__source_file'] = path
                all_rows.append(row)

    matched = set()

    # Transferbuchungen erkennen
    for row in all_rows:
        if row['Betrag'] == '' or row['Waehrung'] != 'EUR':
            continue

        try:
            amount = float(row['Betrag'].replace('.', '').replace(',', '.'))
        except ValueError:
            continue

        if amount < 0:
            for candidate in all_rows:
                if (
                    candidate == row or
                    id(candidate) in matched or
                    id(row) in matched
                ):
                    continue

                try:
                    candidate_amount = float(candidate['Betrag'].replace('.', '').replace(',', '.'))
                except ValueError:
                    continue

                if (
                    candidate_amount == -amount and
                    candidate['__source_file'] != row['__source_file']
                ):
                    # Beide Buchungen markieren
                    matched.add(id(candidate))
                    matched.add(id(row))
                    row['Bemerkung'] = 'Transferbuchung'
                    candidate['Bemerkung'] = 'Transferbuchung'
                    break

    # Nur noch Zeilen behalten, die keine positiven Transferbuchungen sind
    filtered_rows = []
    for row in all_rows:
        try:
            betrag = float(row['Betrag'].replace('.', '').replace(',', '.'))
        except ValueError:
            continue

        if not (
            row.get('Bemerkung') == 'Transferbuchung' and betrag > 0
        ):
            filtered_rows.append(row)

    # Feldnamen für CSV-Ausgabe
    fieldnames = list(filtered_rows[0].keys())
    if '__source_file' in fieldnames:
        fieldnames.remove('__source_file')

    # Vor dem Schreiben: entferne Hilfsspalte
    for row in filtered_rows:
        if '__source_file' in row:
            del row['__source_file']

    # CSV-Datei schreiben
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(filtered_rows)
