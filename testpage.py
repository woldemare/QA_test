from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import requests
import random
import string
import shutil
import time

class Netpeak:
    def __init__(self, driver):
        self.driver = driver
        self.url_to_png = 'https://cdn.icon-icons.com/icons2/1812/PNG/512/4213444-extension-file-format-png-type_115361.png'
        self.input_file_locator = '//input[@type="file"]'
        self.birthday_day = '//*[@id="user-main-info"]/div[11]/div[2]/select/option[12]'
        self.birthday_month = '//*[@id="user-main-info"]/div[11]/div[3]/select/option[6]'
        self.birthday_year = '//*[@id="user-main-info"]/div[11]/div[4]/select/option[6]'
        self.netpeak_courses = 'https://school.netpeak.group'

    def input_png_file(self):
        response = requests.get(self.url_to_png, stream=True)
        with open('file_4213.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        path_to_png = os.path.abspath("file_4213.png")
        self.driver.find_element(By.XPATH, self.input_file_locator).send_keys(path_to_png)
        file_msg = self.driver.find_element(By.ID, "up_file_name")
        time.sleep(5)
        assert file_msg.text == "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf).", \
                "The resume file was uploaded in incorrect format"
        print("The resume file was uploaded in incorrect format")
        
    def form(self):
        random_letters = string.ascii_lowercase
        print ( ''.join(random.choice(random_letters)))
        self.driver.find_element(By.ID, 'inputName').send_keys(random_letters)
        print ( ''.join(random.choice(random_letters) for i in range(1)))
        self.driver.find_element(By.ID, 'inputLastname').send_keys(random_letters)
        email = string.ascii_lowercase + "@gmail.com"
        print ( ''.join(random.choice(email) for i in range(1)))
        self.driver.find_element(By.ID, 'inputEmail').send_keys(email)
        phone_number = "+38" + string.digits
        print ( ''.join(random.choice(phone_number) for i in range(1)))
        self.driver.find_element(By.ID, 'inputPhone').send_keys(phone_number)
        self.driver.find_element(By.XPATH, self.birthday_day).click()
        self.driver.find_element(By.XPATH, self.birthday_month).click()
        self.driver.find_element(By.XPATH, self.birthday_year).click()

        self.driver.find_element(By.ID, 'agree_rules').click()
        self.driver.find_element(By.ID, 'submit').click()

    def check_error_color(self):
        error_color = self.driver.find_element(By.CLASS_NAME, 'warning-fields').value_of_css_property('color')
        print(error_color)
        assert error_color == 'rgba(255, 0, 0, 1)', "The color of warning field is not red"
        print("The color of warning field is red")

    def courses(self):
        self.driver.get(self.netpeak_courses)
        courses = self.driver.current_url
        assert courses == "https://school.netpeak.group/", "Error loading courses tab"
        print("Netpeak Education Center is loaded")