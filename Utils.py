import os
import requests
import warnings as w
from time import sleep
from requests import Session
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Disable unnecessary warnings
w.filterwarnings("ignore")


class Utils:
    @staticmethod
    def get_session(
        USERNAME: str = "",
        PASSWORD: str = "",
        config: dict = dict(),
        driver_type: str = "CHROME",
        browser_profile: str = "first",
        return_browser: bool = False,
    ) -> Session:
        """
        Creates and return a Logged in Session
        :param USERNAME: username to login
        :param PASSWORD: password to login
        :param config: configuration file used for login
        :param browser_profile: Browser Profile to utilise for session
        :return session: Logged in Session
        """

        # Webdriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        if config.get("LOGIN_CREDENTIALS").get("DRIVER_TYPE") == "CHROME":
            """
                Grab Current User Profile Path
            + Add Browser Profiles Location
            + Add Profile Number
                TO CREATE BROWSER PROFILE PATH
            """
            BROWSER_PATH = (
                os.environ.get("USERPROFILE")
                + config.get("BROWSER_PATH")
                + config.get("LOGIN_CREDENTIALS").get("PROFILE")
            )

            # Assign Browser Profile in Arguments
            browser_argument = "user-data-dir=" + BROWSER_PATH

            # Add Profile Number in Argument
            print("[#]  BROWSER ARGUMENT:   ", browser_argument)
            chrome_options.add_argument(browser_argument)

            driver = webdriver.Chrome(
                executable_path="D:\\chromedriver.exe",
                chrome_options=chrome_options,
            )
        else:
            profile = webdriver.FirefoxProfile()
            profile.set_preference(
                "dom.webnotifications.enabled",
                False,
            )
            profile.set_preference(
                "dom.push.enabled",
                False,
            )

            options = webdriver.FirefoxOptions()
            options.headless = False
            options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

            driver = webdriver.Firefox(
                executable_path="D:\\geckodriver.exe",
                options=options,
                firefox_profile=profile,
            )

        driver.maximize_window()
        # driver.get("https://www.tiktok.com/")
        # sleep(5)
        if return_browser:
            return driver

        # if (
        #     config.get("LOGIN_CREDENTIALS").get("USERNAME")
        #     if not USERNAME
        #     else USERNAME
        # ) not in driver.page_source:
        #     print("[!]  Driver Not Logged IN!")
        #     print("[*]  Trying to Log IN!")

        #     # Get username element
        # username = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable(
        #         (
        #             By.CSS_SELECTOR,
        #             "input[name='username']",
        #         ),
        #     )
        # )

        #     # Get password element
        #     password = WebDriverWait(driver, 10).until(
        #         EC.element_to_be_clickable(
        #             (
        #                 By.CSS_SELECTOR,
        #                 "input[name='password']",
        #             ),
        #         )
        #     )

        #     # Clear fields
        #     username.clear()
        #     password.clear()

        #     username.send_keys(
        #         config.get("LOGIN_CREDENTIALS").get("USERNAME")
        #         if not USERNAME
        #         else USERNAME,
        #     )
        #     password.send_keys(
        #         config.get("LOGIN_CREDENTIALS").get("PASSWORD")
        #         if not PASSWORD
        #         else PASSWORD,
        #     )

        #     sleep(2)
        #     password.send_keys(Keys.ENTER)
        #     sleep(10)

        #     if (
        #         config.get("LOGIN_CREDENTIALS").get("USERNAME")
        #         if not USERNAME
        #         else USERNAME
        #     ) not in driver.page_source:
        #         print("[!]  Driver Not Logged IN!")
        #         driver.quit()
        #         exit()
        #     else:
        #         print("[+]  Log In Successful!")

        # else:
        # print("[+]  Browser is Already Logged IN!")

        print("[+]  Browser does not require Logging IN!")

        # Grab Cookies from Driver
        cookies = driver.get_cookies()

        # Create New Session
        session = Session()
        session.headers.update(config.get("HEADERS"))

        # Assign Cookies to our Session
        session.cookies.clear()
        for single_cookie in cookies:
            required_cookies = {
                "name": single_cookie.get("name"),
                "value": single_cookie.get("value"),
            }
            optional_cookies = {
                "domain": single_cookie.get("domain"),
                "expires": None,
                "rest": {"HttpOnly": True},
                "path": single_cookie.get("path"),
                "secure": single_cookie.get("secure"),
            }
            # if single_cookie.get("name") == "csrftoken":
            #     session.headers.update({"x-csrftoken": single_cookie.get("value")})

            my_cookie = requests.cookies.create_cookie(
                **required_cookies, **optional_cookies
            )
            session.cookies.set_cookie(my_cookie)

        # Finally Cookies are set for Session, Closing Browser
        driver.quit()
        return session
