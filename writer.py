import csv

def write(output,encoding):
    with open('output.csv', mode='a', encoding=encoding) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerow(output)

def write_error():
    pass