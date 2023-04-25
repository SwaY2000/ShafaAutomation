# coding: utf8
import re

from utils.exception import NoPrice


def search_and_slice_price(title):
    price_pattern = r"(Ціна|ціна|Цена|цена)\s*:?(\s*\d+)\s*(грн|гривна|грівна)?"
    price = re.search(price_pattern, title)
    if price:
        title = re.sub(price_pattern, "", title)  # удаляем совпадения из текста
        return {'price': price.group(2),
                'cleaned_data': title.strip()}
    else:
        raise NoPrice('Price not found')


def remove_art(title):
    return re.sub(r'Арт[\d\-\s]*', '', title)


def remove_info_drop(title, to_remove: str = '📢Номери для замовлення ⬇️💁🏼‍♀️Менеджер: @dropolga'):
    return title.replace(to_remove, '')


def get_topic_name(title):
    paragraphs = title.split('\n')
    if paragraphs:
        lines = paragraphs[0].split('\n')
        first_line = lines[0]
        return {'name': first_line,
                'cleaned_data': title}
    else:
        return None
