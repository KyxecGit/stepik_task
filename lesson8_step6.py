from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    browser.get('https://SunInJuly.github.io/execute_script.html')

    # Находим элемент с переменной x и считываем текст
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text

    # Вычисляем результат
    y = calc(x)

    # Прокручиваем страницу до элемента ввода, чтобы убедиться, что он виден
    browser.execute_script("arguments[0].scrollIntoView(true);", x_element)

    # Вводим ответ в текстовое поле
    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_field.send_keys(y)

    # Прокручиваем страницу до checkbox и radiobutton, чтобы они были видны
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')

    browser.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    browser.execute_script("arguments[0].scrollIntoView(true);", radiobutton)

    # Отмечаем checkbox
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#robotCheckbox'))).click()

    # Выбираем radiobutton
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#robotsRule'))).click()

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit_button.click()

    # Даем время на выполнение
    time.sleep(5)

finally:
    # Закрываем браузер
    browser.quit()
