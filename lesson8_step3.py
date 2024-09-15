from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Путь к вашему WebDriver
driver_path = 'path/to/your/webdriver'

# Создаем экземпляр браузера
browser = webdriver.Chrome()

try:
    # Открываем страницу
    browser.get('https://suninjuly.github.io/selects1.html')

    # Находим элементы с числами
    num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text

    # Вычисляем сумму чисел
    total = int(num1) + int(num2)

    # Находим выпадающий список и создаем объект Select
    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))

    # Выбираем значение в выпадающем списке, которое равно рассчитанной сумме
    select.select_by_visible_text(str(total))

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn')
    submit_button.click()

    # Даем время на выполнение
    time.sleep(5)

finally:
    # Закрываем браузер
    browser.quit()
