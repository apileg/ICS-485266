import codecs
import json

from excel_reader import get_data


def to_json():
    data = get_data()
    numpy_to_list = data.values.tolist()

    filepath = "./to_json.json"

    json.dump(numpy_to_list, codecs.open(filepath, 'w', encoding='utf8', errors='strict'),
              sort_keys=True,
              indent=4, default=str)
