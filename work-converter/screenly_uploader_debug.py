import os
import sys
import webbrowser
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def toggle_screenly_asset(name, active):
    assets_root = driver.find_elements_by_xpath("//*[@id='assets']/div")
    active_assets = assets_root[0].find_elements_by_xpath(".//*[@id='active-assets']/tr")
    inactive_assets = assets_root[1].find_elements_by_xpath(".//*[@id='inactive-assets']/tr")
    
    for e in active_assets if active else inactive_assets:
        root = e.find_elements_by_xpath(".//*[@class='asset_row_name']")
        if len(root) > 0:
            if name in root[0].text:
                toggle = e.find_elements_by_xpath(".//td[@class='asset-toggle']")
                if len(toggle) > 0:
                    inputs = toggle[0].find_elements_by_xpath(".//input")
                    if len(inputs) > 0:
                        driver.execute_script("arguments[0].click();", inputs[0])
                        # print(inputs[0].is_selected())
                        break


print('starting screenly upload...')
screen_url = "https://358ff7b44b93c784c373a90861d9b267.balena-devices.com"
path = "/Users/ryanharrington/Development/Python_Scripts/work-converter/test.png"

# date = datetime.now().strftime('-%Y-%m-%d-%H-%M-%S')

# Create a new instance of the driver
driver = webdriver.Safari()

# go to the page
driver.get(screen_url)
sleep(1)

# find the add new asset button and click
driver.find_element_by_id("add-asset-button").click()

# now find the correct tab and click
print("uploading asset...")

driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//a[@href='#tab-file_upload']"))
el = driver.find_element_by_name('file_upload')
el.send_keys(path)
sleep(3)

# status = driver.find_element_by_class_name("status")
# print(status)

try:
    # wait until the upload process has completed
    wait = WebDriverWait(driver, 180)
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "status"), "Upload completed."))
except: print('error waiting')

#Asset has been successfully uploaded.
print("upload complete!...")
sleep(3)

#dismiss modal uploader
btns = driver.find_elements_by_xpath("//*[contains(@value,'Back')]")
driver.execute_script("arguments[0].click();", btns[0])
print(btns[0])
#print(t)

# wait until the new asset shows up in inactive elements
##########

# find the uploaded item starting with the inactive assets text

toggle_screenly_asset(path.rsplit('/', 1)[-1], False)
sleep(3)
toggle_screenly_asset(path.rsplit('/', 1)[-1], True)

#driver.quit()
