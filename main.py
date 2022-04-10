from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, time


time_start = time()

s = Service(ChromeDriverManager().install())
dr = webdriver.Chrome(service=s)
action = ActionChains(dr)

url = "https://orteil.dashnet.org/cookieclicker/"

dr.get(url)
sleep(2)
big_cookie = dr.find_element(By.ID, "bigCookie")

game_is_on = True
buy_cursor = True
buy_gma = False
buy_farm = False
buy_mine = False
buy_factory = False
buy_bank = False
n = 22

buy_button = dr.find_element(By.ID, "storeBulkBuy")
action.move_to_element(buy_button).perform()
buy_button.click()
for x in range(8):
    action.send_keys(Keys.DOWN).perform()

while game_is_on:
    for x in range(n):
        big_cookie.click()
    try:
        upgrade = dr.find_element(By.ID, "upgrade0")
        action.move_to_element(upgrade)
        upgrade.click()
    except:
        pass
    if buy_cursor:
        try:
            cursor = dr.find_element(By.ID, "product0")
            action.move_to_element(cursor)
            cursor.click()
            cursor_owned = int(dr.find_element(By.ID, "productOwned0").text)
            if cursor_owned < 10:
                action.move_to_element(cursor)
                cursor.click()
            if cursor_owned == 10:
                buy_cursor = False
                gma = dr.find_element(By.ID, "product1")
                action.move_to_element(gma)
                gma.click()
                buy_gma = True
                n = 50
            if cursor_owned < 25:
                action.move_to_element(cursor)
                cursor.click()
            if cursor_owned == 25:
                buy_cursor = False
        except:
            pass
    if buy_gma:
        try:
            action.move_to_element(gma)
            gma.click()
            gma_owned = int(dr.find_element(By.ID, "productOwned1").text)
            if gma_owned < 12:
                action.move_to_element(gma)
                gma.click()
            if gma_owned == 12:
                buy_gma = False
                farm = dr.find_element(By.ID, "product2")
                action.move_to_element(farm)
                farm.click()
                buy_farm = True
                n = 150
        except:
            pass
    if buy_farm:
        try:
            action.move_to_element(farm)
            farm.click()
            farm_owned = int(dr.find_element(By.ID, "productOwned2").text)
            if farm_owned < 10:
                action.move_to_element(farm)
                farm.click()
            if farm_owned == 10:
                buy_farm = False
                mine = dr.find_element(By.ID, "product3")
                action.move_to_element(mine)
                mine.click()
                buy_mine = True
                n = 200
        except:
            pass
    if buy_mine:
        try:
            action.move_to_element(mine)
            mine.click()
            mine_owned = int(dr.find_element(By.ID, "productOwned3").text)
            if mine_owned < 3:
                action.move_to_element(mine)
                mine.click()
            if mine_owned == 3:
                buy_mine = False
                factory = dr.find_element(By.ID, "product4")
                action.move_to_element(factory)
                factory.click()
                buy_factory = True
        except:
            pass
    if buy_factory:
        try:
            action.move_to_element(factory)
            factory.click()
            factory_owned = int(dr.find_element(By.ID, "productOwned4").text)
            if factory_owned < 2:
                action.move_to_element(factory)
                factory.click()
            if factory_owned == 2:
                buy_factory = False
                bank = dr.find_element(By.ID, "product5")
                action.move_to_element(bank)
                bank.click()
                buy_bank = True
        except:
            pass
    if buy_bank:
        try:
            action.move_to_element(bank)
            bank.click()
            bank_owned = int(dr.find_element(By.ID, "productOwned5").text)
            if bank_owned < 2:
                action.move_to_element(bank)
                bank.click()
            if bank_owned == 2:
                buy_factory = False
                bank = dr.find_element(By.ID, "product6")
                action.move_to_element(bank)
                bank.click()
                buy_next = True
        except:
            pass
    if time() - time_start >= 300:
        game_is_on = False
        print(dr.find_element(By.ID, "cookies").text)
        break


input("Don't Close!")
