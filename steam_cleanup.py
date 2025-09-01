from modules.imports import *

steamID = "FILISPEENCS2" # ENTER YOUR STEAMID
UPLOAD_URL = f"https://steamcommunity.com/id/{steamID}/myworkshopfiles/" 

def delete_last_5(driver):
    driver.get(UPLOAD_URL)
    if not steam_auth_check(driver):
        print("Authentification requied to upload.")
        if steam_login(driver): store_cookies(driver) #Storing cookies
    
    i = 0
    while i < 5:
        driver.get(UPLOAD_URL)

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "workshopItem")))
        elements = driver.find_elements(By.CLASS_NAME, "workshopItem")
        elements[0].click()

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.general_btn.panel_btn")))
        panel_elements = driver.find_elements(By.CSS_SELECTOR, "span.general_btn.panel_btn")
        print(panel_elements)

        for subel in panel_elements:
            print(subel.text)
            if "delete" in subel.text.strip().lower():
                print(f"Deleting {i}")
                subel.click()
                sleep(1)
                okbutt = WebDriverWait(driver, 60).until( EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_green_steamui.btn_medium")) )
                okbutt.click()
                break
            else: pass
        i += 1

if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        delete_last_5(driver)
    finally:
        driver.quit()
