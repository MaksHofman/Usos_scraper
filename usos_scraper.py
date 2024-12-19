from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FireOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs import BeautifulSoup

class Usos_scraper:
    usos_test_page = "https://usosweb.usos.pw.edu.pl/kontroler.php?_action=dla_stud/studia/sprawdziany/index"
    usos_login_url = "https://cas.usos.pw.edu.pl/cas/login?service=https%3A%2F%2Fusosweb.usos.pw.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex&locale=pl"
    
    def __init__(self, login, password):
        self.driver_logged_into = Usos_scraper.login_to_usos(self, login, password)
    

    def init_driver(url):
        options = FireOptions()
        options.add_argument('--disable-logging')
        options.add_argument("--headless")
        options.add_argument("--log-level=3")
        driver = webdriver.Firefox(options)
        driver.get(url)
        return driver

    def login_to_usos(self, login, password):
        driver = Usos_scraper.init_driver(Usos_scraper.usos_login_url)
        login_el = driver.find_element(By.ID, "username")
        login_el.send_keys(login)
        password_el = driver.find_element(By.ID, "password")
        password_el.send_keys(password)
        button = driver.find_element(By.NAME, "submit")
        button.click
        if WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id="layout-c22"]/div/div[3]/div[2]/usos-frame[1]/h2/a"))):
            return driver
        else:
            return ValueError("Nieudalo sie zalogowac")
    
    def go_to_test_results_page(self):
        driver = self.driver_logged_into
        usos_resultspage = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id="layout-c22"]/div/div[3]/div[2]/usos-frame[1]/h2/a")))
        usos_resultspage.click
        



def read_from_file_test(file):
    

if __name__ == "__main__":
    print("start")