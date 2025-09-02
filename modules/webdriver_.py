from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

if __name__ == "__main__":
    main()