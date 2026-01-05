from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

    
    
def get_html_browser():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--disable-gpu")  
        chrome_options.add_argument("--window-size=1920,1080") 
        chrome_options.add_argument("--no-sandbox")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options= chrome_options)
        driver.get("https://www.99freelas.com.br/projects?categoria=web-mobile-e-software&data-da-publicacao=menos-de-24-horas-atras")
        
        results_list = driver.find_element(By.CLASS_NAME, "result-list")
        time.sleep(2)
        html = results_list.get_attribute("outerHTML")
    
    finally:
        driver.quit()
    return html
    

