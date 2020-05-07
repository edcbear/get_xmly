# date : 2020/5/7 15:22     
import os
import datetime
import time
import requests
from setting import HEADERS,CONTENT_LIST_URL,IMAGE_HOST,COVER_PATH,MUSIC_PATH,MongoDB

content_dict = {
    "红楼": ["13383289", ],
    "三国": ["13396678", ]
}

def get_content_xmly():

    for tag, a_list in content_dict.items():
        for aid in a_list:
            page = 1
            while True:
                content_list = requests.get(CONTENT_LIST_URL % (aid, page), headers=HEADERS).json()
                if not content_list.get("data").get("trackDetailInfos"):
                    break
                content_mongo_list = []
                page += 1
                for content in content_list.get("data").get("trackDetailInfos"):
                    audio_name = content.get('trackInfo').get("title")

                    # 去除掉文件名可能会出现，并且引起报错的 |
                    if "|" in audio_name:
                        audio_name = audio_name.replace('|', '')
                    audio_url = content.get('trackInfo').get("playPath")
                    # 图片url
                    # audio_img_url = IMAGE_HOST+content.get('trackInfo').get("cover")

                    path1 = os.path.join(MUSIC_PATH, f'{tag}')
                    if not os.path.exists(path1):
                        os.makedirs(path1)

                    audio_path = os.path.join(MUSIC_PATH, f'{tag}', f'{audio_name}.mp3')

                    # 图片保存的地址
                    # audio_img_path = os.path.join(COVER_PATH, f'{tag}', f'{audio_name}.jpg')


                    # 保存音频文件
                    audio = requests.get(audio_url).content
                    with open(audio_path, "wb") as f:
                        f.write(audio)

                    # 保存图片
                    # audio_img = requests.get(audio_img_url).content
                    # with open(audio_img_path, "wb") as f:
                    #     f.write(audio_img)


                    # 把音频相关信息存入一个列表
                    content_info = {
                        "title": audio_name,
                        "music": f"{audio_name}.mp3",
                        "cover": f"{audio_name}.jpg",
                        "tag": tag,
                        "creatTime": datetime.datetime.now()
                    }
                    content_mongo_list.append(content_info)

                    time.sleep(1.5)

                # 把音频相关信息存入数据库
                print('存入数据库')
                MongoDB.contents.insert_many(content_mongo_list)

get_content_xmly()