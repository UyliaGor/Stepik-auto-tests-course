from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x1,x2):
  return str(int(x1) + int(x2))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    x_element1 = browser.find_element_by_id('num1')
    x1 = x_element1.text
    x_element2 = browser.find_element_by_id('num2')
    x2 = x_element2.text

    sum = calc(x1,x2)



    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum)  # ищем элемент с текстом "Python"


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn-default')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



# не забываем оставить пустую строку в конце файла
