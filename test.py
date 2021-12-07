from selenium import webdriver
import time
driver = webdriver.Chrome('C:/Users/User/PycharmProjects/itdashboard/chromedriver.exe')

driver.get('https://itdashboard.gov/')
dive_in = driver.find_element_by_xpath('//*[@id="node-23"]/div/div/div/div/div/div/div/a').click()



time.sleep(10)

driver.close()
