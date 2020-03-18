import numpy
import math
import scipy
import csv
import matplotlib.pyplot as plt


def graphingTest(myList):
    #x1 = list(range(0,len(myList)))
    plt.figure()
    x = list(range(0, len(myList)))
    print(max(myList))
    plt.scatter(x, myList)
    plt.xlabel('Days since 1/22/20')
    plt.ylabel('Confirmed Cases')
    plt.title("[country name]")
    #plt.autoscale(enable=True, axis='y', tight=true)
    plt.show()

if __name__ == '__main__':
    with open('time_series_19-covid-Confirmed.csv') as csv_file: # load raw data from JHU
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader: # iterate through each location
                if line_count == 0: # initialize first row of dates
                    print('The countries/regions are:')
                    line_count += 1
                else:
                    if not row[0]: # check if location has a subregion
                        print('\tLocation: {}. '.format(row[1]), end= '')
                    else:
                        print('\tLocation: {}, {}'.format(row[0], row[1]), end= '')
                    index = 0
                    cases_list = [] # create a list for location
                    for elem in row:
                        if index > 3:
                            cases_list.append(int(elem)) # add cases for each day to the list
                            #print(cases_list, end='')
                        index += 1
                    print(cases_list)
                    graphingTest(cases_list)
                    




