import requests
# import os

# pic_path = "C:\Users\DELL\Pictures\Camera Roll\WIN_20231108_06_49_18_Pro.jpg"
# file_name = os.listdir(pic_path)
url = 'https://images.app.goo.gl/jWepNspXiANo8JrB6'
r = requests.get(url)
with open("timi.png", mode='wb') as mf:
    mf.write(r.content)
