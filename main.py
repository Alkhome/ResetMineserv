import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Server:
    def __init__(self):

        self.hidden_credentials = []
        with open(file="credentials.txt") as credentials:
            self.hidden_credentials = [line.rstrip() for line in credentials]
        print(self.hidden_credentials)
        self.driver = webdriver.Chrome()
        self.driver.get(self.hidden_credentials[0])

    def login(self):
        username_element = self.driver.find_element(by=By.XPATH, value='//*[@id="username"]')
        password_element = self.driver.find_element(by=By.XPATH, value='//*[@id="password"]')
        login_button = self.driver.find_element(by=By.XPATH,
                                                value='/html/body/div[4]/div/div[2]/form/div[3]/div[2]/button')

        username_element.send_keys(self.hidden_credentials[1])
        password_element.send_keys(self.hidden_credentials[2])
        login_button.click()

    def choose_server(self):
        server_name = self.driver.find_element(by=By.LINK_TEXT, value=self.hidden_credentials[3])
        server_name.click()

    def restart_server(self):
        xpath_kill = "/html/body/div/div[1]/section[2]/div[2]/div/div/div[2]/button[4]"
        xpath_start = "/html/body/div/div[1]/section[2]/div[2]/div/div/div[2]/button[1]"
        kill_button = self.driver.find_element(by=By.XPATH, value=xpath_kill)
        start_button = self.driver.find_element(by=By.XPATH, value=xpath_start)
        time.sleep(5)

        kill_button.click()
        time.sleep(5)
        start_button.click()


if __name__ == '__main__':
    server = Server()
    server.login()
    server.choose_server()
    server.restart_server()
    exit()

