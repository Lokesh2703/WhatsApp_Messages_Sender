from selenium import webdriver
import pandas as pd
import csv

driver= webdriver.Chrome(executable_path='C:\\Users\\Dell\\Downloads\\chromedriver_win32_2\\chromedriver')
driver.get('https://web.whatsapp.com/')

input('Enter anything after scanning QR code!!\n')
msg = input('Enter the message :')

n=int(input('''Enter :
"1" : If u want to enter the names manually 
"2"  : If u want to enter the .csv file name :'''))
if n==1:
    count = int(input('Enter the no.of users :'))
    for i in range(count):
        name = input('Enter the name of user or group: ')
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        user.click()
        msg_box = driver.find_element_by_class_name('_13mgZ')
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()

elif n==2:
    file_nm = input('Enter the filename(with extension): ')
    file = pd.read_csv(file_nm)
    names = file.iloc[:,0]

    for name in names:
        # print(name)
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        user.click()
        msg_box = driver.find_element_by_class_name('_13mgZ')
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
