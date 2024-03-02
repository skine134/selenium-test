from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class selenium_crawler():
    def __init__(self):
        self.driver =webdriver.Chrome()


    def url_load(self,page_url:str):
        driver = self.driver
        driver.get(page_url)
        WebDriverWait(driver=driver,timeout=10).until(EC.presence_of_element_located((By.TAG_NAME,"body")))
        print("페이지 로드 완료")
        data = driver.find_elements(By.TAG_NAME,"img")
        print(f'print data: {data}')
        driver.close()