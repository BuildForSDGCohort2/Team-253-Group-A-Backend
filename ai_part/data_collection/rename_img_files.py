# This piece of code is used to rename image files and move them to a specific folder.

import os

root_dir = './covidTrash'
directory = './covidTrash/as_trash_clean_v1.clean/'
clean_data_dir = './covidTrash/cleaned_data/'

for file in os.listdir(directory):
    os.rename(directory + file, clean_data_dir + 'number_of_dir' + file)