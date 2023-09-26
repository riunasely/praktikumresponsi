import csv
with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[1])
    for row in reader:
        print(row[1])
    year_1958 = dict()
    for row in reader:
        year_1958[row[0]] = row[1]
    print(year_1958)
    year_1958 = dict()
    for row in reader:
        year_1958[row[0]] = row[1]
    print(year_1958)
    max_1958 = max(year_1958.values())
    print(max_1958)
    year_1958 = dict()
    for row in reader:
        year_1958[row[0]] = row[1]
    print(year_1958)
    max_1958 = max(year_1958.values())
    print(max_1958)
    for k, v in year_1958.items():
        if max_1958 == v:
            print(f'Bulan tersibuk di tahun 1958:{k}, Flights:{v.strip()}'}
