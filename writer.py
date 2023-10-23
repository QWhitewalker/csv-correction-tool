import csv

def write_row(p_output,p_file,p_encoding):
    with open(p_file, mode='a', encoding=p_encoding) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerow(p_output)