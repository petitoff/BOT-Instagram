from selenium import webdriver
from time import sleep
from random import randint

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
    # open selenium and login
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
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, button_path))).click()

        # accept save login
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/section/main/div/div/div/section/div/button"))).click()
        # off notification
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))).click()

        print("Login Success\n")

    # close browser
    def close_browser(self):
        try:
            self.driver.close()
        except selenium.common.exceptions.WebDriverException:
            pass

    # first option from execution
    def if_user_input_exec_is_1(self):
        while True:
            self.how_many = verify_input_int("How many")
            if self.how_many > 0:
                print("Enter a number greater than 0")
                break
            else:
                continue

        # print("\nDo you want send comments")
        # print("Yes: 1")
        # print("No: 2")
        #
        # self.ask_user_want_comments = verify_input_int("set")

        # Comments and likes
        while True:
            print("")
            print("Searching by the tag: 1")
            print("Selecting the explore tab: 2")
            print("Your own link: 3")
            print("Quit: 99")

            while True:
                user_input_1 = verify_input_int()
                if user_input_1 == 1:
                    while True:
                        status_tag_1 = self.instagram_search_by_tag()
                        if status_tag_1 == "error":
                            print("\nError occurred. Probably a mistake occurred in the tag name or hashtag. "
                                  "Try again to enter the name of the tag.")
                            continue
                        elif status_tag_1 == "done":
                            print("\nI'm done")
                            break
                        else:
                            break
                    break
                elif user_input_1 == 2:
                    self.instagram_explore()
                    break
                elif user_input_1 == 3:
                    status_work_3 = self.instagram_search_by_link_profile()
                    if status_work_3 == "error":
                        print("The profile is private or there are no photos")
                    break
                elif user_input_1 == 99:
                    print("Exiting...")
                    self.close_browser()
                    break
                else:
                    print("Error")

            if user_input_1 == 99:
                break

    def if_user_input_exec_is_2(self):
        self.how_many = verify_input_int("How many")

        while True:
            print("")
            print("User from explore tab: 1")
            print("Link to profile: 2")
            print("Quit: 99")

            user_input_1 = verify_input_int("set")
            if user_input_1 == 1:
                self.instagram_user_explore_tab()
                pass
            elif user_input_1 == 99:
                break
            else:
                continue

    def main_script(self, login, password, user_input_exec):
        # remove login and password before publish
        self.login_script(login="jakubowski.elise5304@yousmail.com", password="doan913nf0ne20fns0")

        # rozpoczęcie pracy głównej definicji

        # if execution set 1
        if user_input_exec == 1:
            self.if_user_input_exec_is_1()
        # if execution set 2
        elif user_input_exec == 2:
            self.if_user_input_exec_is_2()

        print("\nI'm done")  # potwierdzenie zakończenia działania programu

    # definicja wykonuje operacje kliknięcia do następnego zdjęcia
    def further(self):
        try:
            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()  # next photo
        except selenium.common.exceptions.NoSuchElementException:  # if this is the first photo, take it
            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a").click()

    def instagram_main_script_send_like_comments(self):
        try:
            # select the first photo from the tab
            WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.CLASS_NAME, "_9AhH0")))
            picture = self.driver.find_elements_by_class_name("_9AhH0")
            picture[1].click()
        except IndexError:
            # if the entered tag does not exist, throw an error and ask the user for a new tag
            return "error"
        except selenium.common.exceptions.TimeoutException:
            return "error"

        value_1 = self.instagram_load_spam_comments()
        for i in range(0, self.how_many):
            self.instagram_send_like()
            if value_1 != "None":
                self.instagram_send_spam_comments()
            self.further()

    def instagram_send_like(self):
        # click heart
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div"))).click()
        except selenium.common.exceptions.TimeoutException:
            # if the photo did not load, go on
            self.further()  # dalej

    def instagram_send_spam_comments(self):
        lines_len = len(self.lines)
        random_index = randint(0, lines_len - 1)
        random_comment = self.lines[random_index]
        sleep(1)

        try:
            # add comment
            self.driver.find_element_by_class_name("Ypffh").click()
            sleep(1)
            self.driver.find_element_by_class_name("Ypffh").send_keys(random_comment)

            # send comment
            self.driver.find_element_by_xpath(
                "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]").click()
            sleep(1)
        except selenium.common.exceptions.NoSuchElementException:  # if the publish button is unavailable
            pass
        except selenium.common.exceptions.ElementClickInterceptedException:
            pass
        except selenium.common.exceptions.ElementNotInteractableException:  # if off comments
            pass

        sleep(1)
        return "done"

    def instagram_load_spam_comments(self):
        ask_1_1 = verify_input_string("Do you want send comments, Y/n")
        if ask_1_1.lower() == "y":
            while True:
                print("\nSingle comment in the console: 1")
                print("Random comments from the file: 2")
                comment_to_send_1 = verify_input_int("set")
                if comment_to_send_1 == 1:
                    print("Note, a single comment can be detected as spam and blocked. Do you want to continue?")
                    ask_1 = verify_input_string("Y/n")
                    if ask_1.lower() == "y":
                        while True:
                            comment_to_send_from_user = verify_input_string("Your comments: ")
                            print('This is your message: "' + comment_to_send_from_user + '"')
                            ask_2 = input("Do you want to continue, Y or n: ")
                            if ask_2.lower() == "y":
                                break
                            elif ask_2.lower() == "n":
                                continue
                            else:
                                continue
                        break
                    else:
                        continue
                elif comment_to_send_1 == 2:
                    break

            if comment_to_send_1 == 2:
                print('\nPlace comments in the text file: "spam-comments.txt"')
                while True:
                    ask_2 = input("If you did this, enter [d]: ")
                    if ask_2 == "d":
                        self.lines = []
                        with open("spam-comments.txt") as file:
                            for line in file:
                                line = line.strip()
                                self.lines.append(line)
                        break
                    else:
                        continue
        else:
            return "None"

    # wybranie opcji number 1 - szukanie za pomocą tagu
    def instagram_search_by_tag(self):
        what_tag = verify_input_string("What tag")  # query for user tag

        tag_main = "https://www.instagram.com/explore/tags/" + what_tag  # search for a tag
        self.driver.get(tag_main)

        result = self.instagram_main_script_send_like_comments()
        if result == "error":
            return "error"

        return "done"  # termination of the function work

    def instagram_explore(self):
        self.driver.get("https://www.instagram.com/explore/")  # link pointing to the explore tab

        self.instagram_main_script_send_like_comments()  # start sending likes and comments
        return "done"  # termination of the function work

    def instagram_search_by_link_profile(self):
        link_to_profile = verify_input_string("set")
        self.driver.get(link_to_profile)

        self.instagram_main_script_send_like_comments()
        return "done"

    def instagram_main_user(self):
        try:
            # select the first photo from the tab
            WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.CLASS_NAME, "_9AhH0")))
            picture = self.driver.find_elements_by_class_name("_9AhH0")
            picture[1].click()
        except IndexError:
            # if the entered tag does not exist, throw an error and ask the user for a new tag
            return "error"
        except selenium.common.exceptions.TimeoutException:
            return "error"

        error = 0
        while True:
            try:
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "ZIAjV")))
                get_user_profile = self.driver.find_elements_by_class_name("ZIAjV")
                get_user_profile[2].click()
            except IndexError:
                error = 1
            if error == 0:
                break
            else:
                self.further()
                continue

        try:
            # select the first photo from the tab
            WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.CLASS_NAME, "_9AhH0")))
            picture = self.driver.find_elements_by_class_name("_9AhH0")
            picture[1].click()
        except IndexError:
            # if the entered tag does not exist, throw an error and ask the user for a new tag
            return "error"
        except selenium.common.exceptions.TimeoutException:
            return "error"

        value_1 = self.instagram_load_spam_comments()
        for i in range(0, self.how_many):
            self.instagram_send_like()
            if value_1 != "None":
                self.instagram_send_spam_comments()
            self.further()

        self.driver.find_element_by_xpath("/html/body/div[5]/div[3]/button").click()  # zamykanie postu
        sleep(1)
        self.driver.execute_script("scroll(0, 0);")  # scroll top
        sleep(1)
        self.driver.find_element_by_class_name("_5f5mN").click()  # click follow
        sleep(1)
        self.driver.find_element_by_class_name("sqdOP").click()  # click send msg

    def instagram_user_explore_tab(self):
        self.driver.get("https://www.instagram.com/explore/")  # link pointing to the explore tab
        self.instagram_main_user()
        sleep(3000)
