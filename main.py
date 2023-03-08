from selenium import webdriver
from selenium.webdriver.common.by import By

class Server:
    def __init__(self, webpage="https://mineserv.eu/login"):
        self.driver = webdriver.Chrome()
        self.driver.get(webpage)

    def login(self, username, password):
        username_element = self.driver.find_element(by=By.XPATH, value='//*[@id="username"]')
        password_element = self.driver.find_element(by=By.XPATH, value='//*[@id="password"]')
        login_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div[2]/form/div[3]/div[2]/button')

        username_element.send_keys("testing")
        password_element.send_keys("testing")
        login_button.click()

    def choose_server(self):
        pass

    def restart_server(self):
        pass



if __name__ == '__main__':
    server = Server()
    server.login(username="", password="")
    server.choose_server()
    server.restart_server()
    input()  # TODO remove

