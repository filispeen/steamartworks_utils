from modules.imports import *

UPLOAD_URL = "https://steamcommunity.com/sharedfiles/edititem/767/3"

def upload_file(driver, file_to_upload):
    driver.get(UPLOAD_URL)
    if not steam_auth_check(driver):
        print("Authentification requied to upload.")
        if steam_login(driver): store_cookies(driver) #Storing cookies
    driver.get(UPLOAD_URL)

    upload_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#file[type='file']")))
    upload_input.send_keys(file_to_upload)
    driver.execute_script(r"v_trim=_=>{return _},$J('#title').val(' \n'+Array.from(Array(126),_=>'\t').join(''));$J('[name=consumer_app_id]').val(480);$J('[name=file_type]').val(0);$J('[name=visibility]').val(0);")
    driver.find_element(By.CSS_SELECTOR, "input.inputTagsFilter[type='checkbox'][name='agree_terms']").click()  # Погодитися з умовами
    driver.find_element(By.CSS_SELECTOR, "a.btn_blue_white_innerfade.btn_medium").click()  # Кнопка "Зберегти"
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.subscribeText")))

@click.command()
@click.option('--base-dir', help='Base directory containing subdirectories with images.')
def main(base_dir=None):
    if base_dir==None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        folders = list_folders(base_dir)
        for i in range(len(folders)):
            folders[i] = os.path.join(base_dir, folders[i], "upload")
    else: 
        path = os.path.join(base_dir, "upload")
        folders = [ path ]
    
    print(f"Found {len(folders)} folders to process.")

    driver = get_driver()
    try:
        for directory in folders:
            for file_name in os.listdir(directory):
                file_path = os.path.join(base_dir, os.path.join(directory, file_name))
                if ".ignore" in file_path: break
                if os.path.isfile(file_path) and "upload" in file_path:
                    print(f"Uploading: {file_path}")
                    upload_file(driver, file_path)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()