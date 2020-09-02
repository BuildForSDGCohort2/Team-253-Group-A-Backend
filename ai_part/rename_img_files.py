"""
This piece of code is used to rename image files and move them to a specific folder.
"""

import os

root_dir = './covidTrash'
first_dir = './covidTrash/as_trash_clean_v1.clean/'
second_dir = './covidTrash/covid_19.clean/'
third_dir = './covidTrash/used_s.clean/'
clean_data_dir = './covidTrash/cleaned_data/'
fourth_dir = './covidTrash2/discarded_hand_sanitizer.clean/'
fifth_dir = './covidTrash2/discarded_s.clean/'
sixth_dir = './covidTrash2/discarded.clean/'
seventh_dir = './covidTrash2/used__thrown.clean/'
eigth_dir = './covidTrash2/used.clean/'

#files = []
"""
for file in os.listdir(first_dir):
    os.rename(first_dir + file, clean_data_dir + 'first_' + file)
    
for file in os.listdir(second_dir):
    os.rename(second_dir + file, clean_data_dir + 'second_' + file)
for file in os.listdir(third_dir):
    os.rename(third_dir + file, clean_data_dir + 'third_' + file)
    
#print(files)
"""
for file in os.listdir(fourth_dir):
    os.rename(fourth_dir + file, clean_data_dir + 'fourth_' + file)

for file in os.listdir(fifth_dir):
    os.rename(fifth_dir + file, clean_data_dir + 'fifth_' + file)

for file in os.listdir(sixth_dir):
    os.rename(sixth_dir + file, clean_data_dir + 'sixth_' + file)

for file in os.listdir(seventh_dir):
    os.rename(seventh_dir + file, clean_data_dir + 'seventh_' + file)
    
for file in os.listdir(eigth_dir):
    os.rename(eigth_dir + file, clean_data_dir + 'eigth_' + file)