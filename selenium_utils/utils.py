import re
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

from settings.settings import USER_NAME_SHAFA, PASSWORD_SHAFA, PATH_TO_MEDIA_FOLDER, MARGIN


class Shafa:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--window-size=1920,1080')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--charset=UTF-8')

        self.driver = webdriver.Chrome(options=self.options)

    def connect_to_shafa(self, link: str = 'https://shafa.ua/'):
        self.driver.get(link)

    def login(self, link: str = 'https://shafa.ua/uk/login'):
        self.driver.get(link)
        time.sleep(2)
        input_login = self.driver.find_element(By.NAME, 'username')
        input_login.send_keys(USER_NAME_SHAFA)
        input_password = self.driver.find_element(By.NAME, 'password')
        input_password.send_keys(PASSWORD_SHAFA)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/form/button')
        login_button.click()
        time.sleep(3)

    def add_item(self, data_for_fill: dict, link: str = 'https://shafa.ua/uk/new'):
        time.sleep(5)
        self.driver.get(link)
        time.sleep(2)
        upload_button = self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/form/div[1]/div[2]/div[2]/button'
        )
        self.driver.execute_script("arguments[0].click();", upload_button)

        for photo in data_for_fill['photos']:
            photo_name = photo['filename']
            upload_button = self.driver.find_element(By.ID, 'upload-img')
            upload_button.send_keys(f'{PATH_TO_MEDIA_FOLDER}\\photo\\' + photo_name)

            upload_button = self.driver.find_element(By.ID, 'upload-img')
            upload_button.clear()
            time.sleep(1)

        name_item = self.driver.find_element(By.ID, 'product-name')
        name_item.send_keys(re.sub(r'[^\u0000-\uFFFF]', '', data_for_fill['name']))

        name_description = self.driver.find_element(By.ID, 'product-description')
        name_description.send_keys(re.sub(r'[^\u0000-\uFFFF]', '', data_for_fill['description']))

        item_condition = self.driver.find_element(By.XPATH, '//*[@id="product-condition"]/div/div[2]/div')
        item_condition.click()
        item_condition_new = self.driver.find_element(By.ID, 'react-select-2-option-0')
        item_condition_new.click()

        item_gender = self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/form/div[4]/div[2]/div[1]'
        )
        item_gender.click()

        item_category = self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/form/div[5]/div[2]/ul/li[1]'
        )
        item_category.click()
        item_category_detailed = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/ul/li[1]/div/a')
        item_category_detailed.click()

        wait = WebDriverWait(self.driver, 5)
        item_several_size_checkbox = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/form/div[6]/div[1]/label")))
        item_several_size_checkbox.click()
        item_general_size = self.driver.find_element(
            By.CLASS_NAME, 'cNY9janEoOAroChx6Zjv'
        )
        item_general_size.click()

        item_color = self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/form/div[7]/div[2]/ul/li[17]'
        )
        item_color.click()

        item_quantity = self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/form/div[9]/div/div/span[1]/input'
        )
        item_quantity.clear()
        item_quantity.send_keys(10)

        item_price = self.driver.find_element(By.ID, 'price')
        item_price.send_keys(round(data_for_fill['price']+(data_for_fill['price']*(MARGIN/100))))

        item_price_button = self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/form/div[10]/div[2]/label[1]'
        )
        item_price_button.click()

        time.sleep(3)

        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'body > div.b-layout > div.b-layout__content > div:nth-child(3) > div > form > div.b-form-row.b-add-product__footer > button')
        submit_button.click()

        without_ads = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div/a[1]')
                                           )
        )
        without_ads.click()



if __name__ == '__main__':
    shafa = Shafa()
    shafa.connect_to_shafa()
    shafa.login()
    shafa.add_item()
    time.sleep(1000)