from selenium import webdriver

driver= webdriver.Chrome(executable_path='/home/lokesh/Downloads/chromedriver')
driver.get('https://web.whatsapp.com/')

input('Enter anything after scanning QR code!!\n')
count = int(input('Enter the no.of users :'))
msg = input('Enter the message :')

for i in range(count):
    name = input('Enter the name of user or group: ')
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name('_13mgZ')
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
