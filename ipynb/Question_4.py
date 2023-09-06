def transform(string):
    if len(string) < 2:
        return ""
    else:
        return string[0:2] + string[-2:]

