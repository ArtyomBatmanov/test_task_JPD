def find_differences(json_old, json_new, diff_list) -> dict:
    differences = {}

    for key in diff_list:
        old_value = json_old['data'].get(key)
        new_value = json_new['data'].get(key)

        if old_value != new_value:
            differences[key] = new_value

    return differences


json_old = {
    'company_id': 111111,
    'resource': 'record',
    'data': {
        'services': [{'id': 9035445, 'title': 'Стрижка', 'cost': 1500}],
        'staff': {'id': 1819441, 'name': 'Мастер'},
        'datetime': '2022-01-25T11:00:00+03:00'
    }
}

json_new = {
    'company_id': 111111,
    'resource': 'record',
    'data': {
        'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500}],
        'staff': {'id': 1819441, 'name': 'Мастер'},
        'datetime': '2022-01-25T13:00:00+03:00'
    }
}

diff_list = ['services', 'staff', 'datetime']

result = find_differences(json_old, json_new, diff_list)
print(result)
