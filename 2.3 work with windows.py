from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #Открыть браузер
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    #Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, 'button.trollface').click()

    #Переключится на новую вкладку
    second_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(second_window)

    #На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element(By.ID, 'input_value').text
    x = x_element
    y = calc(x)
    input_pole = browser.find_element(By.ID, "answer").send_keys(y)

    # Нажать на кнопку
    button2 = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла