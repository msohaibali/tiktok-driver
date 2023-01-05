import requests
import unittest
import json


class TestBasicInfoData(unittest.TestCase):
    user_name: str = "jannatmirza"
    headers = {
        "authority": "www.tiktok.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "tt_csrf_token=MDVAOg7x-K57cmfVdQpbXA4hNZ6MspfiwBqE; tiktok_webapp_theme=light; _ttp=2IMORhN9SxeCERDDWoPpT94Dhqk; tt_chain_token=TLIfLaDCxxBphNe3hEE2WA==; _abck=E835185401FFD58BCB162B7F2FDBA9A3~0~YAAQHOldbj6T+hGFAQAAm639cQkmnSL3XkX8gq6ho77OEWJOvCz7ba56GqtW/ObHdHKrn+ZlOEhph/ZSfzLMTtE90MYl2DlIhNuwYfeUnHrry1/7RK7OLIbw+wEEdT+HSqq+dZ8u1MeWY6l6OYiIzZ6TKZhSJ+IsL87bMd4PYwaUnxVS+m9l2WCaZLfMB9xhfp+oK6m5tQ+LiaQluJhfjLs2SXGGlIb52cD91RJTc4HOmitdKlIg12PBRA8AKo+Bvcwy010/d0Om5u3CNqMX49j/yQT3Gy+wnwWfjyXHHrdGEcTkteLaJ9MAtEHBG60SHM2ALTYQs0mZUqnbnrYNWm6TK1BdXvvq695dNyH3Sns9TTE7SATnZCjLVjYYVLbTJ4q2Z4d6qc5Y40nyCR6UuBTXNqjJkKOL~-1~-1~-1; bm_sz=B2F4B42F046595D59C14620431188993~YAAQHOldbkGT+hGFAQAAm639cRKh6gzF/1Uf2MUE/dNdVzUV/YqNNLqcNmtbcjWEqeIoF532TtHxEXnocaitRATiyKiUf5IhS5yzes3yL73B1iluaJFzWZuejXDflTbleTwsTS/5vLvhe2D9QMdL93bCDdhWJj9+0q3uA11J8AX8x0ninIS3AV/rXaluzDh8mEvn08Lu4x2RJ58tcitctNNlg3SmllAX1UbAJbyyr5nlgXIpdsIWl73DLiOygZswD3KK1Xl+LccM4AcbDQQ6hA5AI6TpyRe3lBH08RoRl5QCX6A=~4338245~3355960; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227168854950909920770%22%2C%22timestamp%22:1669129173102}; ak_bmsc=2B264E96EC8A617DAEBA0E9F2BD786B0~000000000000000000000000000000~YAAQHOldblOT+hGFAQAAC8b9cRIigQs4BO8dewfdogwjUa9QyFgqe5OvrZbI75rMYEOvj/XcZSH7cjkcML3OTJiqza4YTsAB28VHHdjlCF5QCZLHM4vEQKZyzWGCkBGZlGl8AKADKCen+n5n1oYJcGJlQ0jikQIuT6LlEtxlhW4Teswt7b12QddzRb9kN3UZ/Qd0Mirf+9QOHLEGtEWJHSFApcM+tN6j5CtPwKu+4u/owDYrP/HbpBZCICxN/vZWvIFURnFO4hKFJcDg1J+2oLg8jnxedLbb9A52BhkKCZTVDWI5mCS1X47UTKdNs8CcVNvbsb0AUd9bpimhA7knfCm3yvOhijXYcUkuJemTEwJVAkS2WwXsFxp0JXFgguqrktGQtJoFv6BWBqMgzsZoyuG3EO7mHXL075YtLRcZEnqfGpI7VUGU7HVPayeM+OL0QtAvsQLKijvRk64cX4N3f64RXSrz2/vXtpEfm7IDQGweKPnd5nvgd0s=; passport_csrf_token=7426b2ef1d6a56942eead2fe021c53e7; passport_csrf_token_default=7426b2ef1d6a56942eead2fe021c53e7; s_v_web_id=verify_lcengirr_q2tgZsoS_tLmz_4vbX_9mmS_UIefeIRU7o5p; d_ticket=684eefc4bc2a7d61486b53be9818944596817; cmpl_token=AgQQAPPdF-RO0orQJvyb8s02-R16q9TWf4AzYMr4OA; passport_auth_status=823f267c17379de88f91109b849f379d%2C; passport_auth_status_ss=823f267c17379de88f91109b849f379d%2C; sid_guard=208a1b90bc8936dceb607c9def5d327a%7C1672654809%7C5184000%7CFri%2C+03-Mar-2023+10%3A20%3A09+GMT; uid_tt=69dddd056467e1ec757d5d7d6f86a3bf8ab1bb141d3925a926bfc34f5cba77e2; uid_tt_ss=69dddd056467e1ec757d5d7d6f86a3bf8ab1bb141d3925a926bfc34f5cba77e2; sid_tt=208a1b90bc8936dceb607c9def5d327a; sessionid=208a1b90bc8936dceb607c9def5d327a; sessionid_ss=208a1b90bc8936dceb607c9def5d327a; sid_ucp_v1=1.0.0-KGRkZWJjMTMzYmM0ZTcwMDAwNzhlYmNiZDAzZWUzZGM0ZjkwZDIyNmIKIAiPqICesYuy91oQ2d_KnQYYswsgDDDi_oncBTgCQPEHEAMaBm1hbGl2YSIgMjA4YTFiOTBiYzg5MzZkY2ViNjA3YzlkZWY1ZDMyN2E; ssid_ucp_v1=1.0.0-KGRkZWJjMTMzYmM0ZTcwMDAwNzhlYmNiZDAzZWUzZGM0ZjkwZDIyNmIKIAiPqICesYuy91oQ2d_KnQYYswsgDDDi_oncBTgCQPEHEAMaBm1hbGl2YSIgMjA4YTFiOTBiYzg5MzZkY2ViNjA3YzlkZWY1ZDMyN2E; store-idc=useast2a; store-country-code=pk; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=tjlVfVPDYNsqkm5pb2Azy2yaGTQSVA9qlRZAejVjbXQDBwZwqHrniMqQ9FUrbwFYCWAmX8aeJMmyWkMcbeQ5psdlVqYH4y8QDQzSOKvIYLkc7xAp2WsrEu59NgNPwbw483hr4OkD_1g5WIoXTLq_5GOEvXHCsZL79cVJ41XMRbC5zVZYhKjafzOGD0Hes9ejTsmsphwFl4HAayuz6JbeL0wqbDS3VUGkJZF74QnR8c0T5-b_9hD-By1lkbCBfdhkRZgfReNexsHBOlo7eozqNO6RQDTW-1bzSaimtGuk9J6cq6Q6C7mX35W2Wi_-fXDh_jTIleicI5E0VDLBF9RP-thrjSMX_rP87NcdEMxt8ql5xCdwGrlkPTgEoNF64THJ3io7CG9iIQhJ57gAHur99koWzCzm9mYBejle8qfyhr1yaskIrgyLip8Ljn_kfNtvazjPtB2BwqvnCdCfw2iGMqlWDE04z3QLGQBTZWIGbFKF6OR-6sJSjatK3vhcQHs6; passport_fe_beating_status=true; ttwid=1%7CwVc7_ykyUDLMLsg-G7V6t8ePiwrInQZcExKqtQbGpEk%7C1672654819%7C6a3ad6491267ff400a8895d7311210b49a2e8db0404b5f486e9ac4f48c730644; odin_tt=895c66332ec589eef9e598581a223ba87a1fc58d01a1a0511b4ef6a2c8881270117e2e4ee40fb19ba7ab297803b42042e1d3f95505e82c4b8cb540e87fda528ea8d57e128f510aeac8e8804dad33e0c0; msToken=qSoMvBrHIT8SeV6cmFyfzicrJStnmPDpcbkXacjrSOqTZJgMrtFf0S1jm0exbStAQZNTW2SKdVv1-xdU6oWv5GCVmVr0Fkyxg9Ukh8k6DF4hGqEUfamJ1B1eXN8F78unrY2y737EAPMdFZiQr_qX; bm_sv=B1F57B5310E9384730A4F5C7F444F256~YAAQHOldbreT+hGFAQAA6GT/cRJ+WeKpWPDJRbRhNo2s+fq+x278CJN06xFhzzJTcAfLttojbJrw+qr3N7aMcendm6z2+JjGF7SIsZg8lKA+9EE8doxtrNu2VfMvbzcz3cD/RYGTRSTyUWGzJy5r3hFFAmvA1dfwez/xmAFcNS5BwKMG5rQ8UUd/u463HmTNOywArK2qGoqSKofibUsX9bkDOIxPn9RHMVOQV5xoHhOYUgh7NHE6ke3wwdXZBwtH~1; msToken=rMwS17Nb6ip7X6TuVCD3XPsL8oljoBLXBTWLbR5H7-xSr4q6iaDB7ee-Q201snlT6vM2ABRsb1M2fE3KBaiYAvXJFj02f3JFUm1QIHU7qe9E10IO-PWlBxsexrw1cE96c3YPUSJSuQPr8joQsc4r",
        "referer": "https://www.tiktok.com/@{}?lang=en".format(user_name),
        "sec-ch-ua": '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    }

    url = (
        "https://www.tiktok.com/api/user/detail/?abTestVersion=%5Bobject%20Object%5D&aid=1988&appType=m&app_language=en&app_name=tiktok_web&battery_info=0.83&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7168854950909920770&device_platform=web_pc&focus_state=true&from_page=user&history_len=4&is_fullscreen=false&is_page_visible=true&language=en&os=windows&priority_region=PK&referer=https%3A%2F%2Fwww.tiktok.com%2F&region=PK&root_referer=https%3A%2F%2Fwww.tiktok.com%2F&screen_height=750&screen_width=1334&secUid=&tz_name=Asia%2FKarachi&uniqueId="
        + user_name
        + "&user=%5Bobject%20Object%5D&verifyFp=verify_lcengirr_q2tgZsoS_tLmz_4vbX_9mmS_UIefeIRU7o5p&webcast_language=en&msToken=NZl5MKcozvFfXxVSljXZW8hUSsp_lVQI5RgkaRgT0oCSjpdUiT16HKVsqPtcEhIg8ZOJ3M8npFIGOMk-MOJXognhQ5H-3NDKkPZgY9ajhojOM--jmwNRTgzz0_ningHMSyQdUIWazZOjopvrFb0N&X-Bogus=DFSzswVLaahANtdJSD2y-cYklTIv&_signature=_02B4Z6wo00001qNikFgAAIDDfRTI.DcI6tKjYpTAAMt207"
    )
    response = requests.get(url, headers=headers)

    def setUp(self) -> None:
        return super().setUp()

    def test_status_code(self, response=response):
        self.assertEqual(response.status_code, 200)

    def test_data_is_json(self, response=response):
        breakpoint()
        with open("basic.json", "w") as fl:
            json.dump(response.json(), fl)
        self.assertEqual(type(response.json()), type({}))

    def test_data_is_not_empty(self, response=response):
        self.assertNotEqual(response.json(), {})

    def tearDown(self) -> None:
        return super().tearDown()
