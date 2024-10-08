import re

test_text = '''{name} ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}'''

list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']


def verify_keys(test_text, list_keys) -> str:
    found_keys = re.findall(r'\{(.*?)\}', test_text)

    for key in found_keys:
        if key not in list_keys:
            return f"Ошибка: некорректный ключ '{key}'"

    if test_text.count('{') != test_text.count('}'):
        return "Ошибка: не совпадает количество открывающих и закрывающих скобок"

    return "Тест пройден успешно"


result = verify_keys(test_text, list_keys)
print(result)
