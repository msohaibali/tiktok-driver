import json
from time import sleep
from Utils import Utils
from BasicInfo import BasicInfo
from datetime import datetime as dt
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Read Configuration as global variable
with open("config.json") as fl:
    config = json.loads(fl.read())

# session = Utils.get_session(config=config)
start_time = dt.now()
driver = Utils.get_session(config=config, return_browser=True)
userlist = ["sidmr.rapper4"]
for single_user in userlist:
    request_url = (
        "https://www.tiktok.com/api/user/detail/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.84&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7178862406331696641&device_platform=web_pc&focus_state=false&from_page=user&history_len=4&is_fullscreen=false&is_page_visible=true&language=en&os=windows&priority_region=&referer=&region=PK&screen_height=750&screen_width=1334&secUid=MS4wLjABAAAABVwxfCNBZI7P8cMB0DzEK6hMdBxK1aNA3PEySDIkos8qm-6NxTUXq-QZXiA7n7TC&tz_name=Asia%2FKarachi&uniqueId="
        + single_user
        + "&verifyFp=verify_lbuvwujx_U3UdBNxz_BM5X_4Oyw_BMrN_x2ufNk6Uhwqv&webcast_language=en&msToken=J9Mjj0w6PGYKOAi3krUHq8aFLjpjzXGEcFLfDEQTrHpLidSgEyZPXfYzdKeEqfDyFrJRGQd7YG0_PO_ySatX4wOkuhNSNbd6mK94FlpttIysSw04Y5hBVUvJtLCRXH2DZZJ8QptUaikl-fBfoA==&X-Bogus=DFSzswVOUstANGrzSkvsQQYklTXw&_signature=_02B4Z6wo00001YIVdgQAAIDAXGMuomudUh2CFXKAAAMma4"
    )
    # request_url = "https://www.tiktok.com/api/post/item_list/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.3&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7178862406331696641&device_platform=web_pc&focus_state=false&from_page=user&history_len=4&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=&referer=&region=PK&screen_height=750&screen_width=1334&tz_name=Asia%2FKarachi&verifyFp=verify_lbuvwujx_U3UdBNxz_BM5X_4Oyw_BMrN_x2ufNk6Uhwqv&webcast_language=en&msToken=hFLMPYwrBTualm1qv5I_NIdEoQsxAFe2Dt8EKzS275bAt3J2UZ8ztPZJfnNJX3kYY_OQ8U1nMQKS4Vk277SI8q_XS7MoFq36VgeEICO60BuU9pd5f-rlVe-KBigeXyco0o7ZP0IVi7TQ7wRqSA==&X-Bogus=DFSzswVYl2UANCpgSkv/zOYklTIU&_signature=_02B4Z6wo00001BcZ1RAAAIDByW-NtPLC9YQXGdGAAGZtc6"
    # driver.get("https://www.tiktok.com/")
    # sleep(2)
    driver.get(request_url)
    # sleep(5)
    body = driver.find_elements(By.TAG_NAME, "body")
    body_text = body[0].text if body else ""
    data = json.loads(body_text)
    with open("JM.json", "w", encoding="utf-8") as fl:
        json.dump(data, fl)
    # print(data)

end_time = dt.now()
print("[+]  Total Time  ::  ", str(end_time - start_time))
