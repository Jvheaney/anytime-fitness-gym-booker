from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager
import time
import datetime

keyfob = ""
lastname = ""
delay = 20
desired_time = ""
member_sign_in_page = ""
club_page = ""

date_1 = datetime.datetime.strptime(datetime.date.today().strftime('%Y-%m-%d'), "%Y-%m-%d")

selection_date_p = date_1 + datetime.timedelta(days=2)

selection_date = selection_date_p.strftime('%Y-%m-%d')

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get(member_sign_in_page)
keyfob_input = driver.find_element_by_name("keyfob")
keyfob_input.send_keys(keyfob)
lastname_input = driver.find_element_by_name("lastName")
lastname_input.send_keys(lastname)
lastname_input.send_keys(Keys.ENTER)

time.sleep(10)

driver.get(club_page);

time.sleep(10)

timeslot_input = driver.find_element_by_xpath("//*[contains(text(), '" + desired_time + "')][@data-day_ident='" + selection_date + "']")

actions = ActionChains(driver)
driver.execute_script("arguments[0].scrollIntoView();", timeslot_input)
time.sleep(2)
actions.click(timeslot_input).perform()
time.sleep(5)
confirm_input = driver.find_element_by_xpath("//*[contains(text(), '" + desired_time + "')][@data-day_ident='" + selection_date + "']/following-sibling::a[@class='res-timeslot-confirm']")

time.sleep(1)
driver.execute_script("arguments[0].click();", confirm_input)

time.sleep(10)
driver.quit()
