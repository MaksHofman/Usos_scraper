from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FireOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
class UsosScraper:
    usos_test_page = "https://usosweb.usos.pw.edu.pl/kontroler.php?_action=dla_stud/studia/sprawdziany/index"
    usos_login_url = "https://cas.usos.pw.edu.pl/cas/login?service=https%3A%2F%2Fusosweb.usos.pw.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex&locale=pl"
    
    def __init__(self, login, password):
        self.driver_logged_into = UsosScraper.login_to_usos(self, login, password)
    

    def init_driver(url):
        options = FireOptions()
        #options.add_argument('--disable-logging')
        #options.add_argument("--headless")
       # options.add_argument("--log-level=3")
        driver = webdriver.Firefox(options)
        driver.get(url)
        return driver

    def login_to_usos(self, login, password):
        driver = UsosScraper.init_driver(UsosScraper.usos_login_url)
        time.sleep(4)
        driver.find_element(By.ID, "username").send_keys(login)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "password").send_keys("\ue007")
        #driver.find_element(By.XPATH, '/html/body/main/div/div[3]/form/div[3]/div[1]/button').click
        time.sleep(3)
        return driver

    
    def go_to_test_results_page(self):
        driver = self.driver_logged_into
        usos_resultspage = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/usos-layout/div[2]/main-panel/main/div/div/div[3]/div[2]/usos-frame[1]/h2/a')))
        usos_resultspage.click
        
    def get_list_of_this_years_results_avaiable(self):
        self.go_to_test_results_page()# niedziala
        driver = self.driver_logged_into
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        feed_items = soup.find_all(class_='feed-item')
        x = 0
        lecture_names = []
        for ul in soup:
            if x != 0 :
                return lecture_names
            for il in ul:
                lecture_names.append(il)
            x += 1



def read_from_file_test(file):
    f = open(file, "r")
    return f.readline()

if __name__ == "__main__":
    print("start")
    f = open("secret.txt", "r")
    usos = UsosScraper(f.readline(), f.readline())
    lista = usos.get_list_of_this_years_results_avaiable()
    print(lista)