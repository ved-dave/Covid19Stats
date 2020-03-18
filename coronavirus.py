import numpy
import scipy
import csv
from matplotlib.pyplot import*





if __name__ == '__main__':
    with open('time_series_19-covid-Confirmed.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print('The countries/regions are')
                    line_count += 1
                else:
                    if not row[0]:
                        print('\tLocation: {}. '.format(row[1]), end = '')
                    else:
                        print('\tLocation: {}, {}'.format(row[0], row[1]), end = '')
                    index = 0
                    cases_list = []
                    for elem in row:
                        if index > 3:
                            cases_list.append(elem)
                            #print(cases_list)
                        index += 1
                    print(cases_list)


        
