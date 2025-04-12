import json


def reverse_json(json_file: str):
    """
    """
    import json
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    reversed_data = {}
    for key, value in data.items():
        reversed_data[value] = key
    
    with open("reversed_data.json", "w", encoding="windows-1252") as f:
        json.dump(reversed_data, f, indent=4)


def ascii_256_mapper_creation(lvl_1_json_path = r"C:/Users/axelo/Documents/Projects/level-auto-encoder/sprites_token/full_token/level_1_full_token.json"):

    with open(lvl_1_json_path, "r") as f:
        lvl_1_json = json.load(f)

    keys = list(lvl_1_json.keys())
    start_unicode = 0x0100  # 'Ā' (Latin Extended-A)
    dictionary_mapping = {key: chr(start_unicode + i) for i, key in enumerate(keys)}

    with open("ascii_mapping.json", "w", encoding="utf-8") as f:
        json.dump(dictionary_mapping, f, indent=4, ensure_ascii=False)

    print("Mapping saved to ascii_mapping.json")