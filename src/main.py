import os
from read_counties import ReadCounties
from read_states import ReadStates
from read_US import ReadUS

dataType = input('Please type in the dataset you want to see (Counties, States, or US):')


path = os.getcwd()
path_data =  path + '/data'

path_counties = path_data + '/us-counties.csv'
path_states = path_data + '/us-states.csv'
path_US = path_data + '/us.csv'

def print_list(listname):
    for row in listname:
        print(row,end = '\n')

if dataType == 'Counties':
    data = ReadCounties(path_counties)
    print_list(data.read_all(path_counties))
elif dataType == 'States':
    data = ReadStates(path_states)
    print_list(data.read_all(path_states))
elif dataType == 'US':
    data = ReadUS(path_US)
    print_list(data.read_all(path_US))
