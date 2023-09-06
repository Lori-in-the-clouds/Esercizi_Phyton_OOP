def control_password(string):
    if len(string) < 6 or len(string) > 12:
        return False
    if not string.isnumeric() and not string.isalpha():
        return False
    return True


print(control_password("222223"))
