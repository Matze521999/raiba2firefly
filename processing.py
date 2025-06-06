import csv

def process_csv_files(input_paths, output_path):
    transfers = {}
    all_rows = []

    for path in input_paths:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            rows = list(reader)
            for row in rows:
                row['__source_file'] = path
                all_rows.append(row)

    matched = set()
    result_rows = []

    for row in all_rows:
        if row['Betrag'] == '' or row['Waehrung'] != 'EUR':
            continue

        betrag = row['Betrag'].replace('.', '').replace(',', '.')
        try:
            amount = float(betrag)
        except ValueError:
            continue

        if amount < 0:
            for candidate in all_rows:
                if id(candidate) in matched or candidate == row:
                    continue
                if candidate['Betrag'].replace('.', '').replace(',', '.') == f"{-amount:.2f}" and candidate['__source_file'] != row['__source_file']:
                    matched.add(id(candidate))
                    matched.add(id(row))
                    candidate['Bemerkung'] = 'Transferbuchung'
                    row['Bemerkung'] = 'Transferbuchung'
                    break

    fieldnames = list(all_rows[0].keys())
    fieldnames.remove('__source_file')

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for row in all_rows:
            del row['__source_file']
            writer.writerow(row)
