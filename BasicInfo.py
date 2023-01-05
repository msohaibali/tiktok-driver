from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class BasicInfo:
    @staticmethod
    def get_basic_info(
        driver: Chrome = None,
        user_name: str = "",
        config: dict = dict(),
    ) -> dict:
        """
        Return basic data of a Profile/Page
        :param driver: Logged in Driver to perfrom requests
        :param user_name: target user name of Page/Profile
        :return data: Basic Data against provided user name
        """
        BASE_URL = "https://www.tiktok.com/@{username}"
        final_dict = dict()

        driver.get(BASE_URL.format(username=user_name))

        # Name of Profile
        name_elm = driver.find_elements(
            By.XPATH,
            config["BASIC_XPATH"]["name_xpath"],
        )
        final_dict["name"] = name_elm[0].text if name_elm else ""

        # Bio of Profile
        bio_elm = driver.find_elements(
            By.XPATH,
            config["BASIC_XPATH"]["bio_xpath"],
        )
        final_dict["bio"] = bio_elm[0].text if bio_elm else ""

        # Avatar of Profile
        avatar_elm = driver.find_elements(
            By.XPATH, config["BASIC_XPATH"]["avatar_xpath"]
        )
        final_dict["image"] = avatar_elm[0].get_attribute("src") if avatar_elm else ""

        # Followers of Profile
        followers_elm = driver.find_elements(
            By.XPATH, config["BASIC_XPATH"]["followers_xpath"]
        )
        final_dict["followers_count"] = followers_elm[0].text if followers_elm else ""

        # Followings of Profile
        followings_elm = driver.find_elements(
            By.XPATH, config["BASIC_XPATH"]["followings_xpath"]
        )
        final_dict["followings_count"] = (
            followings_elm[0].text if followings_elm else ""
        )

        # Likes of Profile
        likes_elm = driver.find_elements(
            By.XPATH,
            config["BASIC_XPATH"]["likes_xpath"],
        )
        final_dict["likes_count"] = likes_elm[0].text if likes_elm else ""

        return final_dict
