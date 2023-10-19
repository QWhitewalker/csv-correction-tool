def validate_charset():
    pass

def regex_validator(row, pattern):
    if pattern.match(row[1]):
        print("match")
    else:
        print("nomatch")