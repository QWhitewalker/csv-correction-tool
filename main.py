import csv
import re
import json
import validator
import writer

# load config.json into python dictionary 'config'
configFile = open('config.json')
config = json.load(configFile)

pattern = re.compile(config['columns']['1'])

with open(config['csv-file'], encoding=config['encoding'], errors='replace') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=config['delimiter'])
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            writer.write_row(row,config['encoding'])
            line_count += 1
        else:
            writer.write_row(row,config['encoding'])
            #validator.regex_validator(row, pattern)
            line_count += 1
            if line_count == 5:
                break
    print(f'Processed {line_count} lines.')
#print(config['columns'].keys())

def regex_corrector():
    pass