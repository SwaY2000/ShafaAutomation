from models.models_utils import Item
from selenium_utils.utils import Shafa
from telegram_parsing.telegram_utils import ParsingTelegram


class StartBot:
    def __init__(self):
        self.Item = Item()
        self.Shafa = Shafa()
        self.ParsingTelegram = ParsingTelegram()

    def parsing_item_from_tg(self):
        self.ParsingTelegram.parsing_data()

    def add_item(self):
        if hasattr(self.ParsingTelegram, 'sorting_data'):
            self.Item.add_item(self.ParsingTelegram.sorting_data)
        else:
            raise Exception('Parsing data from tg is empty')

    def fill_shafa(self):
        self.Item.get_all_data()
        self.Shafa.connect_to_shafa()
        self.Shafa.login()
        for item, id in zip(self.Item.all_data.values(), self.Item.all_data.keys()):
            self.Shafa.add_item(item)
            self.Item.delete_element(id)




if __name__ == '__main__':
    bot = StartBot()
    bot.parsing_item_from_tg()
    bot.add_item()
    bot.fill_shafa()