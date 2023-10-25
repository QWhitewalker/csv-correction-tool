import csv
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

# delete error file if it already exists
if os.path.isfile(config['error-file']):
    os.remove(config['error-file'])

# open input file and call all other needed functions to process the file
with open(config['input-file'],encoding=config['encoding'],errors='replace') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=config['input-delimiter'])
    line_count = 0
    # loop through all the rows inside the file
    for row in csv_reader:
        # if its the first row
        if line_count == 0:
            # write row into output file
            writer.write_row(row,config['output-file'],config['encoding'],config['output-delimiter'])
            line_count += 1
        # if its not the first row
        else:
            # validate row
            validator_output = validator.regex_validator(row,config['columns'])
            # if the row is valid
            if validator_output[0]:
                # write row into output file
                writer.write_row(row,config['output-file'],config['encoding'],config['output-delimiter'])
            # if the row contains errors
            else:
                # write indeces of columns with errors into output file
                writer.write_row(validator_output[1],config['error-file'],config['encoding'],config['output-delimiter'])
            line_count += 1
            # only process that many rows (from the top) if number-of-rows isn't null
            if not config['number-of-rows'] is None:
                if line_count == config['number-of-rows'] + 1:
                    break
    # print count of processed rows into terminal
    print(f'Processed {line_count-1} lines.')