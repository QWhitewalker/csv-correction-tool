import re

"""
takes a row and part of the config.json as argument
returns array
first element of array is a boolean that indicates if everything is valid
second element of array is a array that contains the index of all columns that contain errors
"""
def regex_validator(p_row,p_columns_config):
    # define default return value
    return_value = [True,[]]
    # loop through all columns that are registered inside config.json
    for field in list(p_columns_config.keys()):
        # read  regex pattern for current colum out of config.json
        pattern = re.compile(p_columns_config[field])
        #compare value with regex pattern (no match -> set False + append column index to array)
        if not pattern.match(p_row[int(field)]):
            return_value[0] = False
            return_value[1].append(field)
    return return_value