# date : 2020/5/7 15:29     

HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}
CONTENT_LIST_URL = "https://m.ximalaya.com/m-revision/common/album/queryAlbumTrackRecordsByPage?albumId=%s&page=%s&pageSize=20"

IMAGE_HOST = "https://imagev2.xmcdn.com/"

# 目录配置
import os
COVER_PATH = os.path.join("data", "cover")
MUSIC_PATH = os.path.join("data", "music")


# 数据库配置
from pymongo import MongoClient
MC = MongoClient()
MongoDB = MC['XMLY']

