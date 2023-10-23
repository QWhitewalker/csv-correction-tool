import csv
import re
import json
import validator
import writer
import os

# load config.json into python dictionary 'config'
configFile = open('config.json')
config = json.load(configFile)

# delete output file if it already exists
if os.path.isfile(config['output-file']):
    os.remove(config['output-file'])


pattern = re.compile(config['columns']['1'])

# open input file and call all other needed functions to process the file
with open(config['input-file'],encoding=config['encoding'],errors='replace') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=config['input-delimiter'])
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            writer.write_row(row,config['output-file'],config['encoding'],config['output-delimiter'])
            line_count += 1
        else:
            writer.write_row(row,config['output-file'],config['encoding'],config['output-delimiter'])
            #validator.regex_validator(row, pattern)
            line_count += 1
            if line_count == 5:
                break
print(f'Processed {line_count} lines.')
#print(config['columns'].keys())

def regex_corrector():
    pass