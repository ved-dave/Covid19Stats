import numpy
import scipy
import csv
from matplotlib.pyplot import*

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
                            cases_list.append(elem) # add cases for each day to the list
                            graphingTest(cases_list)
                            #print(cases_list, end='')
                        index += 1
                    print(cases_list)
                    

def graphingTest(myList)
    for i in myList:
        x1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        y1 = mylist[i]
        plt.plot(x1,y1,label = "line X")
        plt.xlim(1,40)
        plt.ylim(0,500)
        plt.xlabel('Days')
        plt.ylabel('Confirmed Victims')
        plt.show()

