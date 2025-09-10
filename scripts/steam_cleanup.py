import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.imports import *

steamID = "FILISPEENCS2" # ENTER YOUR STEAMID
UPLOAD_URL = f"https://steamcommunity.com/login/home/?goto=id%2F{steamID}%2Fmyworkshopfiles%2F" 
items_to_delete = 5

def delete_last_5(driver):
    driver.get(UPLOAD_URL)
    if not steam_auth_check(driver):
        print("Authentification requied to upload.")
        if steam_login(driver): store_cookies(driver) #Storing cookies
    
    print(f"Cleaning up last {items_to_delete} items")

    i = 0
    while i < items_to_delete:
        driver.get(UPLOAD_URL)

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "workshopItem")))
        elements = driver.find_elements(By.CLASS_NAME, "workshopItem")
        elements[0].click()

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.general_btn.panel_btn")))
        panel_elements = driver.find_elements(By.CSS_SELECTOR, "span.general_btn.panel_btn")

        for subel in panel_elements:
            if "delete" in subel.text.strip().lower():
                print(f"Deleting {i+1}")
                subel.click()
                sleep(0.5)
                okbutt = WebDriverWait(driver, 60).until( EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_green_steamui.btn_medium")) )
                okbutt.click()
                break
            else: pass
        i += 1

if __name__ == "__main__":
    driver = get_driver()
    try:
        delete_last_5(driver)
    finally:
        driver.quit()
