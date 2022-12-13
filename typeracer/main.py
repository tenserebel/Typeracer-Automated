# Importing the libraries
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from termcolor import colored

# If chromedriver error occurs. 
# driver = webdriver.Chrome('./chromedriver.exe')

driver = webdriver.Chrome() 
driver.get("https://play.typeracer.com/")

def website_starter():    
    html = driver.page_source
    return html


def find_text(data):
    html_content = data
    soup = BeautifulSoup(html_content,features="html.parser")
    span = soup.findAll("span")

    # Text to be typed
    text = ""

    for i in span:
        if "unselectable" in str(i):
            text += i.text 
    return text

delay = 0.10

def send_data(content):
    wait = WebDriverWait(driver, 15)
    elem = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "txtInput")))
    for i in content:
                time.sleep(delay)
                elem.send_keys(i)
    

flag = True
def main(flag):
    while flag:
        Starting_point = input("Enter y to start or e to exit: ")
        if Starting_point == "y":
            data = website_starter()
            content = find_text(data)
            text = colored("Started", "green", attrs=["bold", "blink"])
            print(text)
            print(content)
            send_data(content)
            
        else: 
            flag =False 
            text = colored("Ended", "red", attrs=["bold", "blink"])
            print(text)



if __name__ == "__main__":
    main(flag)