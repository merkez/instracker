import csv
import time
import os
import instaloader


username = os.getenv("username")
password = os.getenv("password")
timestamp = time.strftime("%Y-%m-%d_%H:%M")
insta_file_name = "inst_followers-{}.csv".format(timestamp)

instagram_loader = instaloader.Instaloader()
instagram_loader.login(username, password)
profile = instaloader.Profile.from_username(instagram_loader.context, username)

users = []
field_names = ["user_name", "full_name", "profile_pic_url"]
for followee in profile.get_followers():
    users.append({
            "user_name": followee.username,
            "full_name": followee.full_name,
            "profile_pic_url": followee.profile_pic_url,
        })

with open(insta_file_name, "w") as followers_file:
    writer = csv.DictWriter(followers_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(users)

