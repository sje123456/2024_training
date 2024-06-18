import requests
import zipfile
import os

# 下载URL
url = "https://bj.bcebos.com/apollo-air/v2-2022-01-08/single-vehicle-side-example_16160970215399424.zip?authorization=bce-auth-v1%2F62ff93831d5840338d0fcc9585430b3a%2F2024-06-17T01%3A39%3A54Z%2F604800%2F%2Fc6b499c053c62a3f43af463c38a0436f9fc40b20f72cfd198b3cd56e65b56e95"

# 发送GET请求下载文件
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 保存文件到本地
    with open("single-vehicle-side-example_1.zip", "wb") as f:
        f.write(response.content)
    print("文件下载成功！")

    # 解压文件
    with zipfile.ZipFile("single-vehicle-side-example_1.zip", "r") as zip_ref:
        zip_ref.extractall("extracted_files")
    print("文件解压成功！")
else:
    print("无法下载文件，状态码：", response.status_code)

# 删除下载的zip文件
os.remove("single-vehicle-side-example_1.zip")
