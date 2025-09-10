import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.imports import *

def scroll_down(driver, pause_time=1.5):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def smooth_scroll_down(driver, step=300, pause_time=1.5):
    last_height = driver.execute_script("return document.body.scrollHeight")
    current_position = 0
    while current_position < last_height:
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        sleep(pause_time)
        current_position += step
        last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(pause_time)

def get_folder_name_from_url(url):
    return url.rstrip('/').split('/')[-1]

def download_images(image_urls, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    for idx, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                ext = url.split('.')[-1].split('?')[0]
                filename = f"{idx+1}.{ext}"
                with open(os.path.join(save_dir, filename), "wb") as f:
                    f.write(response.content)
        except Exception as e:
            print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    try:
        driver = webdriver.Chrome()
        urls = [
            ""
        ]
        for url in urls:
            print(f"Processing {url}")
            driver.get(url)
            smooth_scroll_down(driver, step=300, pause_time=0.01)
               
            folder_name = get_folder_name_from_url(url)
            img_elements = driver.find_elements(By.TAG_NAME, "img")
            image_urls = []
            for img in img_elements:
                src = img.get_attribute("src")
                if src: image_urls.append(src)
            download_images(image_urls, save_dir=folder_name)
    finally:
        driver.quit()