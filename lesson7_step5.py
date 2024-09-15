from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import math
import time

# Функция для вычисления ответа
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Путь к вашему WebDriver
driver_path = 'path/to/your/webdriver'

# Создаем экземпляр браузера
browser = webdriver.Chrome()

try:
    # Открываем страницу
    browser.get('https://suninjuly.github.io/math.html')

    # Находим элемент с переменной x и считываем текст
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text

    # Вычисляем результат
    y = calc(x)

    # Вводим ответ в текстовое поле
    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(y)

    # Отмечаем checkbox
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()

    # Выбираем radiobutton
    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton.click()

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit_button.click()

    # Даем время на выполнение
    time.sleep(5)

finally:
    # Закрываем браузер
    browser.quit()
