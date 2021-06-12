from selenium import webdriver
from time import sleep

import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ScriptSelenium:
    def __init__(self):
        pass

    def main_script(self, login, password, how_many, commant_message):
        self.driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")

        self.script(login="jakubowski.elise5304@yousmail.com", password="doan913nf0ne20fns0")

        print("Searching on the tag: 1")
        print("Selecting the explore tab: 2")
        while True:
            try:
                user_input_2 = int(input(": "))
                if user_input_2 == "":
                    print("It cannot be empty")
                    pass
                else:
                    break
            except ValueError:
                print("Enter number")

        if user_input_2 == 1:
            what_tag = input("What tag: ")
            self.instagram_search(what_tag, how_many, commant_message)

        print("I'm done")
        sleep(3000)

    def script(self, login, password):
        # open selenium / webdriver
        self.driver.get("https://instagram.com/")

        # Accept cookies
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/button[1]"))).click()

        # login form
        button_path = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div"
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(
            login)  # login
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(
            password)  # password
        self.driver.find_element_by_xpath(button_path).click()

        # accept save login
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/section/main/div/div/div/section/div/button"))).click()
        # off notification
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))).click()

        print("Login Success\n")

    def instagram_search(self, tag, how_many, commant_message):
        tag_main = "https://www.instagram.com/explore/tags/" + tag
        self.driver.get(tag_main)

        sleep(3)

        pictures = self.driver.find_elements_by_css_selector("div[class='_9AhH0']")
        picture = pictures[0]
        picture.click()

        sleep(3)

        for i in range(0, how_many):
            # click heart
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div"))).click()

            try:
                self.driver.find_element_by_xpath(
                    "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(
                    commant_message)
                self.driver.find_element_by_xpath(
                    "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]").click()
            except selenium.common.exceptions.NoSuchElementException:
                pass
            except selenium.common.exceptions.ElementNotInteractableException:
                pass

            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a").click()
