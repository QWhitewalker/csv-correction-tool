import csv

# writes array into row of file (appends)
def write_row(p_output,p_file,p_encoding,p_delimiter):
    with open(p_file, mode='a', encoding=p_encoding) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=p_delimiter)
        csv_writer.writerow(p_output)

# writes array into row of file (appends) (only writes columns that are listed in config file)
def write_validated_row(p_output,p_file,p_encoding,p_delimiter,p_columns_config):
    output = []

    for field in list(p_columns_config.keys()):
        output.append(p_output[int(field)])

    with open(p_file, mode='a', encoding=p_encoding) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=p_delimiter)
        csv_writer.writerow(output)

# writes array into row of file (appends) (only writes columns that are listed in config file) (adds header row that tells if field is valid)
def write_error_row(p_output,p_file,p_encoding,p_delimiter,p_columns_config,p_errors):
    output = []
    info = []

    for field in list(p_columns_config.keys()):
        output.append(p_output[int(field)])

    for field in list(p_columns_config.keys()):
        if field in p_errors:
            info.append("error")
        else:
            info.append("valid")

    with open(p_file, mode='a', encoding=p_encoding) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=p_delimiter)
        csv_writer.writerow(info)
        csv_writer.writerow(output)