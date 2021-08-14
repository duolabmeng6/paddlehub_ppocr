import requests
from pyefun import *
from pyefun.encoding.ebase64 import *

# 基于 Serverless 架构部署通用文字识别 PaddleOCR
# https://github.com/duolabmeng6/paddlehub_ppocr
# docker run -itd --name ppocr -p 9000:9000 ccr.ccs.tencentyun.com/llapi/pphubocr:1.0 /bin/bash -c "sh /PaddleOCR/start.sh"

def ocr(文件地址):
    image = base64编码(读入文件(文件地址))
    data = '{"images":["' + image + '"]}'
    txt = requests.post("http://127.0.0.1:9000/predict/ocr_system", data=data,
                        headers={'Content-Type': 'application/json'})
    return txt.content.decode("utf-8")

print(ocr("./test.png"))
