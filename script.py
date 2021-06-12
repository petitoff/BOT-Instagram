from selenium import webdriver
from time import sleep

import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ScriptSelenium:
    def __init__(self):
        pass

    def verify_input(self, msg=""):
        while True:
            try:
                user_input = input(msg + ": ")
                if user_input == "":
                    print("It cannot be empty")
                    pass
                else:
                    return user_input
            except ValueError:
                print("Enter number")

    def main_script(self, login, password, how_many, commant_message):
        self.driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")

        # remove before publish
        self.script(login="jakubowski.elise5304@yousmail.com", password="doan913nf0ne20fns0")

        print("Searching on the tag: 1")
        print("Selecting the explore tab: 2")
        print("Your own link: 3")
        user_input_2 = int(self.verify_input())

        if user_input_2 == 1:
            while True:
                status_tag_1 = self.instagram_search(how_many, commant_message)
                if status_tag_1 == "error":
                    print("\nError occurred. Probably a mistake occurred in the tag name or hashtag. "
                          "Try again to enter the name of the tag.")
                else:
                    break
        elif user_input_2 == 3:
            self.instagram_search_by_link_profile()

        print("\nI'm done")
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

    def instagram_search(self, how_many, commant_message):
        what_tag = self.verify_input("What tag")

        tag_main = "https://www.instagram.com/explore/tags/" + what_tag
        self.driver.get(tag_main)

        sleep(3)
        try:
            pictures = self.driver.find_elements_by_css_selector("div[class='_9AhH0']")
            picture = pictures[1]
            picture.click()
        except IndexError:
            return "error"

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
            except selenium.common.exceptions.ElementNotInteractableException:  # off comments
                pass

            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()

    def instagram_search_by_link_profile(self):
        pass
