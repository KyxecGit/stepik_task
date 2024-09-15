from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import math
import time

# Функция для вычисления ответа капчи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Путь к вашему WebDriver
driver_path = 'path/to/your/webdriver'

# Создаем экземпляр браузера
browser = webdriver.Chrome()

try:
    # Открываем страницу
    browser.get('http://suninjuly.github.io/alert_accept.html')

    # Нажимаем на кнопку, чтобы вызвать confirm
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

    # Принять confirm
    alert = Alert(browser)
    alert.accept()

    # На новой странице решаем капчу
    # Находим элемент с переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text

    # Вычисляем результат
    y = calc(x)

    # Вводим ответ в текстовое поле
    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit_button.click()

    # Даем время на выполнение
    time.sleep(5)

finally:
    # Закрываем браузер
    browser.quit()
