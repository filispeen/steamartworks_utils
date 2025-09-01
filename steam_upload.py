from modules.imports import *

UPLOAD_URL = "https://steamcommunity.com/sharedfiles/edititem/767/3"

def upload_file(driver, file_to_upload):
    driver.get(UPLOAD_URL)
    if not steam_auth_check(driver):
        print("Authentification requied to upload.")
        if steam_login(driver): store_cookies(driver) #Storing cookies
    driver.get(UPLOAD_URL)

    upload_input = driver.find_element(By.CSS_SELECTOR, "input#file[type='file']")
    upload_input.send_keys(file_to_upload)
    driver.execute_script(r"v_trim=_=>{return _},$J('#title').val(' \n'+Array.from(Array(126),_=>'\t').join(''));$J('[name=consumer_app_id]').val(480);$J('[name=file_type]').val(0);$J('[name=visibility]').val(0);")
    driver.find_element(By.CSS_SELECTOR, "input.inputTagsFilter[type='checkbox'][name='agree_terms']").click()  # Погодитися з умовами
    driver.find_element(By.CSS_SELECTOR, "a.btn_blue_white_innerfade.btn_medium").click()  # Кнопка "Зберегти"
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.subscribeText")))

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    upload_folders = []
    for file in os.listdir(base_dir):
        folder_path = os.path.join(os.path.join(base_dir, os.path.join(file, "upload")))
        if os.path.isdir(folder_path) and file not in [".git", "modules", "venv"]:
            print(folder_path)
            upload_folders.append(folder_path)
    driver = webdriver.Chrome()
    try:
        for directory in upload_folders:
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                if os.path.isfile(file_path):
                    print(f"Uploading: {file_path}")
                    upload_file(driver, file_path)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()