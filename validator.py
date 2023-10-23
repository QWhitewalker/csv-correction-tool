def regex_validator(p_row,p_pattern):
    if p_pattern.match(p_row[1]):
        return_value = (True,[''])
    else:
        return_value = (False,['1'])
    return return_value