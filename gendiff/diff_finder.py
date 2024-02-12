import json
from gendiff.parser import parse_data_from_file
from gendiff.generate import generate
from gendiff.formatters.choice_formatter import format_diff



def generate_diff(path_to_file1, path_to_file2, formatter='stylish'):
    # print('контрольная точка --> вход в generate_diff')
    content_file_1 = parse_data_from_file(path_to_file1)
    content_file_2 = parse_data_from_file(path_to_file2)
    # print('content_file_1=',content_file_1)
    # print('content_file_2=',content_file_2)
    #content_file_2 = json.load(open(path_to_file2))
    diff = generate(content_file_1, content_file_2)
    return format_diff(diff, formatter)

    
    
    
    '''
    content_file_3 = {}
    for k, v in sorted(content_file_1.items()):
        if k not in content_file_2:
            k =" - " + str(k)
            content_file_3[k] = v
        if k in content_file_2 and content_file_1[k] != content_file_2[k]:
            content_file_3[" - " + str(k)] = v
            content_file_3[" + " + str(k)] = content_file_2[k]
        if k in content_file_2 and content_file_1[k] == content_file_2[k]:
            content_file_3[k] = v
        if k in content_file_2 and content_file_1[k] == content_file_2[k]:
            content_file_3[k] = v
    key_not_in_content_file_1 = list(set(content_file_2).difference(set(content_file_1)))
    for i in key_not_in_content_file_1:
        if i in content_file_2:
            content_file_3[" + "+str(i)] = content_file_2[i]

    #return content_file_3
    content_file_4 = json.dumps(content_file_3)
    if 'true' in content_file_4:
        content_file_4 = content_file_4.replace('true','True')
    if 'false' in content_file_4:
        content_file_4 = content_file_4.replace('false', 'False')
    return content_file_4
    '''
    '''
    data = {'name': 'Russia', 'phone_code': 7, 'capital': 'Moscow', 'currency': 'RUB'}
    json_data = json.dumps(data) # сериализуем словарь data в json строку
    print(type(json_data))
    print(json_data)
    '''
