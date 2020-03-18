import csv

with open('time_series_19-covid-Confirmed.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print('The countries/counties are {", ".join(row)}')
                line_count += 1
            else:
                print('\tCountry: {row[1]}. ')
                line_count += 1

