from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pypresence import Presence
from re import findall
import time

client_id = "791950538849648641"

RPC = Presence(client_id)
RPC.connect()
RPC.update(state="Just browsing",large_image="logo")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

chrome_options.add_argument("--hide-scrollbars --disable-extensions --app=https://www.animelab.com/home")

driver = webdriver.Chrome(chrome_options=chrome_options)

# LOGIN INFO
infoFile = open("loginInfo.txt").read().split('\n')
username = infoFile[0]
password = infoFile[1]

done = True
while done:
    try:
        loginBtn = driver.find_element_by_class_name("account-login")
        loginBtn.click()
        done = False
    except:
        pass

done = True
while done:
    try:
        emailBox = driver.find_element_by_id("modal-email")
        done = False
    except:
        pass

emailBox = driver.find_element_by_id("modal-email")
passBox = driver.find_element_by_id("modal-password")
signIn = driver.find_elements_by_class_name("btn-signin")

print(emailBox)
time.sleep(0.1)
emailBox.click()
time.sleep(0.1)
emailBox.send_keys(username)
time.sleep(0.1)
passBox.click()
time.sleep(0.1)
passBox.send_keys(password)
time.sleep(0.1)
print(signIn)
signIn[0].click()

lock = True
showTitle = ""
try:
    while True:
        time.sleep(1)
        if(len(findall("https:\/\/www.animelab.com\/player\/.+",driver.current_url))):
            URL = driver.title.split("|")
            showTitle = URL[0]
            showTitle = "Watching " + showTitle
            episodeName = URL[1]
            #timeIn = driver.find_element_by_class_name("vl-current-time").text
            #timeTotal = driver.find_element_by_class_name("vl-total-time").text

            #try:
            #    print((int(timeIn.split(':')[0].replace('s',"")) * 60) + int(timeIn.split(':')[1].replace('s',"")))
            #except:
            #    pass
            RPC.update(details=showTitle,state=episodeName,large_image="logo")
        else:
            RPC.update(state="Just browsing",large_image="logo")
            lock = True
except:
    RPC.close()
    driver.quit()