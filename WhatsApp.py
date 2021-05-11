from selenium import webdriver

driver= webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group: ')
msg = input('Enter the message :')
count = int(input('Enter the count :'))

input('Enter anything after scanning QR code!!\n')

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_1E0Oz')
    button.click()