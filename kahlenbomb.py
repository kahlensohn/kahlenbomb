from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def banner():
    print('''
 /$$   /$$           /$$       /$$                     /$$                               /$$      
| $$  /$$/          | $$      | $$                    | $$                              | $$      
| $$ /$$/   /$$$$$$ | $$$$$$$ | $$  /$$$$$$  /$$$$$$$ | $$$$$$$   /$$$$$$  /$$$$$$/$$$$ | $$$$$$$ 
| $$$$$/   |____  $$| $$__  $$| $$ /$$__  $$| $$__  $$| $$__  $$ /$$__  $$| $$_  $$_  $$| $$__  $$
| $$  $$    /$$$$$$$| $$  \ $$| $$| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \ $$| $$ \ $$ \ $$| $$  \ $$
| $$\  $$  /$$__  $$| $$  | $$| $$| $$_____/| $$  | $$| $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$
| $$ \  $$|  $$$$$$$| $$  | $$| $$|  $$$$$$$| $$  | $$| $$$$$$$/|  $$$$$$/| $$ | $$ | $$| $$$$$$$/
|__/  \__/ \_______/|__/  |__/|__/ \_______/|__/  |__/|_______/  \______/ |__/ |__/ |__/|_______/ 
		''')


def main():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))  # 2nd change
    driver.get('https://web.whatsapp.com/')

    name = input('Enter the name of user or group: ')
    msg = input('Enter your message: ')
    count = int(input('Enter the count: '))

    input('Enter any key after scanning QR code')

    user = driver.find_element(by=By.XPATH, value='//span[@title = "{}"]'.format(name))
    user.click()

    # The classname of message box may vary.
    msg_box = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')

    for i in range(count):
        for j in range(len(msg)):
            msg_box.send_keys(msg[j])
        # The classname of send button may vary.
        button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        button.click()
    print('Bombing Complete!!')


banner()
main()
