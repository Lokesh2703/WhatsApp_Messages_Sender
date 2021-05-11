from selenium import webdriver
import pandas as pd
import csv

driver= webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://web.whatsapp.com/')

input('Enter anything after scanning QR code!!\n')
# name = input('Enter the name :')
# names= []
# names.append(name)
# name = input('Enter the name :')
# names.append(name)
group_name = input('Enter the group name :')

file_nm = input('Enter the filename(with extension): ')
file = pd.read_csv(file_nm)
names = file.iloc[:,0]

user = driver.find_element_by_xpath('//div[@title="{}"]'.format('Menu'))
user.click()

button2 = driver.find_element_by_xpath('//div[@aria-label="{}"]'.format('New group'))
button2.click()

for name in names:
    msg_box=driver.find_element_by_class_name('_38sK8')
    msg_box.send_keys(name)

    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()

button3 = driver.find_element_by_class_name('SncVf')
button3.click()

msg_box=driver.find_element_by_class_name('_2_1wd')
msg_box.send_keys(group_name)

button3 = driver.find_element_by_class_name('SncVf')
button3.click()