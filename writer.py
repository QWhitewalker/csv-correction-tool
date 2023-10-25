import csv

# writes array into row of file (appends)
def write_row(p_output,p_file,p_encoding,p_delimiter):
    with open(p_file, mode='a', encoding=p_encoding) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=p_delimiter)
        csv_writer.writerow(p_output)

# writes array into row of file (appends)
def write_validated_row(p_output,p_file,p_encoding,p_delimiter,p_columns_config):
    output = []
    for field in list(p_columns_config.keys()):
        output.append(p_output[int(field)])
    with open(p_file, mode='a', encoding=p_encoding) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=p_delimiter)
        csv_writer.writerow(output)

def write_error_row(p_error,p_output,p_file,p_encoding,p_delimiter):
    pass