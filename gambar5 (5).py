import csv
with open('people.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    csvdata = (5, 'Anne', 'Amsterdam')
    writer.writerow(csvdata)
with open('numbers.csv', 'w') as f:
    writer = csv.writer(csvfile)
    csvdata = (['x', 'x**2', 'x**3', 'x**4'])
    for x in range(1,101):
    writer.writerow([x, x**2, x**3, x**4])
