"""
Develped by AneryCoft
Github:https://github.com/AneryCoft
2025.6.25
"""


import httpx
import json
import hashlib



url = "http://xxcx.hebeea.edu.cn/hebeea.xxcx/ptgk/app/cjcx.query" # 普通高考 成绩查询

with open("info.json", "r") as f:
    info = json.load(f)

id:str = info["id"] # 考生号
id_card:str = info["idCard"] # 身份证号
password:str = info["password"] # 密码

key = "TiXewdgMA3fa7LTI"
token:str = hashlib.md5((id + id_card + password + key).encode("utf-8")).hexdigest()

data = {
    "ksh": id,
    "sfzh": id_card,
    "mm": password,
    "user": "hebeeaApp",
    "token": token
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "okhttp/4.3.1"
}

client = httpx.Client(headers=headers, verify=False, timeout=10)

while True:
    try:
        response = client.post(url, data=data)
        if response.is_success:
            with open("scores.json", "w", encoding="utf-8") as f:
                json.dump(response.json(), f, ensure_ascii=False, indent=4)
                print("查询成功，成绩已保存到 scores.json")
            break
    except Exception as e:
        print(e)
        continue

"""
# 查询次数 
url = "http://count.hebeea.edu.cn/hebeeaCounter/queryCounterJson"
data = {
    "countCategory": "ptgk_cjcx",
    "clientCategory": "android",
    "isCount": "Y"
}
response = client.post(url, data=data)
count:str = response.json()["msg"]
"""