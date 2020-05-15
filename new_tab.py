from selenium import  webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
from time import sleep


driver = webdriver.Chrome('C:\\Users\\SHUBH\\Desktop\\chromedriver.exe')
driver.get("https://www.instagram.com/accounts/emailsignup/")
sleep(2)



driver.execute_script("window.open('');")

driver.switch_to_window(driver.window_handles[1])
driver.get("https://temp-mail.org/en/")

sleep(5)
driver.find_element_by_xpath('//*[@id="mail"]').click()
driver.find_element_by_xpath('//*[@id="mail"]').send_keys(Keys.CONTROL,'c')
sleep(2)

driver.switch_to_window(driver.window_handles[0])

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input') \
    .send_keys(Keys.CONTROL, 'v')
sleep(4)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input') \
    .send_keys("Saurabh Tiwari")
sleep(5)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input') \
    .send_keys("desi_bond420")
sleep(5)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input') \
    .send_keys("carypaul18")
sleep(6)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button') \
    .click()
sleep(4)

driver.implicitly_wait(5)


driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select').click()
sleep(2)
day =Select(driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select'))
day.select_by_value('15')
sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select').click()

sleep(1)
month =Select(driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select'))
month.select_by_value('3')
sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select').click()
sleep(1)
year =Select(driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select'))
year.select_by_value('1999')
sleep(3)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button') \
    .click()
sleep(2)


