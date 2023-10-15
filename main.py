import csv
import re
import json

# load config.json into python dictionary "config"
configFile = open('config.json')
config = json.load(configFile)

pattern = re.compile(config["columns"]["1"])

def regex_validator():
    if pattern.match(row[1]):
        print("match")
    else:
        print("nomatch")

with open(config["csv-file"]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(row[1])

            line_count += 1
        else:
            print(row[1])
            regex_validator()
            line_count += 1
            #if line_count == 5:
                #break
            #print(f'Processed {line_count} lines.')
    print(f"Processed {line_count} lines.")

def charset_validator():
    pass

def regex_corrector():
    pass

def error_writer():
    pass

def output_writer():
    pass