from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from time import sleep
import requests
import shutil
import json
import os

def load_cookies(driver=None, file_path="cookies.json"):
    if driver==None: raise RuntimeError("You kinda forgot to use requied \"driver\" argument.")
    if file_path in os.listdir("."):
        with open(file_path, "r", encoding="utf-8") as f:
            cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        return True
    else: return False

def store_cookies(driver=None, file_path="cookies.json"):
    if driver==None: raise RuntimeError("You kinda forgot to use requied \"driver\" argument.")
    cookies = driver.get_cookies()
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(cookies, f, indent=4)

def steam_auth_check(driver=None):
    if driver==None: raise RuntimeError("You kinda forgot to use requied \"driver\" argument.")
    if load_cookies(driver): return True
    try:
        WebDriverWait(driver, 360).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input._2GBWeup5cttgbTw8FM3tfx[type='text']"))  # аватарка в меню
        )
        login_input = driver.find_element(By.CSS_SELECTOR, "input._2GBWeup5cttgbTw8FM3tfx[type='text']")
        if login_input.is_displayed():
            return False # Auth needed
    except NoSuchElementException:
        return True # Auth not needed
    
def steam_login(driver=None):
    if driver==None: raise RuntimeError("You kinda forgot to use requied \"driver\" argument.")
    try:
        WebDriverWait(driver, 360).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.user_avatar.playerAvatar"))  # аватарка в меню
        )
        print("Successfully authenticated")
        return True
    except:
        print("Unable to say if authentification is successfull")
        return False

def get_driver():
    try:
        print("Trying Chrome...")
        chrome_options = ChromeOptions()
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                options=chrome_options)
    except Exception:
        print("Chrome failed")

    try:
        print("Trying Firefox...")
        firefox_options = FirefoxOptions()
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                 options=firefox_options)
    except Exception:
        print("Firefox failed")

    try:
        print("Trying Edge...")
        edge_options = EdgeOptions()
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),
                              options=edge_options)
    except Exception:
        print("Edge failed")

    raise RuntimeError("No supported browser could be started. Please install Chrome, Edge, or Firefox.")


if __name__ == "__main__":
    print("It`s module not a script")