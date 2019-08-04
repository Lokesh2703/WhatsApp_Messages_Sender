from selenium import webdriver
import pyautogui
import time

driver= webdriver.Chrome(executable_path='C:\\Users\\Dell\\Downloads\\chromedriver_win32_2\\chromedriver')
driver.get('http://demo.guru99.com/test/upload/')

selector = driver.find_element_by_name('uploadfile_0')
selector.send_keys('C:\\Users\\Dell\\Pictures\\Saved Pictures\\car.jpg')

selector2 = driver.find_element_by_id('terms')
selector2.click()

selector2 = driver.find_element_by_id('submitbutton')
selector2.click()

time.sleep(5)
driver.quit()



