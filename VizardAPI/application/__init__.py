# TODO File

# todo database to constructor

# todo userdata

# todo save db


import re


def to_snake_case(name: str):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def data_to_snake(data):
    snake_case_data = {}
    for key in data.keys():
        snake_case_data[to_snake_case(key)] = data[key]
    return snake_case_data
