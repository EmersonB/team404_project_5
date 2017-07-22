import json

def gen_message(dict_obj):
    '''
    Generate JSON file
    '''
    json_file = json.dumps( dict_obj, indent=2, sort_keys=True)
    return json_file

test_dict = {"temp":24.5, "humidity":0.12}

print gen_message(test_dict)
