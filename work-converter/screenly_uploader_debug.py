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

# def highlight(element, effect_time, color, border):
#     """Highlights (blinks) a Selenium Webdriver element"""
#     driver = element._parent
#     def apply_style(s):
#         driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
#                               element, s)
#     original_style = element.get_attribute('style')
#     apply_style("border: {0}px solid {1};".format(border, color))
#     sleep(effect_time)
#     apply_style(original_style)

def get_screen_url(screen):
    with open('/Users/ryanharrington/Development/players-dev/digital-sinage/work-converter/.screens','r') as file:
        for line in file:
            keys = line.split('=')
            for key in keys:
                if key == screen:
                    return keys[1].strip()
    return "screen"

def toggle_screenly_asset(name, active):
    print(name)
    assets_root = driver.find_elements_by_xpath("//*[@id='assets']/div")
    active_assets = assets_root[0].find_elements_by_xpath(".//*[@id='active-assets']/tr")
    inactive_assets = assets_root[1].find_elements_by_xpath(".//*[@id='inactive-assets']/tr")

    for e in active_assets if active else inactive_assets:
        root = e.find_elements_by_xpath(".//*[@class='asset_row_name']")
        if len(root) > 0:
            if name in root[0].text:
                toggle = e.find_elements_by_xpath(".//*[@class='asset-toggle']")
                #print(toggle)
                if len(toggle) > 0:
                    inputs = toggle[0].find_elements_by_xpath(".//label/input")
                    if len(inputs) > 0:
                        #print(inputs[0])
                        print("found toggle")
                        driver.execute_script("arguments[0].click();", inputs[0])
                        break


path = ""
screen_url = ""
automate = False
argLen = len(sys.argv)
if argLen > 2:
    path = sys.argv[1].strip()
    screen_url = get_screen_url(sys.argv[2])
    # if argLen > 3 and sys.argv[3] == "-na":
    #     automate = False
    if screen_url == "screen":
        print("screen was not found...exiting")
        sys.exit(1)
else: print('hopefully debug mode')

print('starting screenly upload...')

date = datetime.now().strftime('-%Y-%m-%d-%H-%M-%S')
os.rename(path + '.mp4', path + date + '.mp4')

driver = webdriver.Safari()
driver.get(screen_url)
sleep(3)
toggle_screenly_asset("pns-slides-2020-01-28-15-17-15", False)
#toggle_screenly_asset(path.rsplit('/', 1)[-1] + date, False)
#print(path.rsplit('/', 1)[-1] + date)
driver.quit()

# Create a new instance of the driver
if automate:
    driver = webdriver.Safari()

    # go to the page
    driver.get(screen_url)
    sleep(3)

    # find the add new asset button and click
    addAssetButton = driver.find_element_by_id("add-asset-button")
    driver.execute_script("arguments[0].click();", addAssetButton)
    #sleep(3)

    # now find the correct tab and click
    print("uploading asset...")

    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//a[@href='#tab-file_upload']"))
    el = driver.find_element_by_name('file_upload')
    el.send_keys(path + date + '.mp4')

    ##########
    #el.send_keys("/Users/ryanharrington/Development/pns-slides/test.png")
    ##########

    try:
        # wait until the upload process has completed
        wait = WebDriverWait(driver, 180)
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "status"), "Upload completed."))
    except: print('error waiting')

    #Asset has been successfully uploaded.
    print("upload complete!...")
    #sleep(3)

    #dismiss modal uploader
    btns = driver.find_elements_by_xpath("//*[contains(@value,'Back')]")
    driver.execute_script("arguments[0].click();", btns[0])
    # print(btns[0])
    #sleep(3)

    # find the uploaded item starting with the inactive assets text

    print("enabling asset...")
    toggle_screenly_asset("pns-slides", True)
    sleep(3)
    toggle_screenly_asset(path.rsplit('/', 1)[-1] + date, False)
    print(path.rsplit('/', 1)[-1] + date)

    driver.quit()
webbrowser.open(screen_url)