from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Функция для вычисления ответа капчи
def calc(x):
    try:
        x = int(x)
        result = str(math.log(abs(12 * math.sin(x))))
        return result
    except Exception as e:
        print(f"Error in calc function: {e}")
        return ""

# Путь к вашему WebDriver
driver_path = 'path/to/your/webdriver'

# Создаем экземпляр браузера
browser = webdriver.Chrome()

try:
    # Открываем страницу
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # Ожидаем, пока текст элемента с ценой станет равен "$100"
    price_element = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    print("Price is now $100, proceeding to click 'Book'")

    # Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    # Находим элемент с переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    print(f"Value of x: {x}")  # Отладочный вывод

    # Вычисляем результат
    y = calc(x)
    print(f"Calculated y: {y}")  # Отладочный вывод

    if not y:
        print("Calculation failed or returned an empty result")
    else:
        # Вводим ответ в текстовое поле
        input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
        input_field.send_keys(y)

        # Нажимаем кнопку Submit
        submit_button = browser.find_element(By.CSS_SELECTOR, '#solve')
        submit_button.click()

        # Даем время на выполнение
        time.sleep(5)

finally:
    # Закрываем браузер
    browser.quit()
