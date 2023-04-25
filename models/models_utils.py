from sqlalchemy.orm import Session, sessionmaker

from utils.exception import NoPrice
from .models import Product, Photo
from models.models import engine
from settings.settings import MARGIN
from utils.utils import search_and_slice_price, remove_art, remove_info_drop, get_topic_name


class Item:
    def __init__(self):
        self.sessionmaker = sessionmaker(bind=engine)
        self.session = self.sessionmaker()

    def add_item(self, sorted_data: dict):
        new_item = None
        for item in sorted_data['item'].values():
            try:
                for item_detail, length in zip(item, range(len(item))):
                    if length == 0:
                        cleaned_data_item = self.cleaned_data(item_detail)
                        new_item = Product(name=cleaned_data_item['name'],
                                           description=cleaned_data_item['description'],
                                           price=cleaned_data_item['price'])
                        self.session.add(new_item)
                        self.session.commit()
                        continue

                    new_photo_item = Photo(filename=item_detail, product_id=new_item.id)
                    self.session.add(new_photo_item)
            except NoPrice:
                continue
        self.session.commit()

    def clear_db(self):
        self.session.query(Product).delete()
        self.session.query(Photo).delete()
        self.session.commit()

    def get_all_data(self):
        self.all_data = {}
        query_result = self.session.query(Product, Photo).join(Photo, Product.id == Photo.product_id).all()

        for product, photo in query_result:
            product_id = product.id
            photo_data = {'filename': photo.filename}
            self.all_data.setdefault(product_id,
                            {'name': product.name, 'description': product.description, 'price': product.price,
                             'photos': []})['photos'].append(photo_data)

    def delete_element(self, id: int):
        product = self.session.query(Product).filter_by(id=id).first()
        photos = self.session.query(Photo).filter_by(product_id=id).all()
        self.session.delete(product)
        for photo in photos:
            self.session.delete(photo)
        self.session.commit()

    @staticmethod
    def cleaned_data(title):
        cleaned_data = dict()
        title = search_and_slice_price(title)
        cleaned_data['price'] = title['price']

        title = remove_art(title['cleaned_data'])

        title = remove_info_drop(title)

        title = get_topic_name(title)

        cleaned_data['name'] = title['name']
        cleaned_data['description'] = title['cleaned_data']

        return cleaned_data

    @staticmethod
    def add_margin(price):
        return price + (price/100*(MARGIN / 100))
