import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


#region 2.2.3
try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/selects1.html")
    num1 = driver.find_element_by_id("num1").text
    num2 = driver.find_element_by_id("num2").text
    summ = str(int(num1) + int(num2))
    driver.find_element_by_id("dropdown").click()
    select = Select(driver.find_element_by_tag_name("select"))
    select.select_by_visible_text(summ)

    button = driver.find_element_by_xpath('//*[@type="submit"]')
    button.click()


finally:
    time.sleep(10)
    driver.quit()
#endregion


#region 2.2.6

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/execute_script.html")

    x = int(driver.find_element_by_id("input_value").text)
    y = calc(x)
    driver.find_element_by_id("answer").send_keys(y)
    driver.find_element_by_id("robotCheckbox").click()

    button = driver.find_element_by_id("robotsRule")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    button2 = driver.find_element_by_xpath('//*[@type="submit"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()


finally:
    time.sleep(10)
    driver.quit()

# endregion


#region 2.2.8
try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/file_input.html")


    driver.find_element_by_name("firstname").send_keys("AAA")
    driver.find_element_by_name("lastname").send_keys("AAA")
    driver.find_element_by_name("email").send_keys("AAA")

    element = driver.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'name.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button2 = driver.find_element_by_xpath('//*[@type="submit"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()


finally:
    time.sleep(10)
    driver.quit()

#endregion


#region 2.4
try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    driver.find_element_by_id("book").click()

    x = int(driver.find_element_by_id("input_value").text)
    driver.find_element_by_id("answer").send_keys(calc(x))

    driver.find_element_by_id("solve").click()


finally:
    time.sleep(30)
    driver.quit()

#endregion