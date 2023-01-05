from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class PostMedia:
    @staticmethod
    def get_all_posts(
        driver: Chrome = Chrome,
        config: dict = dict(),
    ) -> dict:
        """
        Return post interactions related data
        :param driver: Logged in Driver to perfrom Scrapping
        :param config: Config to get parameters
        :return data: Post data of target user

        """
        complete_items_list = list()
        total_posts = driver.find_elements(
            By.XPATH, config["MEDIA_XPATH"]["post_xpath"]
        )
        while total_posts and len(total_posts) <= config.get("POSTS_COUNT"):
            sleep(2)
            driver.execute_script(
                "arguments[0].scrollIntoView(true);",
                total_posts[-1],
            )
            total_posts = driver.find_elements(
                By.XPATH, config["MEDIA_XPATH"]["post_xpath"]
            )
            print("[{}] Total Posts Until Now".format(len(total_posts)))

        # for single_post in total_posts:
        #     single_post_view_count = single_post.text
        #     video_thumb = single_post.find_elements(
        #         By.XPATH, config["MEDIA_XPATH"]["video_thumb_xpath"]
        #     )
        #     media_url = single_post.find_elements(
        #         By.XPATH, config["MEDIA_XPATH"]["video_link_xpath"]
        #     )
        #     caption_url = single_post.find_elements(
        #         By.XPATH, config["MEDIA_XPATH"]["video_caption"]
        #     )

        #     data_dict = {
        #         "view_counts": single_post_view_count,
        #         "thumbnail": video_thumb[0].get_attribute("src") if video_thumb else "",
        #         "media_url": media_url[0].get_attribute("href") if media_url else "",
        #         "caption": caption_url[0].text if caption_url else "",
        #     }

        #     complete_items_list.append(data_dict)

        return complete_items_list
