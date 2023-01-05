import json
from Utils import Utils
from BasicInfo import BasicInfo
from PostMedia import PostMedia

# from ParseJson import ParseJson

# Read Configuration as global variable
with open("config.json") as fl:
    config = json.loads(fl.read())

driver = Utils.get_session(config=config, return_browser=True)

userlist = ["jannatmirza"]
for user_name in userlist:
    basic_data = BasicInfo.get_basic_info(
        driver=driver,
        user_name=user_name,
        config=config,
    )
    print("[+]  Basic Data Grabbed Successfully")

    media_data = PostMedia.get_all_posts(
        driver=driver,
        config=config,
    )
    print("[+]  Media Data Grabbed Successfully")

# fl = open("C:\\Users\\DELL\\Desktop\\Sohaib\\fif_influencer.txt")
# userlist = fl.readlines()
# fl.close()
# for user_name in userlist:
#     basic_info = BasicInfo.get_basic_info(
#         session=session, user_name=user_name.replace("\n", "")
#     )
#     status = ParseJson.parse_and_dump_user_basic_info(
#         data=basic_info["data"]["user"],
#         config=config,
#         user_name=user_name.replace("\n", ""),
#     )
print("Done")  #
