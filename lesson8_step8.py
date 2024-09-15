from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Путь к вашему WebDriver
driver_path = 'path/to/your/webdriver'

# Путь к файлу, который нужно загрузить
file_path = 'a.txt'

# Создаем экземпляр браузера
browser = webdriver.Chrome()

try:
    # Открываем страницу
    browser.get('http://suninjuly.github.io/file_input.html')

    # Находим текстовые поля и заполняем их
    first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')

    first_name.send_keys('John')
    last_name.send_keys('Doe')
    email.send_keys('john.doe@example.com')

    # Находим поле для загрузки файла и загружаем файл
    file_input = browser.find_element(By.CSS_SELECTOR, '#file')
    file_input.send_keys(os.path.abspath(file_path))

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit_button.click()

    # Даем время на выполнение
    time.sleep(5)

finally:
    # Закрываем браузер
    browser.quit()
