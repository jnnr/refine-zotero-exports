import json
from collections.abc import Iterable


def load_json(filepath):
    with open(filepath, "r") as file:
        dictionary = json.load(file)

    return dictionary
    
def format_tags(_list):
    list_of_content = ['"' + str(item["tag"]) + '"' for item in _list if "tag" in item]

    return "|".join(list_of_content)

def compress_notes(_list):
    if not isinstance(_list, Iterable):
        _list = []

    list_of_content = [item["note"] for item in _list if "note" in item]

    return " ".join(list_of_content)
