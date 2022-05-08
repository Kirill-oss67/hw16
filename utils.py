import json


def get_json_data(json_file):
    with open(json_file, 'r', encoding='UTF-8') as f:
        our_list = json.load(f)
        return our_list




