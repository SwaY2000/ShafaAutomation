from telethon.sync import TelegramClient

from settings.settings import TELEGRAM_APP_API_ID, TELEGRAM_APP_API_HASH, CHANNEL_URL, PATH_TO_MEDIA_FOLDER


class ParsingTelegram:
    API_ID = TELEGRAM_APP_API_ID
    API_HASH = TELEGRAM_APP_API_HASH

    def __init__(self, link: str = CHANNEL_URL, limit: int = 134):
        self.client = TelegramClient('my_session', ParsingTelegram.API_ID, ParsingTelegram.API_HASH)
        self.client.start()
        self.channel = self.client.get_entity(link)
        self.messages = self.client.get_messages(self.channel, limit=limit)
        self.sorting_data = {'item': dict(), }

    def parsing_data(self):
        id_item = None
        for message in self.messages:
            if message.text:
                self.sorting_data['item'][message.id] = [message.text, ]
                id_item = message.id
            if message.photo:
                if self.sorting_data['item'].get(id_item) and len(self.sorting_data['item'].get(id_item)) <= 10:
                    self.sorting_data['item'][id_item].append(f'{message.photo.id}.jpg')
                    self.client.download_media(message, file=f'{PATH_TO_MEDIA_FOLDER}/photo/{message.photo.id}.jpg')
                continue

    def clear_data_dict(self):
        self.sorting_data = {'item': dict(), }






if __name__ == '__main__':
    parsing = ParsingTelegram()
    parsing.parsing_data()
    print(parsing.sorting_data)
