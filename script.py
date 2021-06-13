from selenium import webdriver
from time import sleep

import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def verify_input_int(msg=""):
    while True:
        try:
            user_input = int(input(msg + ": "))
            if user_input == "":
                print("It cannot be empty")
                pass
            else:
                return user_input
        except ValueError:
            print("Enter number")
            pass


def verify_input_string(msg=""):
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
            pass


class ScriptSelenium:
    def __init__(self):
        pass

    def login_script(self, login, password):
        self.driver = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")  # path to selenium driver

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

    def close_browser(self):
        try:
            self.driver.close()
        except selenium.common.exceptions.WebDriverException:
            pass

    def main_script(self, login, password, how_many, commant_message):
        self.how_many = how_many
        self.commant_message = commant_message

        # remove before publish
        self.login_script(login="jakubowski.elise5304@yousmail.com", password="doan913nf0ne20fns0")

        while True:
            print("\n")
            print("Searching on the tag: 1")
            print("Selecting the explore tab: 2")
            print("Your own link: 3")
            print("Quit: 99")

            while True:
                user_input_1 = verify_input_int()
                if user_input_1 == 1:
                    while True:
                        status_tag_1 = self.instagram_search()
                        if status_tag_1 == "error":
                            print("\nError occurred. Probably a mistake occurred in the tag name or hashtag. "
                                  "Try again to enter the name of the tag.")
                            continue
                        elif status_tag_1 == "done":
                            print("\nI'm done")
                            print("\nDo you want one more time?")

                            user_input_2 = verify_input_string("Y or n")
                            if user_input_2.lower() == "y":
                                continue
                            else:
                                break
                        else:
                            break
                    break
                elif user_input_1 == 2:
                    self.instagram_explore()
                    break
                elif user_input_1 == 3:
                    self.instagram_search_by_link_profile()
                elif user_input_1 == 99:
                    print("Exiting...")
                    self.close_browser()
                    break
                else:
                    print("Error")

            if user_input_1 == 99:
                break

        print("\nI'm done")  # zakończenie pracy programu

    def further(self):
        try:
            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()  # kolejne zdjęcie
        except selenium.common.exceptions.NoSuchElementException:  # jeżeli jest to pierwsze zdjęcie to wykonaj to
            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a").click()

    def instagram_send_like_comments(self):
        for i in range(0, self.how_many):
            # click heart
            try:
                WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div"))).click()
            except selenium.common.exceptions.TimeoutException:
                # jeżeli zdjęcie się nie załadowało to przejdź dalej
                self.further()
                continue

            try:
                # add comment
                self.driver.find_element_by_class_name("Ypffh").click()
                sleep(1)
                self.driver.find_element_by_class_name("Ypffh").send_keys(self.commant_message)

                # send comment
                self.driver.find_element_by_xpath(
                    "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]").click()
                sleep(1)
            except selenium.common.exceptions.NoSuchElementException:  # jeżeli przycisk opublikuj jest nieosiągalny
                pass
            except selenium.common.exceptions.ElementNotInteractableException:  # if off comments
                pass

            sleep(1)
            self.further()  # kliknięcie dalej

    def instagram_search(self):
        what_tag = verify_input_string("What tag")  # zapytanie o tag użytkownika

        tag_main = "https://www.instagram.com/explore/tags/" + what_tag  # wyszukanie tagu
        self.driver.get(tag_main)

        sleep(3)
        try:
            # kliknięcie pierwszego zdjęcia w tagu
            pictures = self.driver.find_elements_by_css_selector("div[class='_9AhH0']")
            picture = pictures[0]
            picture.click()
        except IndexError:
            # jeżeli wpisany tag nie istnieje to wyrzuć błąd i zapytaj użytkownika o nowy tag
            return "error"

        sleep(3)

        self.instagram_send_like_comments()

        return "done"  # zakończenie pracy funkcji

    def instagram_explore(self):
        self.driver.get("https://www.instagram.com/explore/")

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "_9AhH0")))
        picture = self.driver.find_elements_by_class_name("_9AhH0")
        picture[1].click()

        self.instagram_send_like_comments()
        return "done"

    def instagram_search_by_link_profile(self):
        pass
