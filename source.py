from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# from selenium.webdriver.common.keys import Keys

#u can use these to dont show webdrive
#option = webdriver.ChromeOptions()
#option.add_argument('headless')
#dev = webdriver.Chrome(options=option)

dev = webdriver.Chrome('chromedriver.exe')
dev.get("https://web.shad.ir/#/login")
number = "9186716654"

(WebDriverWait(dev, 20).until(EC.presence_of_element_located((By.NAME, 'phone_number')))).send_keys(number)
(WebDriverWait(dev,10).until(EC.presence_of_element_located((By.CLASS_NAME,'login_head_submit_wrap')))).click()
(WebDriverWait(dev,10).until(EC.presence_of_element_located((By.CLASS_NAME,'btn.btn-md.btn-md-primary')))).click()




#it is personal dont use it :)
# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# ndev = webdriver.Chrome(options=option)
# # ndev.set_window_position(-10000,0)
# ndev.get("https://app.mysms.com/#login")

# # print('1')

# (WebDriverWait(ndev,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[2]/div/div[2]/div/table/tbody/tr[3]/td/div[1]/table/tbody/tr[2]/td/a')))).click()

# (ndev.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/table/tbody/tr[3]/td/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/input')).send_keys("9186716654")
# # print('1')

# (ndev.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/table/tbody/tr[3]/td/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/div/input')).send_keys("123456789m")

# (ndev.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/table/tbody/tr[3]/td/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/button')).click()
# # print('1')
# time.sleep(20)
# # t = ndev.find_elements_by_class_name('message')
# t = ndev.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/div[4]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div[1]')
# # print('1')
# p = ((t.text).split())
# # print('1')
# #/html/body/div[4]/div[2]/div/div[2]/div/div[4]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div[1]
# #/html/body/div[4]/div[2]/div/div[2]/div/div[4]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div[2]
# #/html/body/div[4]/div[2]/div/div[2]/div/div[4]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/div[1]/div/div/div[4]
# ndev.close()

# # print('1')




(WebDriverWait(dev, 20).until(EC.presence_of_element_located((By.NAME, 'phone_code')))).send_keys(p[8])

gr = ['/html/body/div/app-root/span/div[1]/div/rb-chats/div/div[2]/div/div[1]/ul[2]/li[1]',
'/html/body/div/app-root/span/div[1]/div/rb-chats/div/div[2]/div/div[1]/ul[2]/li[2]']
#/html/body/div/app-root/span/div[1]/div/rb-chats/div/div[2]/div/div[1]/ul[2]/li[3]


while True:
    try:
        
        for i in gr:
            (WebDriverWait(dev,60).until(EC.presence_of_element_located((By.XPATH, i)))).click()
            for u in range(55):
                try:
                    dev.find_element_by_xpath(f'/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[2]/div[1]/div/div[1]/div[2]/div[{u}]/div/div/div/div/div[2]/div/div/rb-message-media/div/rb-message-poll/div/div[3]/div/div/a/span').click()
                    
                
                except:
                    continue
        dev.refresh()    
    except:
        continue
            

