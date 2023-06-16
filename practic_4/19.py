https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python


def abbrev_name(name):
    first_name, last_name = name.split()
    return f"{first_name[0].upper()}.{last_name[0].upper()}"
